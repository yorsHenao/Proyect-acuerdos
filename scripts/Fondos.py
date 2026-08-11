from scripts.numero_a_letras import numero_a_letras
from scripts.formatear_monto import formatear_monto


def procesar_fondo_mercadotecnia(aplica, monto, activas, contexto):
    if not aplica:
        activas["activa_fondo_mercadotecnia"] = False
        return
    activas["activa_fondo_mercadotecnia"] = True
    contexto["N_FONDO_MERCADOTECNIA"] = formatear_monto(monto)
    contexto["N_FONDO_MERCADOTECNIA_NUMERO"] = monto
    contexto["VALOR_FONDO_MERCADOTECNIA"] = numero_a_letras(monto)


def procesar_fondo_mercadotecnia_ooh(aplica, monto, activas, contexto):
    if not aplica:
        activas["activa_fondo_mercadotecnia_ooh"] = False
        return
    activas["activa_fondo_mercadotecnia_ooh"] = True
    contexto["N_FONDO_MERCADOTECNIA_OOH"] = formatear_monto(monto)
    contexto["N_FONDO_MERCADOTECNIA_OOH_NUMERO"] = monto
    contexto["VALOR_FONDO_MERCADOTECNIA_OOH"] = numero_a_letras(monto)


def procesar_linea_nuevas_aperturas(aplica, monto, activas, contexto):
    if not aplica:
        activas["activa_linea_nuevas_aperturas"] = False
        return
    activas["activa_linea_nuevas_aperturas"] = True
    contexto["N_NUEVAS_APERTURAS"] = formatear_monto(monto)
    contexto["N_NUEVAS_APERTURAS_NUMERO"] = monto
    contexto["VALOR_NUEVAS_APERTURAS"] = numero_a_letras(monto)
