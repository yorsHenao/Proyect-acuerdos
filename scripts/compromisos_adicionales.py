from scripts.numero_a_letras import numero_a_letras


def procesar_descuento_menu(aplica, porcentaje, meses, activas, contexto):
    if not aplica:
        activas["activa_descuento_menu"] = False
        return
    activas["activa_descuento_menu"] = True
    contexto["N_DESCUENTO_MENU"] = porcentaje
    contexto["VALOR_DESCUENTO_MENU"] = numero_a_letras(porcentaje)
    contexto["N_MESES_DESCUENTO_MENU"] = meses
    contexto["VALOR_MES_DESCUENTO_MENU"] = numero_a_letras(meses)


def procesar_mark_down(aplica, porcentaje, activas, contexto):
    if not aplica:
        activas["activa_mark_down"] = False
        return
    activas["activa_mark_down"] = True
    contexto["N_DESCUENTO_MARK_DOWN"] = porcentaje
    contexto["VALOR_DESCUENTO_MARK_DOWN"] = numero_a_letras(porcentaje)


def procesar_publicaciones_redes(aplica, cantidad, activas, contexto):
    if not aplica:
        activas["activa_publicaciones_redes"] = False
        return
    activas["activa_publicaciones_redes"] = True
    contexto["N_DESCUENTO_REDES"] = cantidad
    contexto["DESCUENTO_REDES"] = numero_a_letras(cantidad)


def procesar_platillos_top_seller(aplica, cantidad, porcentaje, meses, activas, contexto):
    if not aplica:
        activas["activa_platillos_top_seller"] = False
        return
    activas["activa_platillos_top_seller"] = True
    contexto["N_CANTIDAD_PLATILLOS"] = cantidad
    contexto["N_DESCUENTO_PLATILLOS"] = porcentaje
    contexto["VALOR_DESCUENTO_PLATILLOS"] = numero_a_letras(porcentaje)
    contexto["N_MESES_DESCUENTO_PLATILLOS"] = meses
    contexto["VALOR_MES_DESCUENTO_PLATILLOS"] = numero_a_letras(meses)


def procesar_resumen_compromisos_adicionales(activas):
    activas["activa_compromisos_adicionales"] = any([
        activas["activa_descuento_menu"],
        activas["activa_mark_down"],
        activas["activa_publicaciones_redes"],
        activas["activa_platillos_top_seller"],
    ])
