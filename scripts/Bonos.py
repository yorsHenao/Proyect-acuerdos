from scripts.numero_a_letras import numero_a_letras
from scripts.formatear_monto import formatear_monto


def procesar_bono_crecimiento(aplica, monto, activas, contexto):
    if not aplica:
        return
    contexto["N_BONO_CRECIMIENTO"] = formatear_monto(monto)
    contexto["N_BONO_CRECIMIENTO_NUMERO"] = monto
    contexto["VALOR_BONO_CRECIMIENTO"] = numero_a_letras(monto)


def procesar_bono_mercadotecnia(aplica, monto, activas, contexto):
    if not aplica:
        return
    contexto["N_BONO_MERCADOTECNIA"] = formatear_monto(monto)
    contexto["N_BONO_MERCADOTECNIA_NUMERO"] = monto
    contexto["VALOR_BONO_MERCADOTECNIA"] = numero_a_letras(monto)


def procesar_bono_nuevas_aperturas(monto, num_establecimientos, meses, maximo_bono, periodo_amortizacion, activas, contexto):
    activas["activa_bono_nuevas_aperturas"] = True

    contexto["N_BONO_NUEVAS_APERTURAS"] = formatear_monto(monto)
    contexto["N_BONO_NUEVAS_APERTURAS_NUMERO"] = monto
    contexto["VALOR_BONO_NUEVAS_APERTURAS"] = numero_a_letras(monto)

    contexto["ESTABLECIMIENTOS"] = num_establecimientos
    contexto["NUM_ESTABLECIMIENTOS"] = numero_a_letras(num_establecimientos)

    contexto["NUM_MESES"] = meses
    contexto["MESES"] = numero_a_letras(meses)

    contexto["NUM_MAXIMO_BONO"] = maximo_bono
    contexto["VALOR_MAXIMO_BONO"] = numero_a_letras(maximo_bono)

    contexto["NUM_PERIODO_AMORTIZACIÓN"] = periodo_amortizacion
    contexto["PERIODO_AMORTIZACIÓN"] = numero_a_letras(periodo_amortizacion)


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
