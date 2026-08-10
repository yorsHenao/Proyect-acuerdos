from num2words import num2words


def numero_a_letras(n: int) -> str:
    if n < 0:
        raise ValueError("El número debe ser positivo")

    return num2words(n, lang="es")
