"""Pruebas: montos con comas y máximo 9 dígitos."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app, entero_monto
from scripts.validaciones import validar_formulario, _no_es_monto

BASE = {
    "tipo_persona": "fisica",
    "razon_social_fisica": "Ana Lopez",
    "rfc_fisica": "LOPA800101ABC",
    "direccion_fisica": "Calle 1",
    "marca_fisica": "Marca",
    "vigencia_meses": "12",
    "tipo_comision": "fija",
    "n_comision_fija": "18",
    "exclusividad": "3",
    "correo_comercial": "a@b.com",
    "correo_aliado": "c@d.com",
    "n_clabe": "012345678901234567",
    "n_cuenta": "1234567890",
    "banco": "Banorte",
}


def main():
    errores = []

    if entero_monto("1,000") != 1000:
        errores.append("entero_monto 1,000")
    if entero_monto("500,000,000") != 500_000_000:
        errores.append("entero_monto 500M")

    form_ok = dict(BASE)
    form_ok["activa_bono_crecimiento"] = "si"
    form_ok["monto_bono_crecimiento"] = "999,999,999"
    if validar_formulario(form_ok):
        errores.append("debe aceptar 999,999,999")

    form_diez = dict(form_ok)
    form_diez["monto_bono_crecimiento"] = "1,000,000,000"
    if not validar_formulario(form_diez).get("monto_bono_crecimiento"):
        errores.append("debe rechazar 10 dígitos")

    if not _no_es_monto({"monto_bono_crecimiento": "1,000,000,000"}, "monto_bono_crecimiento"):
        errores.append("_no_es_monto debe fallar con 10 dígitos")

    if _no_es_monto({"monto_bono_crecimiento": "500,000,000"}, "monto_bono_crecimiento"):
        errores.append("_no_es_monto debe aceptar 500,000,000")

    with app.test_client() as client:
        html = client.get("/acuerdos").data.decode()
        if "input-monto" not in html:
            errores.append("falta clase input-monto en HTML")
        if "formulario.js?v=20261005c" not in html:
            errores.append("falta cache bust formulario.js")
        for campo in (
            "monto_bono_crecimiento",
            "monto_bono_mercadotecnia",
            "monto_nuevas_aperturas",
            "maximo_bono",
            "monto_fondo_mercadotecnia",
            "monto_linea_nuevas_aperturas",
        ):
            if f'id="{campo}"' not in html:
                errores.append(f"falta campo {campo}")

    if errores:
        print("FALLÓ:", "; ".join(errores))
        raise SystemExit(1)
    print("OK: pruebas de montos (9 dígitos) y HTML")


if __name__ == "__main__":
    main()
