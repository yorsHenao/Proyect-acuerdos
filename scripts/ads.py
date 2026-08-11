from scripts.numero_a_letras import numero_a_letras


def procesar_ads(activas, porcentaje, contexto):
    activas["activa_ads"] = True
    contexto["N_ADS"] = porcentaje
    contexto["VALOR_ADS"] = numero_a_letras(porcentaje)
