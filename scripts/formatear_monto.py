def formatear_monto(valor):
    """Miles con comas, sin decimales (las plantillas ya incluyen 00/100)."""
    return f"{int(valor):,}"
