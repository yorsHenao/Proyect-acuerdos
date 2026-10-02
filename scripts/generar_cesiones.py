from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

#rutas
plantilla = Path("plantillas/ejemplo.docx")

#Función para formato fecha
def fecha(d: date) -> str:
    meses = ["enero","febrero","marzo","abril","mayo","junio",
             "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


#palabras a rellenar

nombre = input("nombre ")
doc = input("nombre documento ")
ciudad = input("ciudad ")


#Nombre archivo
nombre_archivo = f"{nombre}.docx"
salida = Path("D:/salidas")/ nombre_archivo


#datos plantilla

contexto = {
    "NOMBRE": nombre,
    "DOC": doc,
    "CIUDAD": ciudad,
    "FECHA": fecha(date.today()),
}

#relleno de plantilla
docx = DocxTemplate(plantilla)
docx.render(contexto)
docx.save(salida)

print(f"Documento generado")