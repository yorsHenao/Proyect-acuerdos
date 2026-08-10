from scripts.numero_a_letras import numero_a_letras

#funcion para terminal
def generar_descuento_menu(activas, contexto):
    respuesta = input("¿Aplica Descuento en Menú? (si/no): ").strip().lower()
    if respuesta != "si":
        activas["activa_descuento_menu"] = False
        return
    activas["activa_descuento_menu"] = True
    contexto["N_DESCUENTO_MENU"] = int(input("Porcentaje de descuento (número): "))
    contexto["VALOR_DESCUENTO_MENU"] = numero_a_letras(contexto["N_DESCUENTO_MENU"])
    contexto["N_MESES_DESCUENTO_MENU"] = int(input("Cantidad de meses (número): "))
    contexto["VALOR_MES_DESCUENTO_MENU"] = numero_a_letras(contexto["N_MESES_DESCUENTO_MENU"])


#funcion para flask
def procesar_descuento_menu(aplica, porcentaje, meses, activas, contexto):
    if not aplica:
        activas["activa_descuento_menu"] = False
        return
    activas["activa_descuento_menu"] = True
    contexto["N_DESCUENTO_MENU"] = porcentaje
    contexto["VALOR_DESCUENTO_MENU"] = numero_a_letras(porcentaje)
    contexto["N_MESES_DESCUENTO_MENU"] = meses
    contexto["VALOR_MES_DESCUENTO_MENU"] = numero_a_letras(meses)


#funcion para terminal
def generar_mark_down(activas, contexto):
    respuesta = input("¿Aplica Mark Down? (si/no): ").strip().lower()
    if respuesta != "si":
        activas["activa_mark_down"] = False
        return
    activas["activa_mark_down"] = True
    contexto["N_DESCUENTO_MARK_DOWN"] = int(input("Porcentaje de inversión (número): "))
    contexto["VALOR_DESCUENTO_MARK_DOWN"] = numero_a_letras(contexto["N_DESCUENTO_MARK_DOWN"])

#funcion para flask
def procesar_mark_down(aplica, porcentaje, activas, contexto):
    if not aplica:
        activas["activa_mark_down"] = False
        return
    activas["activa_mark_down"] = True
    contexto["N_DESCUENTO_MARK_DOWN"] = porcentaje
    contexto["VALOR_DESCUENTO_MARK_DOWN"] = numero_a_letras(porcentaje)


#funcion para terminal
def generar_publicaciones_redes(activas, contexto):
    respuesta = input("¿Aplica Publicaciones en Redes? (si/no): ").strip().lower()
    if respuesta != "si":
        activas["activa_publicaciones_redes"] = False
        return
    activas["activa_publicaciones_redes"] = True
    contexto["N_DESCUENTO_REDES"] = int(input("Cantidad de publicaciones (número): "))
    contexto["DESCUENTO_REDES"] = numero_a_letras(contexto["N_DESCUENTO_REDES"])


#funcion para flask
def procesar_publicaciones_redes(aplica, cantidad, activas, contexto):
    if not aplica:
        activas["activa_publicaciones_redes"] = False
        return
    activas["activa_publicaciones_redes"] = True
    contexto["N_DESCUENTO_REDES"] = cantidad
    contexto["DESCUENTO_REDES"] = numero_a_letras(cantidad)


#funcion para terminal
def generar_platillos_top_seller(activas, contexto):
    respuesta = input("¿Aplica Platillos Top Seller? (si/no): ").strip().lower()
    if respuesta != "si":
        activas["activa_platillos_top_seller"] = False
        return
    activas["activa_platillos_top_seller"] = True
    contexto["N_CANTIDAD_PLATILLOS"] = int(input("Cantidad de platillos: "))
    contexto["N_DESCUENTO_PLATILLOS"] = int(input("Porcentaje de descuento (número): "))
    contexto["VALOR_DESCUENTO_PLATILLOS"] = numero_a_letras(contexto["N_DESCUENTO_PLATILLOS"])
    contexto["N_MESES_DESCUENTO_PLATILLOS"] = int(input("Cantidad de meses (número): "))
    contexto["VALOR_MES_DESCUENTO_PLATILLOS"] = numero_a_letras(contexto["N_MESES_DESCUENTO_PLATILLOS"])

#funcion para flask
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

#funcion para terminal
def generar_compromisos_adicionales(activas, contexto):
    generar_descuento_menu(activas, contexto)
    generar_mark_down(activas, contexto)
    generar_publicaciones_redes(activas, contexto)
    generar_platillos_top_seller(activas, contexto)

    activas["activa_compromisos_adicionales"] = any([
        activas["activa_descuento_menu"],
        activas["activa_mark_down"],
        activas["activa_publicaciones_redes"],
        activas["activa_platillos_top_seller"],
    ])

#funcion para flask
def procesar_resumen_compromisos_adicionales(activas):
    activas["activa_compromisos_adicionales"] = any([
        activas["activa_descuento_menu"],
        activas["activa_mark_down"],
        activas["activa_publicaciones_redes"],
        activas["activa_platillos_top_seller"],
    ])






if __name__ == "__main__":
    activas = {
        "activa_descuento_menu": False,
        "activa_mark_down": False,
        "activa_publicaciones_redes": False,
        "activa_platillos_top_seller": False,
        "activa_compromisos_adicionales": False
    }
    contexto = {}
    generar_compromisos_adicionales(activas, contexto)
    print("Actividades:", activas)
    print("Contexto:", contexto)