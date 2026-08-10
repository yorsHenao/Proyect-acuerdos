from scripts.numero_a_letras import numero_a_letras

def solicitar_ads(activas, contexto):
    activas["activa_ads"] = True
    porcentaje = int(input("Ingresa porcentaje de ADS (solo números): "))
    contexto["N_ADS"] = porcentaje
    contexto["VALOR_ADS"] = numero_a_letras(porcentaje)


def procesar_ads (activas, porcentaje, contexto):
    activas["activa_ads"] = True
    contexto["N_ADS"] = porcentaje
    contexto["VALOR_ADS"] = numero_a_letras(porcentaje)



if __name__ == "__main__":
    activas = {
        "activa_ads": False
    }
    contexto = {}
    solicitar_ads(activas, contexto)
    print("Actividades:", activas)
    print("Contexto:", contexto)