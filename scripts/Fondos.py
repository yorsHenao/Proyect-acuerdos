from scripts.numero_a_letras import numero_a_letras
from scripts.formatear_monto import formatear_monto

#funcion para terminal
def generar_fondo_mercadotecnia(activas, contexto):
    respuesta = input("¿Aplica Fondo de Mercadotecnia? (si/no): ").strip().lower()
    if respuesta != "si":
        return
    activas["activa_fondo_mercadotecnia"] = True
    monto = int(input("Ingresa monto del fondo de mercadotecnia (Solo numeros): "))
    contexto["N_FONDO_MERCADOTECNIA"] = formatear_monto(monto)
    contexto["N_FONDO_MERCADOTECNIA_NUMERO"] = monto
    contexto["VALOR_FONDO_MERCADOTECNIA"] = numero_a_letras(monto)

#fuincion para flask
def procesar_fondo_mercadotecnia(aplica, monto, activas, contexto):
    if not aplica:
        activas["activa_fondo_mercadotecnia"] = False
        return
    activas["activa_fondo_mercadotecnia"] = True
    contexto["N_FONDO_MERCADOTECNIA"] = formatear_monto(monto)
    contexto["N_FONDO_MERCADOTECNIA_NUMERO"] = monto
    contexto["VALOR_FONDO_MERCADOTECNIA"] = numero_a_letras(monto)


#funcion para terminal
def generar_fondo_mercadotecnia_ooh(activas, contexto):
    respuesta = input("¿Aplica Fondo de Mercadotecnia OOH? (si/no): ").strip().lower()
    if respuesta != "si":
        return
    activas["activa_fondo_mercadotecnia_ooh"] = True
    monto = int(input("Ingresa monto del fondo de mercadotecnia OOH (Solo numeros): "))
    contexto["N_FONDO_MERCADOTECNIA_OOH"] = formatear_monto(monto)
    contexto["N_FONDO_MERCADOTECNIA_OOH_NUMERO"] = monto
    contexto["VALOR_FONDO_MERCADOTECNIA_OOH"] = numero_a_letras(monto)


#funcion para flask
def procesar_fondo_mercadotecnia_ooh(aplica, monto, activas, contexto):
    if not aplica:
        activas["activa_fondo_mercadotecnia_ooh"] = False
        return
    activas["activa_fondo_mercadotecnia_ooh"] = True
    contexto["N_FONDO_MERCADOTECNIA_OOH"] = formatear_monto(monto)
    contexto["N_FONDO_MERCADOTECNIA_OOH_NUMERO"] = monto
    contexto["VALOR_FONDO_MERCADOTECNIA_OOH"] = numero_a_letras(monto)

#funcion para terminal
def generar_linea_nuevas_aperturas(activas, contexto):
    respuesta = input("¿Aplica Linea de Nuevas Aperturas? (si/no): ").strip().lower()
    if respuesta != "si":
        return
    activas["activa_linea_nuevas_aperturas"] = True
    monto = int(input("Ingresa monto de la linea de nuevas aperturas (Solo numeros): "))
    contexto["N_NUEVAS_APERTURAS"] = formatear_monto(monto)
    contexto["N_NUEVAS_APERTURAS_NUMERO"] = monto
    contexto["VALOR_NUEVAS_APERTURAS"] = numero_a_letras(monto)


#funcion para flask
def procesar_linea_nuevas_aperturas(aplica, monto, activas, contexto):
    if not aplica:
        activas["activa_linea_nuevas_aperturas"] = False
        return
    activas["activa_linea_nuevas_aperturas"] = True
    contexto["N_NUEVAS_APERTURAS"] = formatear_monto(monto)
    contexto["N_NUEVAS_APERTURAS_NUMERO"] = monto
    contexto["VALOR_NUEVAS_APERTURAS"] = numero_a_letras(monto)

if __name__ == "__main__":
    activas = {
        "activa_fondo_mercadotecnia": False,
        "activa_fondo_mercadotecnia_ooh": False,
        "activa_linea_nuevas_aperturas": False
    }
    contexto = {}
    generar_fondo_mercadotecnia(activas, contexto)
    generar_fondo_mercadotecnia_ooh(activas, contexto)
    generar_linea_nuevas_aperturas(activas, contexto)
    print("Actividades:", activas)
    print("Contexto:", contexto)