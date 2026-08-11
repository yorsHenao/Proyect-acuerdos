from scripts.numero_a_letras import numero_a_letras

ROMANOS = [
    "i", "ii", "iii", "iv", "v",
    "vi", "vii", "viii", "ix", "x",
    "xi", "xii", "xiii", "xiv", "xv"
]


def procesar_comision_fija(porcentaje, contexto):
    contexto["n_comision_fija"] = porcentaje
    contexto["valor_comision_fija"] = numero_a_letras(porcentaje)


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
