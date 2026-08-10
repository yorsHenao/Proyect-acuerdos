#def para terminal
def solicitar_exclusividad(activas, contexto):
    print("\n--- Exclusividad ---\n")
    print("1. Exclusividad")
    print("2. Semi-exclusividad")
    print("3. Ninguna")
    opcion = input("Selecciona una opción: ").strip() #strip es para quitar espacios en blanco al inicio y al final

    if opcion == "1":
        activas["activa_exclusividad"] = True
    elif opcion == "2":
        activas["activa_semi_exclusividad"] = True
    elif opcion == "3":
        pass # ninguna de las anteriores
    else:
        raise ValueError("Opcion no valida, debe ser 1, 2 o 3")
    
    if activas["activa_exclusividad"]:
        contexto["EXCLUSIVIDAD"] = "exclusividad"
    elif activas["activa_semi_exclusividad"]:
        contexto["EXCLUSIVIDAD"] = "semi-exclusividad"
    else:
        contexto["EXCLUSIVIDAD"] = None

#def para flask
def procesar_exclusividad(opcion, activas, contexto):
    if opcion == "1":
        activas["activa_exclusividad"] = True
    elif opcion == "2":
        activas["activa_semi_exclusividad"] = True
    elif opcion == "3":
        pass
    else:
        raise ValueError("Opcion no valida, debe ser 1, 2 o 3")

    if activas["activa_exclusividad"]:
        contexto["EXCLUSIVIDAD"] = "exclusividad"
    elif activas["activa_semi_exclusividad"]:
        contexto["EXCLUSIVIDAD"] = "semi-exclusividad"
    else:
        contexto["EXCLUSIVIDAD"] = None



if __name__ == "__main__":
    activas = {
        "activa_exclusividad": False,
        "activa_semi_exclusividad": False
    }
    contexto = {}
    solicitar_exclusividad(activas, contexto)
    print("Actividades:", activas)
    print("Contexto:", contexto)

