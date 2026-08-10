from scripts.numero_a_letras import numero_a_letras

ROMANOS = [
    "i", "ii", "iii", "iv", "v",
    "vi", "vii", "viii", "ix", "x",
    "xi", "xii", "xiii", "xiv", "xv"
]

#funcion para terminal
def solicitar_comision_fija(contexto):
    porcentaje = int(input("Ingresa el porcentaje de comisión fija (ej. 18): "))
    
    # Se asignan directamente las dos variables al contexto
    contexto["n_comision_fija"] = porcentaje
    contexto["valor_comision_fija"] = numero_a_letras(porcentaje)


#funcion para flask
def procesar_comision_fija(porcentaje, contexto):
    contexto["n_comision_fija"] = porcentaje
    contexto["valor_comision_fija"] = numero_a_letras(porcentaje)


#funcion para terminal
def solicitar_comision_por_mes(contexto):
    lineas = []
    mes_inicio = 1
    indice = 0

    while True:
        print(f"\n-> Escalón actual: inicia en el Mes {mes_inicio}")

        es_ultimo = input("¿Es el ÚLTIMO escalón? (si/no): ").strip().lower()
        porcentaje = int(input("Ingresa el porcentaje de comisión (ej. 18): "))
        
        # Uso de la función importada para convertir el porcentaje a texto
        porcentaje_texto = f"{porcentaje}% ({numero_a_letras(porcentaje)} por ciento) más IVA"

        if es_ultimo == "si":
            periodo = f"A partir del mes {mes_inicio} en adelante"
            lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")
            break

        mes_fin = int(input(f"¿Hasta qué mes llega este escalón? (mayor o igual a {mes_inicio}): "))

        while mes_fin < mes_inicio:
            print("\nEl mes final no puede ser menor al mes inicial.")
            mes_fin = int(input(f"¿Hasta qué mes llega este escalón? (mayor o igual a {mes_inicio}): "))

        if mes_inicio == mes_fin:
            periodo = f"Mes {mes_inicio}"
        else:
            periodo = f"Mes {mes_inicio} al {mes_fin}"

        lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")

        indice += 1
        mes_inicio = mes_fin + 1

    contexto["comision_escalonada"] = "\n".join(lineas)

#funcion para flask
def procesar_comision_por_mes(tramos, contexto):
    lineas = []
    mes_inicio = 1

    for indice, tramo in enumerate(tramos):
        porcentaje = tramo["porcentaje"]
        porcentaje_texto = f"{porcentaje}% ({numero_a_letras(porcentaje)} por ciento) más IVA"

        if tramo["es_ultimo"]:
            periodo = f"A partir del mes {mes_inicio} en adelante"
            lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")
            break

        mes_fin = tramo["mes_fin"]

        if mes_fin < mes_inicio:
            raise ValueError(f"El mes final ({mes_fin}) no puede ser menor al mes inicial ({mes_inicio}) en el escalón {indice + 1}.")

        periodo = f"Mes {mes_inicio}" if mes_inicio == mes_fin else f"Mes {mes_inicio} al {mes_fin}"
        lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")

        mes_inicio = mes_fin + 1

    contexto["comision_escalonada"] = "\n".join(lineas)

#funcion para terminal
def solicitar_comision_por_ordenes(contexto):
    lineas = []
    orden_inicio = 1
    indice = 0

    while True:
        print(f"\n-> Escalón actual: inicia en {orden_inicio} órdenes")

        es_ultimo = input("¿Es el ÚLTIMO escalón? (si/no): ").strip().lower()
        porcentaje = int(input("Ingresa el porcentaje de comisión (ej. 18): "))
        porcentaje_texto = f"{porcentaje}% ({numero_a_letras(porcentaje)} por ciento) más IVA"

        if es_ultimo == "si":
            periodo = f"A partir de {orden_inicio} órdenes en adelante"
            lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")
            break

        orden_fin = int(input(f"¿Hasta cuántas órdenes llega este escalón? (mayor o igual a {orden_inicio}): "))

        while orden_fin < orden_inicio:
            print("\nEl número final de órdenes no puede ser menor al inicial.")
            orden_fin = int(input(f"¿Hasta cuántas órdenes llega este escalón?: "))

        if orden_inicio == orden_fin:
            periodo = f"{orden_inicio} órdenes"
        else:
            periodo = f"De {orden_inicio} a {orden_fin} órdenes"

        lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")

        indice += 1
        orden_inicio = orden_fin + 1

    contexto["comision_escalonada_ordenes"] = "\n".join(lineas)

#funcion para flask
def procesar_comision_por_ordenes(tramos, contexto):
    lineas = []
    orden_inicio = 1

    for indice, tramo in enumerate(tramos):
        porcentaje = tramo["porcentaje"]
        porcentaje_texto = f"{porcentaje}% ({numero_a_letras(porcentaje)} por ciento) más IVA"

        if tramo["es_ultimo"]:
            periodo = f"A partir de {orden_inicio} órdenes en adelante"
            lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")
            break

        orden_fin = tramo["orden_fin"]

        if orden_fin < orden_inicio:
            raise ValueError(f"El número final de órdenes ({orden_fin}) no puede ser menor al inicial ({orden_inicio}) en el escalón {indice + 1}.")

        periodo = f"{orden_inicio} órdenes" if orden_inicio == orden_fin else f"De {orden_inicio} a {orden_fin} órdenes"
        lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")

        orden_inicio = orden_fin + 1

    contexto["comision_escalonada_ordenes"] = "\n".join(lineas)

#funcion para terminal
def solicitar_comision_por_ventas(contexto):
    lineas = []
    monto_inicio = 0.0
    indice = 0

    while True:
        print(f"\n-> Escalón actual: inicia en ${monto_inicio:,.2f} en ventas")

        es_ultimo = input("¿Es el ÚLTIMO escalón? (si/no): ").strip().lower()
        porcentaje = int(input("Ingresa el porcentaje de comisión (ej. 18): "))
        porcentaje_texto = f"{porcentaje}% ({numero_a_letras(porcentaje)} por ciento) más IVA"

        if es_ultimo == "si":
            periodo = f"A partir de ${monto_inicio:,.2f} en ventas en adelante"
            lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")
            break

        monto_fin = float(input(f"¿Hasta qué monto de ventas llega este escalón?: "))

        while monto_fin <= monto_inicio:
            print("\nEl monto final debe ser mayor al monto inicial.")
            monto_fin = float(input(f"¿Hasta qué monto de ventas llega este escalón?: "))

        periodo = f"De ${monto_inicio:,.2f} a ${monto_fin:,.2f} en ventas"
        lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")

        indice += 1
        monto_inicio = monto_fin + 0.01

    contexto["comision_escalonada_ventas"] = "\n".join(lineas)

#funcion para flask
def procesar_comision_por_ventas(tramos, contexto):
    lineas = []
    monto_inicio = 0.0

    for indice, tramo in enumerate(tramos):
        porcentaje = tramo["porcentaje"]
        porcentaje_texto = f"{porcentaje}% ({numero_a_letras(porcentaje)} por ciento) más IVA"

        if tramo["es_ultimo"]:
            periodo = f"A partir de ${monto_inicio:,.2f} en ventas en adelante"
            lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")
            break

        monto_fin = tramo["monto_fin"]

        if monto_fin <= monto_inicio:
            raise ValueError(f"El monto final (${monto_fin:,.2f}) debe ser mayor al monto inicial (${monto_inicio:,.2f}) en el escalón {indice + 1}.")

        periodo = f"De ${monto_inicio:,.2f} a ${monto_fin:,.2f} en ventas"
        lineas.append(f"{ROMANOS[indice]}) {periodo}: {porcentaje_texto}.")

        monto_inicio = monto_fin + 0.01

    contexto["comision_escalonada_ventas"] = "\n".join(lineas)



if __name__ == "__main__":
    contexto = {}
    print("Selecciona el tipo de comisión:")
    print("1) Comisión fija")
    print("2) Comisión por mes")
    print("3) Comisión por órdenes")
    print("4) Comisión por ventas")

    opcion = input("Ingresa el número de la opción deseada: ").strip()

    if opcion == "1":
        solicitar_comision_fija(contexto)
    elif opcion == "2":
        solicitar_comision_por_mes(contexto)
    elif opcion == "3":
        solicitar_comision_por_ordenes(contexto)
    elif opcion == "4":
        solicitar_comision_por_ventas(contexto)
    else:
        print("Opción no válida.")

    print("\nContexto generado:")
    for clave, valor in contexto.items():
        print(f"{clave}: {valor}")

