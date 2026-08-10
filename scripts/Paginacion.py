
CATALOGO_CLAUSULAS = [
    # --- Cláusulas condicionales ---
    ("NUM_EXCLUSIVIDAD", "activa_exclusividad"),
    ("NUM_SEMI_EXCLUSIVIDAD", "activa_semi_exclusividad"),
    ("NUM_INVERSIÓN_ADS", "activa_ads"),
    ("NUM_BONO_CRECIMIENTO", "activa_bono_crecimiento"),
    ("NUM_BONO_MERCADOTECNIA", "activa_bono_mercadotecnia"),
    ("NUM_BONO_NUEVAS_APERTURAS_POSTERIOR", "activa_bono_nuevas_aperturas"),
    ("NUM_BONO_NUEVAS_APERTURAS_PREVIO", "activa_bono_nuevas_aperturas_previo"),
    ("NUM_FONDO_MERCADOTECNIA", "activa_fondo_mercadotecnia"),
    ("NUM_FONDO_MERCADOTECNIA_OOH", "activa_fondo_mercadotecnia_ooh"),
    ("NUM_LINEA_NUEVAS_APERTURAS", "activa_linea_nuevas_aperturas"),
    ("NUM_INCUMPLIMIENTO_BONO_Y_FONDO", "activa_incumplimiento_bono_fondo"),
    ("NUM_INCUMPLIMIENTO_EXCLUSIVIDAD_Y_SEMI", "activa_incumplimiento_exclusividad"),
    ("NUM_COMPROMISOS_ADICIONALES", "activa_compromisos_adicionales"),
    
    # --- Cláusulas de cola (siempre se incluyen) ---
    ("NUM_DECLARACIONES_Y_GARANTIAS", None),
    ("NUM_PROPIEDAD_INTELECTUAL", None),
    ("NUM_CONFIDENCIALIDAD", None),
    ("NUM_INDEPENDENCIA", None),
    ("NUM_CASO_FORTUITO", None),
    ("NUM_INDEMNIDAD", None),
    ("NUM_CUMPLIMIENTO", None),
    ("NUM_RESOLUCIÓN", None),
    ("NUM_PROTECCIÓN_DATOS_PERSONALES", None),
    ("NUM_DISPOSICIONES_GENERALES", None),
]

def numero_a_ordinal(numero): 
    """Convierte un número entero a su representación ordinal femenina en mayúsculas."""
    ordinales = {
        1: "PRIMERA", 2: "SEGUNDA", 3: "TERCERA", 4: "CUARTA", 5: "QUINTA",
        6: "SEXTA", 7: "SÉPTIMA", 8: "OCTAVA", 9: "NOVENA", 10: "DÉCIMA",
        11: "DÉCIMA PRIMERA", 12: "DÉCIMA SEGUNDA", 13: "DÉCIMA TERCERA",
        14: "DÉCIMA CUARTA", 15: "DÉCIMA QUINTA", 16: "DÉCIMA SEXTA",
        17: "DÉCIMA SÉPTIMA", 18: "DÉCIMA OCTAVA", 19: "DÉCIMA NOVENA",
        20: "VIGÉSIMA", 21: "VIGÉSIMA PRIMERA", 22: "VIGÉSIMA SEGUNDA",
        23: "VIGÉSIMA TERCERA", 24: "VIGÉSIMA CUARTA", 25: "VIGÉSIMA QUINTA",
        26: "VIGÉSIMA SEXTA", 27: "VIGÉSIMA SÉPTIMA", 28: "VIGÉSIMA OCTAVA",
        29: "VIGÉSIMA NOVENA", 30: "TRIGÉSIMA", 31: "TRIGÉSIMA PRIMERA",
        32: "TRIGÉSIMA SEGUNDA", 33: "TRIGÉSIMA TERCERA", 34: "TRIGÉSIMA CUARTA",
        35: "TRIGÉSIMA QUINTA"
    }
    return ordinales.get(numero, str(numero))

def asignar_numeracion_clausulas(activas, contexto):
    contador = 14  # Las cláusulas 1 a 13 son fijas en la plantilla
    
    for variable, flag in CATALOGO_CLAUSULAS:
        # Se procesa si es cláusula de cola (flag es None) o si está activa
        if flag is None or activas.get(flag, False):
            contexto[variable] = numero_a_ordinal(contador)
            contador += 1


if __name__ == "__main__":
    activas = {
        "activa_exclusividad": True,
        "activa_semi_exclusividad": False,
        "activa_bono_crecimiento": True,
        "activa_bono_mercadotecnia": False,
        "activa_bono_nuevas_aperturas": True,
        "activa_bono_nuevas_aperturas_previo": False,
        "activa_fondo_mercadotecnia": True,
        "activa_fondo_mercadotecnia_ooh": False,
        "activa_linea_nuevas_aperturas": True,
        "activa_compromisos_adicionales": True
    }
    contexto = {}
    asignar_numeracion_clausulas(activas, contexto)
    for variable, numero in contexto.items():
        print(f"{variable}: {numero}")

