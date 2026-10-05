from scripts.numero_a_letras import numero_a_letras


def procesar_ads(activas, porcentaje, tipo_ads, contexto, porcentaje_rappi=None):
    activas["activa_ads"] = True
    contexto["tipo_ads"] = tipo_ads
    contexto["N_ADS"] = porcentaje
    contexto["VALOR_ADS"] = numero_a_letras(porcentaje)
    if tipo_ads == "aliado_y_rappi":
        contexto["N_ADS_RAPPI"] = porcentaje_rappi
        contexto["VALOR_ADS_RAPPI"] = numero_a_letras(porcentaje_rappi)
