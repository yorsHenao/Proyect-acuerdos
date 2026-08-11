def construir_lista_bonos_fondos(activas):
    """
    Arma el texto con los Bonos/Fondos realmente activos en el acuerdo,
    para usarse en la cláusula de Incumplimiento por Bono y Fondo.
    Ej: "Bono de Crecimiento, Fondo de Mercadotecnia y Línea de Crédito Nuevas Aperturas"
    """
    nombres = []

    if activas.get("activa_bono_crecimiento"):
        nombres.append("Bono de Crecimiento")

    if activas.get("activa_bono_mercadotecnia"):
        nombres.append("Bono de Mercadotecnia")

    if activas.get("activa_bono_nuevas_aperturas") or activas.get("activa_bono_nuevas_aperturas_previo"):
        nombres.append("Bono para Nuevas Aperturas")

    if activas.get("activa_fondo_mercadotecnia"):
        nombres.append("Fondo de Mercadotecnia")

    if activas.get("activa_fondo_mercadotecnia_ooh"):
        nombres.append("Fondo de Mercadotecnia OOH")

    if activas.get("activa_linea_nuevas_aperturas"):
        nombres.append("Línea de Crédito Nuevas Aperturas")

    if not nombres:
        return ""
    if len(nombres) == 1:
        return nombres[0]

    return ", ".join(nombres[:-1]) + " y " + nombres[-1]