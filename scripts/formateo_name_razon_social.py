import re


def _capitalizar_respetando_abreviaturas(palabra: str) -> str:
    """
    Capitaliza una palabra pero respeta abreviaturas (letras seguidas de puntos).
    Ej: 'c.p' -> 'C.P', 's.a' -> 'S.A'
    """
    if '.' in palabra:
        return palabra.upper()
    return palabra.capitalize()


def formatear_razon_social(texto: str) -> str:
    if not texto:
        return ""

    # 1. Eliminar espacios dobles o innecesarios
    texto = " ".join(texto.strip().split())

    # 2. Capitalizar el nombre comercial (respetando conectores y abreviaturas)
    conectores = {"de", "del", "e", "y", "la", "las", "los", "en", "por", "con", "para"}
    palabras = texto.split(" ")
    palabras_formateadas = []

    for i, word in enumerate(palabras):
        word_lower = word.lower()
        if i > 0 and word_lower in conectores:
            if '.' in word:
                palabras_formateadas.append(word.upper())
            else:
                palabras_formateadas.append(word_lower)
        else:
            palabras_formateadas.append(_capitalizar_respetando_abreviaturas(word))

    resultado = " ".join(palabras_formateadas)

    # 3. Sustituir y estandarizar regímenes societarios con la sintaxis exacta,
    #    sin importar como los haya escrito el usuario (con o sin puntos,
    #    con o sin espacios entre letras, mayúsculas o minúsculas).
    #    SEP tolera: punto opcional + espacios opcionales entre cada letra.
    SEP = r'\.?\s*'
    regimenes = [
        # S. de R.L. de C.V.
        (rf'\bS{SEP}(?:de|DE|De){SEP}R{SEP}L{SEP}(?:de|DE|De){SEP}C{SEP}V\.?(?![A-Za-z])',
         'S. DE R.L. DE C.V.'),
        # S.A.P.I de C.V.
        (rf'\bS{SEP}A{SEP}P{SEP}I{SEP}(?:de|DE|De){SEP}C{SEP}V\.?(?![A-Za-z])',
         'S.A.P.I DE C.V.'),
        # S.A.B de C.V.
        (rf'\bS{SEP}A{SEP}B{SEP}(?:de|DE|De){SEP}C{SEP}V\.?(?![A-Za-z])',
         'S.A.B DE C.V.'),
        # S.A de C.V.
        (rf'\bS{SEP}A{SEP}(?:de|DE|De){SEP}C{SEP}V\.?(?![A-Za-z])',
         'S.A DE C.V.'),
        # S.A.S.
        (rf'\bS{SEP}A{SEP}S\.?(?![A-Za-z])',
         'S.A.S.'),
        # S. de R.L.
        (rf'\bS{SEP}(?:de|DE|De){SEP}R{SEP}L\.?(?![A-Za-z])',
         'S. DE R.L.'),
    ]

    for patron, reemplazo in regimenes:
        resultado = re.sub(patron, reemplazo, resultado, flags=re.IGNORECASE)

    return resultado


def formatear_direccion(texto: str) -> str:
    """
    Formatea una dirección respetando abreviaturas conocidas (Col., Av., No.,
    C.P, Apto., Dep., Blvd., Fracc., Int., Ext.), sin importar como el
    usuario las haya escrito (mayúsculas, minúsculas, con o sin puntos).
    Las palabras normales que solo tienen un punto por ser fin de frase
    (ej. 'Cuautemoc.') ya NO se convierten en mayúsculas completas.
    """
    if not texto:
        return ""

    # 1. Eliminar espacios dobles o innecesarios
    texto = " ".join(texto.strip().split())

    # 2. Abreviaturas conocidas -> como deben quedar escritas
    abreviaturas_conocidas = {
        "cp": "C.P",
        "no": "No.",
        "num": "No.",
        "av": "Av.",
        "col": "Col.",
        "apto": "Apto.",
        "dep": "Dep.",
        "depto": "Dep.",
        "blvd": "Blvd.",
        "fracc": "Fracc.",
        "mza": "Mza.",
        "int": "Int.",
        "ext": "Ext.",
    }

    segmentos = texto.split(",")
    segmentos_procesados = []

    for segmento in segmentos:
        palabras = segmento.strip().split(" ")
        palabras_formateadas = []

        for word in palabras:
            if not word:
                continue

            # separar el punto final de la palabra para analizarla limpia
            core = word.rstrip(".")
            trailing = word[len(core):]  # "" o "." o ".."
            core_sin_puntos = core.replace(".", "")

            if any(ch.isdigit() for ch in core_sin_puntos):
                # números o números+letra (128, 3B, etc.): se dejan tal cual
                palabras_formateadas.append(word)
                continue

            key = core_sin_puntos.lower()
            if key in abreviaturas_conocidas:
                palabras_formateadas.append(abreviaturas_conocidas[key])
            else:
                # palabra normal: capitalizar solo la primera letra,
                # conservando el punto final si lo tenía (fin de frase)
                palabras_formateadas.append(core.capitalize() + trailing)

        segmentos_procesados.append(" ".join(palabras_formateadas))

    resultado = ", ".join(segmentos_procesados)
    return resultado