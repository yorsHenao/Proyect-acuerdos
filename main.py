from pathlib import Path
from scripts.generar_acuerdo import generar_acuerdo

BASE_DIR = Path(__file__).resolve().parent

PERSONA_FISICA = "fisica"
PERSONA_JURIDICA = "juridica"

PLANTILLAS = {
    (PERSONA_FISICA, False):   "acuerdo_sin_ads_persona_fisica.docx",
    (PERSONA_FISICA, True):    "acuerdo_con_ads_persona_fisica.docx",
    (PERSONA_JURIDICA, False): "acuerdo_sin_ads_juridica.docx",
    (PERSONA_JURIDICA, True):  "acuerdo_con_ads_juridica.docx",
}

if __name__ == "__main__":
    print("\n--- Generador de Acuerdos de Cooperación ---\n")
    print("¿Para quién es el acuerdo?\n")
    print("1. Persona física")
    print("2. Persona jurídica\n")
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        tipo_persona = PERSONA_FISICA
    elif opcion == "2":
        tipo_persona = PERSONA_JURIDICA
    else:
        raise ValueError("Opción no válida, debe ser 1 o 2")

    respuesta_ads = input("¿Requiere ADS? (si/no): ").strip().lower()
    if respuesta_ads == "si":
        tiene_ads = True
    elif respuesta_ads == "no":
        tiene_ads = False
    else:
        raise ValueError("Opción no válida, debe ser 'si' o 'no'")

    plantilla = BASE_DIR / "formatos" /PLANTILLAS[(tipo_persona, tiene_ads)]

    generar_acuerdo(tipo_persona, tiene_ads, plantilla)