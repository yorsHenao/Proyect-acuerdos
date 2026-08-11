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
