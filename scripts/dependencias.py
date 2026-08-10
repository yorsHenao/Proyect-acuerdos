def resolver_dependencias(activas):
    bono_o_fondo_activo = any([
        activas["activa_bono_crecimiento"],
        activas["activa_bono_mercadotecnia"],
        activas["activa_bono_nuevas_aperturas"],
        activas["activa_bono_nuevas_aperturas_previo"],
        activas["activa_fondo_mercadotecnia"],
        activas["activa_fondo_mercadotecnia_ooh"],
        activas["activa_linea_nuevas_aperturas"],
    ])

    exclusividad_o_semi_activa = activas["activa_exclusividad"] or activas["activa_semi_exclusividad"]

    # 1. Validación de dependencia
    if bono_o_fondo_activo and not exclusividad_o_semi_activa:
        raise ValueError(
            "Hay Bonos o Fondos activos, pero no se seleccionó Exclusividad ni Semi exclusividad."
        )

    if activas["activa_exclusividad"] and activas["activa_semi_exclusividad"]:
        raise ValueError("Exclusividad y Semi exclusividad son mutuamente excluyentes.")

    # 2. Cálculo de Incumplimiento
    if bono_o_fondo_activo:
        activas["activa_incumplimiento_bono_fondo"] = True
        activas["activa_incumplimiento_exclusividad"] = False
    elif exclusividad_o_semi_activa:
        activas["activa_incumplimiento_bono_fondo"] = False
        activas["activa_incumplimiento_exclusividad"] = True
    else:
        activas["activa_incumplimiento_bono_fondo"] = False
        activas["activa_incumplimiento_exclusividad"] = False