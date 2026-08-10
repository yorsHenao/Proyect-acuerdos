import re

def _capitalizar_respetando_abreviaturas(palabra: str) -> str:
    """
    Capitaliza una palabra pero respeta abreviaturas (letras seguidas de puntos).
    Ej: 'c.p' -> 'C.P', 's.a' -> 'S.A'
    """
    # Si contiene puntos (es una abreviatura), convertir todo a mayúscula
    if '.' in palabra:
        return palabra.upper()
    # Si es una palabra normal, capitalizar primera letra
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
            # Los conectores se mantienen en minúscula, EXCEPTO si tienen puntos (abreviaturas)
            if '.' in word:
                palabras_formateadas.append(word.upper())
            else:
                palabras_formateadas.append(word_lower)
        else:
            palabras_formateadas.append(_capitalizar_respetando_abreviaturas(word))

    resultado = " ".join(palabras_formateadas)

    # 3. Sustituir y estandarizar regímenes con la sintaxis exacta
    regimenes = [
        # S. de R.L. de C.V.
        (r'\bS\.?\s+[D|d][E|e]\s+[R|r]\.?[L|l]\.?\s+[D|d][E|e]\s+[C|c]\.?[V|v]\.?\b', 'S. DE R.L. DE C.V.'),
        # S.A.P.I de C.V.
        (r'\bS\.?[A|a]\.?[P|p]\.?[I|i]\.?\s+[D|d][E|e]\s+[C|c]\.?[V|v]\.?\b', 'S.A.P.I DE C.V.'),
        # S.A.B de C.V.
        (r'\bS\.?[A|a]\.?[B|b]\.?\s+[D|d][E|e]\s+[C|c]\.?[V|v]\.?\b', 'S.A.B DE C.V.'),
        # S.A de C.V.
        (r'\bS\.?[A|a]\.?\s+[D|d][E|e]\s+[C|c]\.?[V|v]\.?\b', 'S.A DE C.V.'),
        # S.A.S.
        (r'\bS\.?[A|a]\.?[S|s]\.?\b', 'S.A.S.'),
        # S. de R.L.
        (r'\bS\.?\s+[D|d][E|e]\s+[R|r]\.?[L|l]\.?\b', 'S. DE R.L.'),
    ]

    for patron, reemplazo in regimenes:
        resultado = re.sub(patron, reemplazo, resultado, flags=re.IGNORECASE)

    return resultado


def formatear_direccion(texto: str) -> str:
    """
    Formatea una dirección respetando abreviaturas en mayúscula.
    Ej: 'Calle Cordoba 128, Col. Roma Norte, Cuautemoc. C.P 06500'
    -> 'Calle Cordoba 128, Col. Roma Norte, Cuautemoc. C.P 06500'
    """
    if not texto:
        return ""

    # 1. Eliminar espacios dobles o innecesarios
    texto = " ".join(texto.strip().split())

    # 2. Dividir por comas para procesar cada segmento
    segmentos = texto.split(",")
    segmentos_procesados = []

    for segmento in segmentos:
        # Procesar cada segmento respetando abreviaturas
        palabras = segmento.strip().split(" ")
        palabras_formateadas = []

        for word in palabras:
            # Si es un número o está completamente en mayúscula (códigos postales), mantener como está
            if word.isdigit() or word.isupper():
                palabras_formateadas.append(word)
            # Si contiene puntos (es una abreviatura), convertir a mayúscula
            elif '.' in word:
                palabras_formateadas.append(word.upper())
            # Si es una palabra normal, capitalizar solo la primera letra
            else:
                palabras_formateadas.append(word.capitalize())

        segmentos_procesados.append(" ".join(palabras_formateadas))

    resultado = ", ".join(segmentos_procesados)

    # 3. Asegurar que abreviaturas comunes en direcciones estén en mayúscula
    abreviaturas_direccion = {
        r'\bC\.P\b': 'C.P',
        r'\bC\.p\b': 'C.P',
        r'\bNo\.\b': 'No.',
        r'\bAv\.\b': 'Av.',
        r'\bCol\.\b': 'Col.',
        r'\bApto\.\b': 'Apto.',
        r'\bDep\.\b': 'Dep.',
    }

    for patron, reemplazo in abreviaturas_direccion.items():
        resultado = re.sub(patron, reemplazo, resultado, flags=re.IGNORECASE)

    return resultado