from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path
from scripts.formateo_name_razon_social import formatear_razon_social, formatear_direccion
from scripts.compromisos_adicionales import (
    procesar_descuento_menu,
    procesar_mark_down,
    procesar_publicaciones_redes,
    procesar_platillos_top_seller,
    procesar_resumen_compromisos_adicionales,
)
from scripts.dependencias import resolver_dependencias
from scripts.solicitar_exclusividad import procesar_exclusividad
from scripts.numero_a_letras import numero_a_letras
from scripts.Paginacion import asignar_numeracion_clausulas

from scripts.Fondos import (
    procesar_fondo_mercadotecnia,
    procesar_fondo_mercadotecnia_ooh,
    procesar_linea_nuevas_aperturas,
)
from scripts.Bonos import (
    procesar_bono_crecimiento,
    procesar_bono_mercadotecnia,
    procesar_bono_nuevas_aperturas,
    procesar_bono_nuevas_aperturas_previo,
)
from scripts.comisiones import (
    procesar_comision_fija,
    procesar_comision_por_mes,
    procesar_comision_por_ordenes,
    procesar_comision_por_ventas,
)
from scripts.ads import procesar_ads
from scripts.datos_personas import (
    procesar_datos_persona_fisica,
    procesar_datos_persona_juridica,
)

BASE_DIR = Path(__file__).resolve().parent


PERSONA_FISICA = "fisica"
PERSONA_JURIDICA = "juridica"

def fecha(d: date) -> str:
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return f"{d.day} de {meses[d.month - 1]} de {d.year}"


def generar_acuerdo(datos, plantilla, salida_path=None):

    contexto = {}

    activas = {
        "activa_exclusividad": False,
        "activa_semi_exclusividad": False,
        "activa_ads": False,
        "activa_bono_crecimiento": False,
        "activa_bono_mercadotecnia": False,
        "activa_bono_nuevas_aperturas": False,
        "activa_bono_nuevas_aperturas_previo": False,
        "activa_fondo_mercadotecnia": False,
        "activa_fondo_mercadotecnia_ooh": False,
        "activa_linea_nuevas_aperturas": False,
        "activa_compromisos_adicionales": False,
        "activa_descuento_menu": False,
        "activa_mark_down": False,
        "activa_publicaciones_redes": False,
        "activa_platillos_top_seller": False,
        "activa_incumplimiento_bono_fondo": False,
        "activa_incumplimiento_exclusividad": False,
    }

    # --- datos generales según tipo de persona ---

    razon_social_limpia = formatear_razon_social(datos["razon_social"])
    direccion_limpia = formatear_direccion(datos["direccion"])

    if datos["tipo_persona"] == PERSONA_FISICA:
        procesar_datos_persona_fisica(
            razon_social_limpia,
            datos["rfc"],
            direccion_limpia,
            datos["marca"],
            contexto,
        )
    else:
        procesar_datos_persona_juridica(
            razon_social_limpia,
            datos["representante_legal"],
            datos["n_acta_constitutiva"],
            datos["fecha_acta_constitutiva"],
            datos["notario"],
            datos["numero_notaria"],
            datos["ubicacion_notaria"],
            datos["n_folio"],
            datos["fecha_folio_mercantil"],
            datos["rfc"],
            direccion_limpia,
            datos["marca"],
            contexto,
        )

    # --- vigencia ---
    contexto["VIGENCIA"] = datos["vigencia"]
    contexto["N_VIGENCIA"] = numero_a_letras(datos["vigencia"])

    # --- comisión ---
    tipo_comision = datos["tipo_comision"]

    if tipo_comision == "fija":
        procesar_comision_fija(datos["n_comision_fija"], contexto)
    elif tipo_comision == "mes":
        procesar_comision_por_mes(datos["tramos_comision"], contexto)
    elif tipo_comision == "ordenes":
        procesar_comision_por_ordenes(datos["tramos_comision"], contexto)
    elif tipo_comision == "ventas":
        procesar_comision_por_ventas(datos["tramos_comision"], contexto)
    else:
        raise ValueError("Tipo de comisión no válido")

    # --- exclusividad / semi ---
    procesar_exclusividad(datos["exclusividad"], activas, contexto)

    # --- ads ---
    if datos["tiene_ads"]:
        procesar_ads(activas, datos["n_ads"], contexto)

    # --- bonos ---
    procesar_bono_crecimiento(
        datos["aplica_bono_crecimiento"],
        datos.get("monto_bono_crecimiento"),
        activas,
        contexto,
    )
    procesar_bono_mercadotecnia(
        datos["aplica_bono_mercadotecnia"],
        datos.get("monto_bono_mercadotecnia"),
        activas,
        contexto,
    )

    if datos["aplica_bono_nuevas_aperturas"]:
        args = (
            datos["monto_nuevas_aperturas"],
            datos["num_establecimientos"],
            datos["meses_apertura"],
            datos["maximo_bono"],
            datos["periodo_amortizacion"],
            activas,
            contexto,
        )
        if datos["tipo_nuevas_aperturas"] == "posterior":
            procesar_bono_nuevas_aperturas(*args)
        else:
            procesar_bono_nuevas_aperturas_previo(*args)

    # --- fondos ---
    procesar_fondo_mercadotecnia(
        datos["aplica_fondo_mercadotecnia"],
        datos.get("monto_fondo_mercadotecnia"),
        activas,
        contexto,
    )
    procesar_fondo_mercadotecnia_ooh(
        datos["aplica_fondo_mercadotecnia_ooh"],
        datos.get("monto_fondo_mercadotecnia_ooh"),
        activas,
        contexto,
    )
    procesar_linea_nuevas_aperturas(
        datos["aplica_linea_nuevas_aperturas"],
        datos.get("monto_linea_nuevas_aperturas"),
        activas,
        contexto,
    )

    # --- compromisos adicionales ---
    procesar_descuento_menu(
        datos["aplica_descuento_menu"],
        datos.get("n_descuento_menu"),
        datos.get("n_meses_descuento_menu"),
        activas,
        contexto,
    )
    procesar_mark_down(
        datos["aplica_mark_down"],
        datos.get("n_descuento_mark_down"),
        activas,
        contexto,
    )
    procesar_publicaciones_redes(
        datos["aplica_publicaciones_redes"],
        datos.get("n_descuento_redes"),
        activas,
        contexto,
    )
    procesar_platillos_top_seller(
        datos["aplica_platillos_top_seller"],
        datos.get("n_cantidad_platillos"),
        datos.get("n_descuento_platillos"),
        datos.get("n_meses_descuento_platillos"),
        activas,
        contexto,
    )
    procesar_resumen_compromisos_adicionales(activas)

    resolver_dependencias(activas)
    asignar_numeracion_clausulas(activas, contexto)

    # --- correos ---
    contexto["CORREO_COMERCIAL"] = datos["correo_comercial"]
    contexto["CORREO_ALIADO"] = datos["correo_aliado"]

    # --- datos bancarios ---
    contexto["N_CUENTA"] = datos["n_cuenta"]
    contexto["N_CLABE"] = datos["n_clabe"]
    contexto["BANCO"] = datos["banco"]

    contexto["tipo_comision"] = tipo_comision
    contexto["fecha"] = fecha(date.today())

    nombre_acuerdo = f"{fecha(date.today())} Acuerdo de cooperación. Rappi & {contexto['RAZÓN_SOCIAL']}.docx"
    if salida_path is None:
        salida = BASE_DIR / "salida_acuerdos" / nombre_acuerdo
    else:
        salida = Path(salida_path)
        if salida.suffix != ".docx":
            salida = salida / nombre_acuerdo
    salida.parent.mkdir(parents=True, exist_ok=True)

    contexto.update(activas)

    docx = DocxTemplate(plantilla)
    docx.render(contexto, autoescape=True)
    docx.save(salida)

    return salida
