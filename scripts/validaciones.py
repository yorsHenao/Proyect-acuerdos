"""
Validación del formulario de generación de acuerdoS.

Revisa request.form ANTES de construir el diccionario `datos`, replicando
las mismas condiciones que usa app.py, y devuelve un diccionario de errores:
    { "nombre_campo_html": "Mensaje para el usuario" }

Si el diccionario devuelto está vacío, el formulario es válido y se puede
continuar con la generación del acuerdo.
"""

import re

CORREO_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def _correo_invalido(form, campo):
    
    valor = form.get(campo, "")
    if valor is None or valor.strip() == "":
        return True
    return not CORREO_REGEX.match(valor.strip())

def _falta(form, campo):
    
    valor = form.get(campo, "")
    return valor is None or valor.strip() == ""


def _no_es_numero(form, campo):
    valor = form.get(campo, "")
    if valor is None or valor.strip() == "":
        return True
    try:
        numero = float(valor)
        return numero < 0  
    except ValueError:
        return True


def _no_es_monto(form, campo):
    valor = form.get(campo, "")
    if valor is None or valor.strip() == "":
        return True
    try:
        monto = int(valor.replace(".", ""))
        return monto < 0  
    except ValueError:
        return True


# limite de caracteres para campos de texto
def _demasiado_largo(form, campo, maximo):
    """True si el campo supera el máximo de caracteres permitido."""
    valor = form.get(campo, "")
    return len(valor) > maximo

CAMPOS_CORTOS = [
    "razon_social_fisica", "razon_social_juridica",
    "rfc_fisica", "rfc_juridica",
    "marca_fisica", "marca_juridica",
    "representante_legal_juridica",
    "notario", "numero_notaria",
    "n_acta_constitutiva", "n_folio_mercantil",
]

CAMPOS_LARGOS = [
    "direccion_fisica", "direccion_juridica",
    "ubicacion_notaria",
]

def validar_formulario(form):
    errores = {}

    # --- tipo de persona ---
    tipo_persona = form.get("tipo_persona")
    if tipo_persona not in ("fisica", "juridica"):
        errores["tipo_persona"] = "Selecciona el tipo de persona."
        tipo_persona = None  #

    if tipo_persona == "fisica":
        for campo, etiqueta in [
            ("razon_social_fisica", "La razón social es obligatoria."),
            ("rfc_fisica", "El RFC es obligatorio."),
            ("direccion_fisica", "La dirección es obligatoria."),
            ("marca_fisica", "La marca es obligatoria."),
        ]:
            if _falta(form, campo):
                errores[campo] = etiqueta

    elif tipo_persona == "juridica":
        for campo, etiqueta in [
            ("razon_social_juridica", "La razón social es obligatoria."),
            ("rfc_juridica", "El RFC es obligatorio."),
            ("representante_legal_juridica", "El representante legal es obligatorio."),
            ("direccion_juridica", "La dirección es obligatoria."),
            ("marca_juridica", "La marca es obligatoria."),
            ("n_acta_constitutiva", "El número de acta constitutiva es obligatorio."),
            ("fecha_acta_constitutiva", "La fecha del acta constitutiva es obligatoria."),
            ("notario", "El nombre del notario es obligatorio."),
            ("numero_notaria", "El número de notaría es obligatorio."),
            ("ubicacion_notaria", "La ubicación de la notaría es obligatoria."),
            ("n_folio_mercantil", "El número de folio mercantil es obligatorio."),
            ("fecha_folio_mercantil", "La fecha del folio mercantil es obligatoria."),
        ]:
            if _falta(form, campo):
                errores[campo] = etiqueta

    # --- longitud máxima de campos de texto libre ---
    for campo in CAMPOS_CORTOS:
        if not _falta(form, campo) and _demasiado_largo(form, campo, 100):
            errores[campo] = "Este campo no puede superar los 100 caracteres."

    for campo in CAMPOS_LARGOS:
        if not _falta(form, campo) and _demasiado_largo(form, campo, 200):
            errores[campo] = "Este campo no puede superar los 200 caracteres."

    # --- vigencia ---
    if _falta(form, "vigencia_meses"):
        errores["vigencia_meses"] = "La vigencia en meses es obligatoria."
    elif _no_es_numero(form, "vigencia_meses"):
        errores["vigencia_meses"] = "La vigencia debe ser un número."
    else:
        try:
            vigencia = int(form.get("vigencia_meses"))
            if vigencia < 1:
                errores["vigencia_meses"] = "La vigencia debe ser mayor a 0 meses."
            elif vigencia > 120:
                errores["vigencia_meses"] = "La vigencia no puede exceder 120 meses."
        except (ValueError, TypeError):
            errores["vigencia_meses"] = "La vigencia debe ser un número válido."

    # --- ads ---
    if "tiene_ads" in form:
        if _falta(form, "n_ads"):
            errores["n_ads"] = "Indica el porcentaje de ADS."
        elif _no_es_numero(form, "n_ads"):
            errores["n_ads"] = "El porcentaje de ADS debe ser un número."

    # --- comisión ---
    tipo_comision = form.get("tipo_comision")
    if _falta(form, "tipo_comision"):
        errores["tipo_comision"] = "Selecciona un tipo de comisión."
    else:
        tipo_comision_final = tipo_comision
        if tipo_comision == "escalonada":
            if _falta(form, "modalidad_escalonada"):
                errores["modalidad_escalonada"] = "Selecciona la modalidad escalonada."
            tipo_comision_final = form.get("modalidad_escalonada")

        if tipo_comision_final == "fija":
            if _falta(form, "n_comision_fija"):
                errores["n_comision_fija"] = "El porcentaje de comisión fija es obligatorio."
            elif _no_es_numero(form, "n_comision_fija"):
                errores["n_comision_fija"] = "La comisión fija debe ser un número."
        elif tipo_comision_final in ("mes", "ordenes", "ventas"):
            if f"escalon_0_porcentaje" not in form:
                errores["escalon_0_porcentaje"] = "Agrega al menos un tramo de comisión."
            else:
                indice = 0
                while f"escalon_{indice}_porcentaje" in form:
                    campo_pct = f"escalon_{indice}_porcentaje"
                    if _no_es_numero(form, campo_pct):
                        errores[campo_pct] = f"El porcentaje del tramo {indice + 1} debe ser un número."

                    es_ultimo = form.get(f"escalon_{indice}_es_ultimo") == "si"
                    if not es_ultimo:
                        campo_fin = f"escalon_{indice}_fin"
                        if _falta(form, campo_fin):
                            errores[campo_fin] = f"Completa el límite del tramo {indice + 1}."
                        elif _no_es_numero(form, campo_fin):
                            errores[campo_fin] = f"El límite del tramo {indice + 1} debe ser un número."
                    indice += 1

    # --- exclusividad ---
    if _falta(form, "exclusividad"):
        errores["exclusividad"] = "Selecciona una opción de exclusividad."

    # --- bonos ---
    if "activa_bono_crecimiento" in form and _no_es_monto(form, "monto_bono_crecimiento"):
        errores["monto_bono_crecimiento"] = "Indica el monto del bono de crecimiento."

    if "activa_bono_mercadotecnia" in form and _no_es_monto(form, "monto_bono_mercadotecnia"):
        errores["monto_bono_mercadotecnia"] = "Indica el monto del bono de mercadotecnia."

    if "activa_bono_nuevas_aperturas" in form:
        if _falta(form, "tipo_nuevas_aperturas"):
            errores["tipo_nuevas_aperturas"] = "Selecciona el tipo de bono de nuevas aperturas."
        for campo, etiqueta, validador in [
            ("monto_nuevas_aperturas", "Indica el monto del bono de nuevas aperturas.", _no_es_monto),
            ("num_establecimientos", "Indica el número de establecimientos.", _no_es_numero),
            ("meses_apertura", "Indica los meses para abrir los establecimientos.", _no_es_numero),
            ("maximo_bono", "Indica el apoyo máximo por establecimiento.", _no_es_monto),
            ("periodo_amortizacion", "Indica el periodo de amortización.", _no_es_numero),
        ]:
            if validador(form, campo):
                errores[campo] = etiqueta

    # --- fondos ---
    if "activa_fondo_mercadotecnia" in form and _no_es_monto(form, "monto_fondo_mercadotecnia"):
        errores["monto_fondo_mercadotecnia"] = "Indica el monto del fondo de mercadotecnia."

    if "activa_fondo_mercadotecnia_ooh" in form and _no_es_monto(form, "monto_fondo_mercadotecnia_ooh"):
        errores["monto_fondo_mercadotecnia_ooh"] = "Indica el monto del fondo de mercadotecnia OOH."

    if "activa_linea_nuevas_aperturas" in form and _no_es_monto(form, "monto_linea_nuevas_aperturas"):
        errores["monto_linea_nuevas_aperturas"] = "Indica el monto de la línea de nuevas aperturas."

    # --- compromisos adicionales ---
    if "activa_descuento_menu" in form:
        if _no_es_numero(form, "n_descuento_menu"):
            errores["n_descuento_menu"] = "Indica el porcentaje de descuento en menú."
        if _no_es_numero(form, "n_meses_descuento_menu"):
            errores["n_meses_descuento_menu"] = "Indica los meses de descuento en menú."

    if "activa_mark_down" in form and _no_es_numero(form, "n_descuento_mark_down"):
        errores["n_descuento_mark_down"] = "Indica el porcentaje de mark down."

    if "activa_publicaciones_redes" in form and _no_es_numero(form, "n_descuento_redes"):
        errores["n_descuento_redes"] = "Indica el porcentaje de descuento en redes."

    if "activa_platillos_top_seller" in form:
        for campo, etiqueta in [
            ("n_cantidad_platillos", "Indica la cantidad de platillos."),
            ("n_descuento_platillos", "Indica el porcentaje de descuento en platillos."),
            ("n_meses_descuento_platillos", "Indica los meses de descuento en platillos."),
        ]:
            if _no_es_numero(form, campo):
                errores[campo] = etiqueta

    # --- correos ---
    if _falta(form, "correo_comercial"):
        errores["correo_comercial"] = "El correo comercial es obligatorio."
    elif _correo_invalido(form, "correo_comercial"):
        errores["correo_comercial"] = "Ingresa un correo comercial válido."

    if _falta(form, "correo_aliado"):
        errores["correo_aliado"] = "El correo del aliado es obligatorio."
    elif _correo_invalido(form, "correo_aliado"):
        errores["correo_aliado"] = "Ingresa un correo del aliado válido."

    # --- datos bancarios ---
    if _falta(form, "n_clabe"):
        errores["n_clabe"] = "La CLABE es obligatoria."
    if _falta(form, "n_cuenta"):
        errores["n_cuenta"] = "El número de cuenta es obligatorio."
    if _falta(form, "banco"):
        errores["banco"] = "El banco es obligatorio."

    return errores