from scripts.numero_a_letras import numero_a_letras
from scripts.formatear_monto import formatear_monto

#Funcion para terminal
def solicitar_bono_crecimiento(activas, contexto):
    respuesta = input("¿Aplica Bono de Crecimiento? (si/no): ").strip().lower()
    if respuesta != "si":
        return
    activas["activa_bono_crecimiento"] = True
    monto = int(input("Ingresa monto del bono de crecimiento (Solo numeros): "))
    contexto["N_BONO_CRECIMIENTO"] = formatear_monto(monto)
    contexto["N_BONO_CRECIMIENTO_NUMERO"] = monto
    contexto["VALOR_BONO_CRECIMIENTO"] = numero_a_letras(monto)

#funcion para flask
def procesar_bono_crecimiento(aplica, monto, activas, contexto):
    if not aplica:
        return
    contexto["N_BONO_CRECIMIENTO"] = formatear_monto(monto)
    contexto["N_BONO_CRECIMIENTO_NUMERO"] = monto
    contexto["VALOR_BONO_CRECIMIENTO"] = numero_a_letras(monto)

#funcion para terminal
def solicitar_bono_mercadotecnia(activas, contexto):
    respuesta = input("¿Aplica Bono de Mercadotecnia? (si/no): ").strip().lower()
    if respuesta != "si":
        return
    activas["activa_bono_mercadotecnia"] = True
    monto = int(input("Ingresa monto del bono de mercadotecnia (Solo numeros): "))
    contexto["N_BONO_MERCADOTECNIA"] = formatear_monto(monto)
    contexto["N_BONO_MERCADOTECNIA_NUMERO"] = monto
    contexto["VALOR_BONO_MERCADOTECNIA"] = numero_a_letras(monto)

#funcion para flask
def procesar_bono_mercadotecnia(aplica, monto, activas, contexto):
    if not aplica:
        return
    contexto["N_BONO_MERCADOTECNIA"] = formatear_monto(monto)
    contexto["N_BONO_MERCADOTECNIA_NUMERO"] = monto
    contexto["VALOR_BONO_MERCADOTECNIA"] = numero_a_letras(monto)

#funcion para terminal
def solicitar_bono_nuevas_aperturas(activas, contexto):
    while True:
        respuesta = input("¿Aplica Bono de Nuevas Aperturas? (si/no): ").strip().lower()
        if respuesta != "si":
            return
        if activas["activa_bono_nuevas_aperturas_previo"]:
            print("No se puede activar el bono de nuevas aperturas si ya se activo el bono de nuevas aperturas previo. Intenta nuevamente.")
            continue

        activas["activa_bono_nuevas_aperturas"] = True
        monto = int(input("Ingresa monto del bono de nuevas aperturas (Solo numeros): "))
        contexto["N_BONO_NUEVAS_APERTURAS"] = formatear_monto(monto)
        contexto["N_BONO_NUEVAS_APERTURAS_NUMERO"] = monto
        contexto["VALOR_BONO_NUEVAS_APERTURAS"] = numero_a_letras(monto)

        num_establecimientos = int(input("Número de establecimientos: "))
        contexto["ESTABLECIMIENTOS"] = num_establecimientos
        contexto["NUM_ESTABLECIMIENTOS"] = numero_a_letras(num_establecimientos)


        meses = int(input("Meses para abrir los establecimientos: "))
        contexto["NUM_MESES"] = meses
        contexto["MESES"] = numero_a_letras(meses)

        maximo_bono = int(input("Apoyo máximo por establecimiento: "))
        contexto["MAXIMO_BONO"] = formatear_monto(maximo_bono)
        contexto["MAXIMO_BONO_NUMERO"] = maximo_bono
        contexto["VALOR_MAXIMO_BONO"] = numero_a_letras(maximo_bono)

        periodo_amortizacion = int(input("Periodo de amortización en meses: "))
        contexto["NUM_PERIODO_AMORTIZACIÓN"] = periodo_amortizacion
        contexto["PERIODO_AMORTIZACIÓN"] = numero_a_letras(periodo_amortizacion)
        return

#funcion par flask
def procesar_bono_nuevas_aperturas(monto, num_establecimientos, meses, maximo_bono, periodo_amortizacion, activas, contexto):
    activas["activa_bono_nuevas_aperturas"]=True

    contexto["N_BONO_NUEVAS_APERTURAS"] = formatear_monto(monto)
    contexto["N_BONO_NUEVAS_APERTURAS_NUMERO"] = monto
    contexto["VALOR_BONO_NUEVAS_APERTURAS"] = numero_a_letras(monto)

    contexto["ESTABLECIMIENTOS"] = num_establecimientos
    contexto["NUM_ESTABLECIMIENTOS"] = numero_a_letras(num_establecimientos)

    contexto["NUM_MESES"] = meses
    contexto["MESES"] = numero_a_letras(meses)

    contexto["MAXIMO_BONO"] = formatear_monto(maximo_bono)
    contexto["MAXIMO_BONO_NUMERO"] = maximo_bono
    contexto["VALOR_MAXIMO_BONO"] = numero_a_letras(maximo_bono)

    contexto["NUM_PERIODO_AMORTIZACIÓN"]= periodo_amortizacion
    contexto["PERIODO_AMORTIZACIÓN"] = numero_a_letras(periodo_amortizacion)

#funcion para terminal
def solicitar_bono_nuevas_aperturas_previo(monto,activas, contexto):
    while True:
        respuesta = input("¿Aplica Bono de Nuevas Aperturas Previo? (si/no): ").strip().lower()
        if respuesta != "si":
            return
        if activas["activa_bono_nuevas_aperturas"]:
            print("No se puede activar el bono de nuevas aperturas previo si ya se activo el bono de nuevas aperturas. Intenta nuevamente.")
            continue

        activas["activa_bono_nuevas_aperturas_previo"] = True
        monto = int(input("Ingresa monto del bono de nuevas aperturas previo (Solo numeros): "))
        contexto["N_BONO_NUEVAS_APERTURAS_PREVIO"] = formatear_monto(monto)
        contexto["N_BONO_NUEVAS_APERTURAS_PREVIO_NUMERO"] = monto
        contexto["VALOR_BONO_NUEVAS_APERTURAS_PREVIO"] = numero_a_letras(monto)

        num_establecimientos = int(input("Número de establecimientos: "))
        contexto["NUM_ESTABLECIMIENTOS"] = num_establecimientos
        contexto["ESTABLECIMIENTOS"] = numero_a_letras(num_establecimientos)

        meses = int(input("Meses para abrir los establecimientos: "))
        contexto["NUM_MESES"] = meses
        contexto["MESES"] = numero_a_letras(meses)

        maximo_bono = int(input("Apoyo máximo por establecimiento: "))
        contexto["MAXIMO_BONO"] = formatear_monto(maximo_bono)
        contexto["MAXIMO_BONO_NUMERO"] = maximo_bono
        contexto["VALOR_MAXIMO_BONO"] = numero_a_letras(maximo_bono)

        periodo_amortizacion = int(input("Periodo de amortización en meses: "))
        contexto["PERIODO_AMORTIZACION"] = periodo_amortizacion
        contexto["N_PERIODO_AMORTIZACION"] = numero_a_letras(periodo_amortizacion)
        return

#def para flask
def procesar_bono_nuevas_aperturas_previo(monto, num_establecimientos, meses, maximo_bono, periodo_amortizacion, activas, contexto):
    activas["activa_bono_nuevas_aperturas_previo"] = True
    contexto["N_BONO_NUEVAS_APERTURAS_PREVIO"] = formatear_monto(monto)
    contexto["N_BONO_NUEVAS_APERTURAS_PREVIO_NUMERO"] = monto
    contexto["VALOR_BONO_NUEVAS_APERTURAS_PREVIO"] = numero_a_letras(monto)

    contexto["NUM_ESTABLECIMIENTOS"] = num_establecimientos
    contexto["ESTABLECIMIENTOS"] = numero_a_letras(num_establecimientos)

    contexto["NUM_MESES"] = meses
    contexto["MESES"] = numero_a_letras(meses)

    contexto["MAXIMO_BONO"] = formatear_monto(maximo_bono)
    contexto["MAXIMO_BONO_NUMERO"] = maximo_bono
    contexto["VALOR_MAXIMO_BONO"] = numero_a_letras(maximo_bono)

    contexto["PERIODO_AMORTIZACION"] = periodo_amortizacion
    contexto["N_PERIODO_AMORTIZACION"] = numero_a_letras(periodo_amortizacion)



#funcion que sirve para procesar los bonos en terminales
def solicitar_bonos(activas, contexto):
    solicitar_bono_crecimiento(activas, contexto)
    solicitar_bono_mercadotecnia(activas, contexto)
    solicitar_bono_nuevas_aperturas(activas, contexto)
    solicitar_bono_nuevas_aperturas_previo(activas, contexto)


#funcion que sirve para procesar los bonos para flask
def procesar_bonos(monto, num_establecimientos, maximo_bono, periodo_amortizacion, meses, activas, contexto):
    procesar_bono_crecimiento(monto, activas, contexto)
    procesar_bono_mercadotecnia(monto, activas, contexto)
    procesar_bono_nuevas_aperturas(monto, num_establecimientos, meses, activas, contexto)
    procesar_bono_nuevas_aperturas_previo(monto, num_establecimientos, maximo_bono, periodo_amortizacion, meses, activas, contexto)




    
if __name__ == "__main__":
    activas = {
        "activa_bono_crecimiento": False,
        "activa_bono_mercadotecnia": False,
        "activa_bono_nuevas_aperturas": False,
        "activa_bono_nuevas_aperturas_previo": False
    }
    contexto = {}
    solicitar_bonos(activas, contexto)
    print("Actividades:", activas)
    print("Contexto:", contexto)