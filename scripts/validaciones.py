
import re

REGEX_NOMBRES = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\-\s]+$")
REGEX_RAZON_SOCIAL = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9.,&\-\s]+$")
REGEX_DIRECCION = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9.,#/\-\s]+$")
REGEX_RFC = re.compile(r"^[A-Z0-9]+$")
REGEX_ALFANUMERICO = re.compile(r"^[a-zA-Z0-9\-/\s]+$")
REGEX_CORREO = re.compile(r"^[a-zA-Z0-9@._+\-]+$")

CORREO_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def _correo_invalido(form, campo):
    
    valor = form.get(campo, "")
    if valor is None or valor.strip() == "":
        return True
    return not CORREO_REGEX.match(valor.strip())

def _falta(form, campo):
    
    valor = form.get(campo, "")
    return valor is None or valor.strip() == ""


def _no_es_porcentaje_dos_digitos(form, campo):
    valor = form.get(campo, "")
    if valor is None or not str(valor).strip().isdigit():
        return True
    numero = int(str(valor).strip())
    return numero < 10 or numero > 99


def _no_es_porcentaje_un_digito(form, campo):
    valor = form.get(campo, "")
    if valor is None or not str(valor).strip().isdigit():
        return True
    numero = int(str(valor).strip())
    return numero < 1 or numero > 9


def _fuera_de_rango(form, campo, minimo, maximo):
    valor = form.get(campo, "")
    if valor is None or not str(valor).strip().isdigit():
        return True
    numero = int(str(valor).strip())
    return numero < minimo or numero > maximo


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
    texto = valor.strip().replace(",", "")
    if not re.fullmatch(r"\d+(\.\d{1,2})?", texto):
        return True
    if "." in texto:
        entero, decimal = texto.split(".", 1)
        if int(decimal) != 0:
            return True
    else:
        entero = texto
    if len(entero) > 9:
        return True
    monto = int(entero)
    return monto < 0


def _no_cumple_formato(form, campo, patron):
    valor = form.get(campo, "")
    if valor is None or valor.strip() == "":
        return False  # el campo vacio ya lo marca _falta, no lo dupliques aqui

    valor_limpio = valor.strip()
    if patron is REGEX_RFC:
        valor_limpio = valor_limpio.upper()

    return patron.fullmatch(valor_limpio) is None


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

        if _falta(form, "razon_social_fisica"):
            errores["razon_social_fisica"] = "La razón social es obligatoria."
        elif _no_cumple_formato(form, "razon_social_fisica", REGEX_NOMBRES):
            errores["razon_social_fisica"] = "El nombre solo puede contener letras."

        if _falta(form, "rfc_fisica"):
            errores["rfc_fisica"] = "El RFC es obligatorio."
        elif _no_cumple_formato(form, "rfc_fisica", REGEX_RFC):
            errores["rfc_fisica"] = "El RFC solo puede contener letras mayúsculas y números."

        if _falta(form, "direccion_fisica"):
            errores["direccion_fisica"] = "La dirección es obligatoria."
        elif _no_cumple_formato(form, "direccion_fisica", REGEX_DIRECCION):
            errores["direccion_fisica"] = "La dirección tiene caracteres no permitidos."

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

        if _falta(form, "razon_social_juridica"):
            errores["razon_social_juridica"] = "La razón social es obligatoria."
        elif _no_cumple_formato(form, "razon_social_juridica", REGEX_RAZON_SOCIAL):
            errores["razon_social_juridica"] = "La razón social tiene caracteres no permitidos."

        if _falta(form, "rfc_juridica"):
            errores["rfc_juridica"] = "El RFC es obligatorio."
        elif _no_cumple_formato(form, "rfc_juridica", REGEX_RFC):
            errores["rfc_juridica"] = "El RFC solo puede contener letras mayúsculas y números."

        if _falta(form, "representante_legal_juridica"):
            errores["representante_legal_juridica"] = "El representante legal es obligatorio."
        elif _no_cumple_formato(form, "representante_legal_juridica", REGEX_NOMBRES):
            errores["representante_legal_juridica"] = "El nombre solo puede contener letras."

        if _falta(form, "direccion_juridica"):
            errores["direccion_juridica"] = "La dirección es obligatoria."
        elif _no_cumple_formato(form, "direccion_juridica", REGEX_DIRECCION):
            errores["direccion_juridica"] = "La dirección tiene caracteres no permitidos."

        if _falta(form, "n_acta_constitutiva"):
            errores["n_acta_constitutiva"] = "El número de acta constitutiva es obligatorio."
        else:
            digitos = form.get("n_acta_constitutiva", "").replace(".", "")
            if not digitos.isdigit():
                errores["n_acta_constitutiva"] = "El número de acta solo puede contener números."

        if _falta(form, "notario"):
            errores["notario"] = "El nombre del notario es obligatorio."
        elif _no_cumple_formato(form, "notario", REGEX_NOMBRES):
            errores["notario"] = "El nombre solo puede contener letras."

        if _falta(form, "ubicacion_notaria"):
            errores["ubicacion_notaria"] = "La ubicación de la notaría es obligatoria."
        elif _no_cumple_formato(form, "ubicacion_notaria", REGEX_DIRECCION):
            errores["ubicacion_notaria"] = "La ubicación tiene caracteres no permitidos."

        if _falta(form, "n_folio_mercantil"):
            errores["n_folio_mercantil"] = "El número de folio mercantil es obligatorio."
        elif _no_cumple_formato(form, "n_folio_mercantil", REGEX_ALFANUMERICO):
            errores["n_folio_mercantil"] = "El folio mercantil tiene caracteres no permitidos."

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
            if vigencia < 1 or vigencia > 99:
                errores["vigencia_meses"] = "La vigencia debe estar entre 1 y 99 meses."
        except (ValueError, TypeError):
            errores["vigencia_meses"] = "La vigencia debe ser un número válido."

    # --- ads ---
    if "tiene_ads" in form:
        if form.get("tipo_ads") not in ("aliado", "aliado_y_rappi"):
            errores["tipo_ads"] = "Selecciona la modalidad de ADS."
        if _falta(form, "n_ads"):
            errores["n_ads"] = "Indica el porcentaje de ADS."
        elif _no_es_porcentaje_un_digito(form, "n_ads"):
            errores["n_ads"] = "El porcentaje de ADS debe ser de un dígito (1 a 9)."
        if form.get("tipo_ads") == "aliado_y_rappi":
            if _falta(form, "n_ads_rappi"):
                errores["n_ads_rappi"] = "Indica el porcentaje de ADS de Rappi."
            elif _no_es_porcentaje_un_digito(form, "n_ads_rappi"):
                errores["n_ads_rappi"] = "El porcentaje de ADS de Rappi debe ser de un dígito (1 a 9)."

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
            elif _no_es_porcentaje_dos_digitos(form, "n_comision_fija"):
                errores["n_comision_fija"] = "La comisión fija debe estar entre 10 y 99."
        elif tipo_comision_final == "ventas":
            errores["modalidad_escalonada"] = "La comisión por ventas no está disponible."
        elif tipo_comision_final == "ordenes":
            if _falta(form, "ordenes_primer_anio") or _no_es_porcentaje_dos_digitos(form, "ordenes_primer_anio"):
                errores["ordenes_primer_anio"] = "El porcentaje del primer año debe estar entre 10 y 99."
            if _falta(form, "max_ordenes") or _fuera_de_rango(form, "max_ordenes", 1, 999):
                errores["max_ordenes"] = "El máximo de órdenes debe tener de 1 a 3 dígitos."
            if _falta(form, "n_comision_1") or _no_es_porcentaje_dos_digitos(form, "n_comision_1"):
                errores["n_comision_1"] = "El take rate debe estar entre 10 y 99."
        elif tipo_comision_final == "mes":
            if f"escalon_0_porcentaje" not in form:
                errores["escalon_0_porcentaje"] = "Agrega al menos un tramo de comisión."
            else:
                indice = 0
                while f"escalon_{indice}_porcentaje" in form:
                    campo_pct = f"escalon_{indice}_porcentaje"
                    if _no_es_porcentaje_dos_digitos(form, campo_pct):
                        errores[campo_pct] = f"El porcentaje del tramo {indice + 1} debe estar entre 10 y 99."

                    es_ultimo = form.get(f"escalon_{indice}_es_ultimo") == "si"
                    if not es_ultimo:
                        campo_fin = f"escalon_{indice}_fin"
                        if _falta(form, campo_fin):
                            errores[campo_fin] = f"Completa el límite del tramo {indice + 1}."
                        elif _fuera_de_rango(form, campo_fin, 1, 999):
                            errores[campo_fin] = f"El límite del tramo {indice + 1} debe tener de 1 a 3 dígitos."
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
            ("num_establecimientos", "El número de establecimientos debe ser de un dígito (1 a 9).", lambda form, campo: _fuera_de_rango(form, campo, 1, 9)),
            ("meses_apertura", "Los meses para abrir establecimientos deben tener de 1 a 3 dígitos.", lambda form, campo: _fuera_de_rango(form, campo, 1, 999)),
            ("maximo_bono", "Indica el apoyo máximo por establecimiento.", _no_es_monto),
            ("periodo_amortizacion", "El periodo de amortización debe tener de 1 a 2 dígitos (1 a 99).", lambda form, campo: _fuera_de_rango(form, campo, 1, 99)),
        ]:
            if validador(form, campo):
                errores[campo] = etiqueta

    # --- fondos ---
    if "activa_fondo_mercadotecnia" in form and _no_es_monto(form, "monto_fondo_mercadotecnia"):
        errores["monto_fondo_mercadotecnia"] = "Indica el monto del fondo de mercadotecnia."

    if "activa_linea_nuevas_aperturas" in form and _no_es_monto(form, "monto_linea_nuevas_aperturas"):
        errores["monto_linea_nuevas_aperturas"] = "Indica el monto de la línea de nuevas aperturas."

    # --- compromisos adicionales ---
    if "activa_descuento_menu" in form:
        if _no_es_porcentaje_dos_digitos(form, "n_descuento_menu"):
            errores["n_descuento_menu"] = "El porcentaje de descuento en menú debe tener mínimo 2 dígitos (10 a 99)."
        if _fuera_de_rango(form, "n_meses_descuento_menu", 1, 99):
            errores["n_meses_descuento_menu"] = "Los meses de descuento en menú deben estar entre 1 y 99."

    if "activa_mark_down" in form and _fuera_de_rango(form, "n_descuento_mark_down", 1, 99):
        errores["n_descuento_mark_down"] = "El porcentaje de mark down debe estar entre 1 y 99."

    if "activa_publicaciones_redes" in form and _fuera_de_rango(form, "n_descuento_redes", 1, 99):
        errores["n_descuento_redes"] = "La cantidad de publicaciones debe estar entre 1 y 99."

    if "activa_platillos_top_seller" in form:
        if _fuera_de_rango(form, "n_cantidad_platillos", 1, 999):
            errores["n_cantidad_platillos"] = "La cantidad de platillos debe tener de 1 a 3 dígitos."
        if _no_es_porcentaje_dos_digitos(form, "n_descuento_platillos"):
            errores["n_descuento_platillos"] = "El porcentaje de descuento en platillos debe estar entre 10 y 99."
        if _fuera_de_rango(form, "n_meses_descuento_platillos", 1, 999):
            errores["n_meses_descuento_platillos"] = "Los meses de platillos deben tener de 1 a 3 dígitos."

    # --- correos ---
    if _falta(form, "correo_comercial"):
        errores["correo_comercial"] = "El correo comercial es obligatorio."
    elif _no_cumple_formato(form, "correo_comercial", REGEX_CORREO):
        errores["correo_comercial"] = "El correo comercial tiene un formato inválido."
    elif _correo_invalido(form, "correo_comercial"):
        errores["correo_comercial"] = "Ingresa un correo comercial válido."

    if _falta(form, "correo_aliado"):
        errores["correo_aliado"] = "El correo del aliado es obligatorio."
    elif _no_cumple_formato(form, "correo_aliado", REGEX_CORREO):
        errores["correo_aliado"] = "El correo del aliado tiene un formato inválido."
    elif _correo_invalido(form, "correo_aliado"):
        errores["correo_aliado"] = "Ingresa un correo del aliado válido."

    # --- datos bancarios ---
    if _falta(form, "n_clabe"):
        errores["n_clabe"] = "La CLABE es obligatoria."
    if _falta(form, "n_cuenta"):
        errores["n_cuenta"] = "El número de cuenta es obligatorio."
    if _falta(form, "banco"):
        errores["banco"] = "El banco es obligatorio."
    elif _no_cumple_formato(form, "banco", REGEX_NOMBRES):
        errores["banco"] = "El banco solo puede contener letras."

    return errores


def validar_formulario_cesion(form):
    errores = {}

    # --- Tipo de Cedente ---
    tipo_cedente = form.get("tipo_cedente")
    if tipo_cedente not in ("fisica", "moral"):
        errores["tipo_cedente"] = "Selecciona el tipo de persona del cedente."
        tipo_cedente = None

    if tipo_cedente == "fisica":
        if _falta(form, "nombre_cedente"):
            errores["nombre_cedente"] = "El nombre del cedente es obligatorio."
        elif _no_cumple_formato(form, "nombre_cedente", REGEX_NOMBRES):
            errores["nombre_cedente"] = "El nombre solo puede contener letras."
        elif _demasiado_largo(form, "nombre_cedente", 100):
            errores["nombre_cedente"] = "El nombre no puede superar los 100 caracteres."

        if _falta(form, "rfc_cedente"):
            errores["rfc_cedente"] = "El RFC del cedente es obligatorio."
        elif _no_cumple_formato(form, "rfc_cedente", REGEX_RFC):
            errores["rfc_cedente"] = "El RFC solo puede contener letras mayúsculas y números."
        elif len(form.get("rfc_cedente", "").strip()) not in (12, 13):
            errores["rfc_cedente"] = "El RFC debe tener 12 o 13 caracteres."

    elif tipo_cedente == "moral":
        if _falta(form, "razon_social_cedente"):
            errores["razon_social_cedente"] = "La razón social del cedente es obligatoria."
        elif _no_cumple_formato(form, "razon_social_cedente", REGEX_RAZON_SOCIAL):
            errores["razon_social_cedente"] = "La razón social tiene caracteres no permitidos."
        elif _demasiado_largo(form, "razon_social_cedente", 150):
            errores["razon_social_cedente"] = "La razón social no puede superar los 150 caracteres."

        if _falta(form, "representante_legal_cedente"):
            errores["representante_legal_cedente"] = "El representante legal del cedente es obligatorio."
        elif _no_cumple_formato(form, "representante_legal_cedente", REGEX_NOMBRES):
            errores["representante_legal_cedente"] = "El nombre solo puede contener letras."
        elif _demasiado_largo(form, "representante_legal_cedente", 100):
            errores["representante_legal_cedente"] = "El nombre no puede superar los 100 caracteres."

        if _falta(form, "rfc_cedente"):
            errores["rfc_cedente"] = "El RFC del cedente es obligatorio."
        elif _no_cumple_formato(form, "rfc_cedente", REGEX_RFC):
            errores["rfc_cedente"] = "El RFC solo puede contener letras mayúsculas y números."
        elif len(form.get("rfc_cedente", "").strip()) not in (12, 13):
            errores["rfc_cedente"] = "El RFC debe tener 12 o 13 caracteres."

    # --- Tipo de Cesionario ---
    tipo_cesionario = form.get("tipo_cesionario")
    if tipo_cesionario not in ("fisica", "moral"):
        errores["tipo_cesionario"] = "Selecciona el tipo de persona del cesionario."
        tipo_cesionario = None

    if tipo_cesionario == "fisica":
        if _falta(form, "nombre_cesionario"):
            errores["nombre_cesionario"] = "El nombre del cesionario es obligatorio."
        elif _no_cumple_formato(form, "nombre_cesionario", REGEX_NOMBRES):
            errores["nombre_cesionario"] = "El nombre solo puede contener letras."
        elif _demasiado_largo(form, "nombre_cesionario", 100):
            errores["nombre_cesionario"] = "El nombre no puede superar los 100 caracteres."

        if _falta(form, "rfc_cesionario"):
            errores["rfc_cesionario"] = "El RFC del cesionario es obligatorio."
        elif _no_cumple_formato(form, "rfc_cesionario", REGEX_RFC):
            errores["rfc_cesionario"] = "El RFC solo puede contener letras mayúsculas y números."
        elif len(form.get("rfc_cesionario", "").strip()) not in (12, 13):
            errores["rfc_cesionario"] = "El RFC debe tener 12 o 13 caracteres."

    elif tipo_cesionario == "moral":
        if _falta(form, "razon_social_cesionario"):
            errores["razon_social_cesionario"] = "La razón social del cesionario es obligatoria."
        elif _no_cumple_formato(form, "razon_social_cesionario", REGEX_RAZON_SOCIAL):
            errores["razon_social_cesionario"] = "La razón social tiene caracteres no permitidos."
        elif _demasiado_largo(form, "razon_social_cesionario", 150):
            errores["razon_social_cesionario"] = "La razón social no puede superar los 150 caracteres."

        if _falta(form, "representante_legal_cesionario"):
            errores["representante_legal_cesionario"] = "El representante legal del cesionario es obligatorio."
        elif _no_cumple_formato(form, "representante_legal_cesionario", REGEX_NOMBRES):
            errores["representante_legal_cesionario"] = "El nombre solo puede contener letras."
        elif _demasiado_largo(form, "representante_legal_cesionario", 100):
            errores["representante_legal_cesionario"] = "El nombre no puede superar los 100 caracteres."

        if _falta(form, "rfc_cesionario"):
            errores["rfc_cesionario"] = "El RFC del cesionario es obligatorio."
        elif _no_cumple_formato(form, "rfc_cesionario", REGEX_RFC):
            errores["rfc_cesionario"] = "El RFC solo puede contener letras mayúsculas y números."
        elif len(form.get("rfc_cesionario", "").strip()) not in (12, 13):
            errores["rfc_cesionario"] = "El RFC debe tener 12 o 13 caracteres."

    # --- Marca ---
    if _falta(form, "marca"):
        errores["marca"] = "La marca es obligatoria."
    elif _demasiado_largo(form, "marca", 100):
        errores["marca"] = "La marca no puede superar los 100 caracteres."

    # --- Datos Bancarios (del cesionario) ---
    if _falta(form, "banco"):
        errores["banco"] = "El banco es obligatorio."
    elif _no_cumple_formato(form, "banco", REGEX_NOMBRES):
        errores["banco"] = "El banco solo puede contener letras."
    elif _demasiado_largo(form, "banco", 100):
        errores["banco"] = "El nombre del banco no puede superar los 100 caracteres."

    if _falta(form, "n_cuenta"):
        errores["n_cuenta"] = "El número de cuenta es obligatorio."
    elif _demasiado_largo(form, "n_cuenta", 30):
        errores["n_cuenta"] = "El número de cuenta no puede superar los 30 caracteres."

    if _falta(form, "n_clabe"):
        errores["n_clabe"] = "La CLABE interbancaria es obligatoria."
    elif len(form.get("n_clabe", "").strip()) != 18 or not form.get("n_clabe", "").strip().isdigit():
        errores["n_clabe"] = "La CLABE debe contener exactamente 18 dígitos numéricos."

    return errores