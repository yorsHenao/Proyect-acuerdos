from datetime import date


def fecha(d: date) -> str:
    """Convierte una fecha a formato largo en español: '1 de octubre de 2026'."""
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    ]
    return f"{d.day} de {meses[d.month - 1]} de {d.year}"
