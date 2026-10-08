"""Regresión: numeración de cláusulas alineada con plantillas New_draft."""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.Paginacion import (
    asignar_numeracion_clausulas,
    numero_a_ordinal,
    CATALOGO_CLAUSULAS,
    OBLIGACIONES_CLAUSULA_CUARTA,
)
from scripts.generar_acuerdo import generar_acuerdo

_NUM_SOLO_DATOS = frozenset(
    {
        "NUM_ESTABLECIMIENTOS",
        "NUM_MESES",
        "NUM_MAXIMO_BONO",
        "NUM_PERIODO_AMORTIZACIÓN",
        "NUM_PERIODO_AMORTIZACION",
    }
)


def _texto_plantilla_docx(ruta: Path) -> str:
    """Une runs de Word para no partir placeholders Jinja."""
    xml = zipfile.ZipFile(ruta).read("word/document.xml").decode("utf-8")
    text = re.sub(r"</w:t>", "", xml)
    text = re.sub(r"<w:t[^>]*>", "", text)
    return re.sub(r"<[^>]+>", "", text)


def _num_clausulas_en_plantilla(ruta: Path) -> set[str]:
    texto = _texto_plantilla_docx(ruta)
    return {
        m
        for m in re.findall(r"NUM_[A-ZÁÉÍÓÚÑ_]+", texto)
        if m not in _NUM_SOLO_DATOS
    }


def _verificar_catalogo_alineado_con_plantillas(errores: list[str]) -> None:
    base = Path("formatos/New_draft")
    if not base.is_dir():
        return
    en_plantillas: set[str] = set()
    rom_en_plantillas: set[str] = set()
    for plantilla in sorted(base.glob("acuerdo*.docx")):
        en_plantillas |= _num_clausulas_en_plantilla(plantilla)
        texto = _texto_plantilla_docx(plantilla)
        rom_en_plantillas |= set(re.findall(r"ROM_[A-Z_]+", texto))

    catalogo = {variable for variable, _ in CATALOGO_CLAUSULAS}
    rom_catalogo = {variable for variable, _ in OBLIGACIONES_CLAUSULA_CUARTA}

    solo_catalogo = sorted(catalogo - en_plantillas)
    solo_plantilla = sorted(en_plantillas - catalogo)
    if solo_catalogo:
        errores.append(f"NUM_* en catálogo sin plantilla: {', '.join(solo_catalogo)}")
    if solo_plantilla:
        errores.append(f"NUM_* en plantilla sin catálogo: {', '.join(solo_plantilla)}")

    rom_solo_catalogo = sorted(rom_catalogo - rom_en_plantillas)
    if rom_solo_catalogo and rom_en_plantillas:
        # ROM_ADS solo en plantillas con ADS; el catálogo ROM es superset válido.
        rom_extra = set(rom_solo_catalogo) - {"ROM_ADS"}
        if rom_extra:
            errores.append(f"ROM_* en catálogo sin ninguna plantilla: {', '.join(sorted(rom_extra))}")


def _activas_brew_brew():
    """Exclusividad + ADS + bono crecimiento (escenario tipo Brew Brew)."""
    flags = {flag: False for _, flag in CATALOGO_CLAUSULAS if flag}
    flags.update(
        {
            "activa_exclusividad": True,
            "activa_ads": True,
            "activa_bono_crecimiento": True,
            "activa_incumplimiento_bono_fondo": True,
        }
    )
    return flags


def _ordinales_asignados(activas):
    contexto = {}
    asignar_numeracion_clausulas(activas, contexto)
    return contexto


def main():
    errores = []
    _verificar_catalogo_alineado_con_plantillas(errores)

    activas = _activas_brew_brew()
    ctx = _ordinales_asignados(activas)

    if ctx.get("NUM_EXCLUSIVIDAD") != numero_a_ordinal(14):
        errores.append("exclusividad debe ser DÉCIMA CUARTA (14)")
    if ctx.get("NUM_BONO_CRECIMIENTO") != numero_a_ordinal(15):
        errores.append(
            f"bono debe ser DÉCIMA QUINTA (15), obtuvo {ctx.get('NUM_BONO_CRECIMIENTO')}"
        )
    if "NUM_INVERSIÓN_ADS" in ctx:
        errores.append("NUM_INVERSIÓN_ADS no debe asignarse (ADS en cláusula 4)")
    if "NUM_COMPROMISOS_ADICIONALES" in ctx:
        errores.append("NUM_COMPROMISOS_ADICIONALES no debe asignarse")

    datos = {
        "tipo_persona": "juridica",
        "razon_social": "Brew Brew S.A. de C.V.",
        "rfc": "BBR123456789",
        "direccion": "Calle 1, CDMX",
        "marca": "Brew Brew",
        "representante_legal": "Ana Representante",
        "n_acta_constitutiva": "12345",
        "fecha_acta_constitutiva": "1 de enero de 2020",
        "notario": "Lic. Notario",
        "numero_notaria": "10",
        "ubicacion_notaria": "Ciudad de México",
        "n_folio": "FM-001",
        "fecha_folio_mercantil": "2 de febrero de 2020",
        "vigencia": 24,
        "tipo_comision": "fija",
        "n_comision_fija": 18,
        "exclusividad": "1",
        "tiene_ads": True,
        "n_ads": 12,
        "tipo_ads": "aliado",
        "aplica_bono_crecimiento": True,
        "monto_bono_crecimiento": 500_000,
        "aplica_bono_mercadotecnia": False,
        "aplica_bono_nuevas_aperturas": False,
        "aplica_fondo_mercadotecnia": False,
        "aplica_linea_nuevas_aperturas": False,
        "aplica_descuento_menu": False,
        "aplica_mark_down": False,
        "aplica_publicaciones_redes": False,
        "aplica_platillos_top_seller": False,
        "correo_comercial": "comercial@rappi.com",
        "correo_aliado": "legal@brewbrew.com",
        "n_clabe": "012345678901234567",
        "n_cuenta": "1234567890",
        "banco": "Banorte",
    }
    plantilla = Path("formatos/New_draft/acuerdo_con_ads_juridica.docx")
    salida = Path(__file__).resolve().parent / "_tmp_test_numeracion.docx"
    if plantilla.exists():
        generar_acuerdo(datos, plantilla, salida)
        texto = _texto_plantilla_docx(salida)
        if "DÉCIMA CUARTA" in texto and "DÉCIMA SEXTA. - Bono de Crecimiento" in texto:
            errores.append(
                "documento aún salta de DÉCIMA CUARTA a DÉCIMA SEXTA en bono de crecimiento"
            )
        if "DÉCIMA QUINTA. - Bono de Crecimiento" not in texto:
            errores.append("falta DÉCIMA QUINTA en título del bono de crecimiento")
        salida.unlink(missing_ok=True)

    if errores:
        print("FALLÓ:", "; ".join(errores))
        raise SystemExit(1)
    print("OK: numeración de cláusulas (ADS/compromisos sin NUM_ fantasma)")


if __name__ == "__main__":
    main()
