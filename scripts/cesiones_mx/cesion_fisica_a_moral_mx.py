from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"

def generar_cesion_fisica_a_moral():
    #ruta
    plantilla = Path("plantillas/mexico/cesion_fisica_a_moral_mx.docx")

#palabras a rellenar

    print(f"\n{"*"*10}Cesión Personas fisicas a moral{"*"*10}\n")

    #contrato antiguo o nuevo

    respuesta = input("¿Incluimos la clásula cuarta? (si/no): ").strip().lower()
    
    incluir_clausula = respuesta == "si"


    #clausula de pago

    nombre_clausula = input("Ingresa nombre de la cláusula (Forma de pago o Contraprestación): ").strip().lower()


    #cedente
    nombre_cedente = input("Ingrese nombre cedente: ")
    domicilio_cedente = input("Ingrese dirección cedente: ")
    correo_cedente = input("Ingrese correo cedente: ")

    #cesionario
    nombre_cesionario = input("Ingrese razón social cesionario: ")
    nombre_rl_cesionario = input("Ingrese nombre representante legal cesionario")
    rfc_cesionario = input("Ingrese RFC razón social cesionario: ")
    domicilio_cesionario = input("Ingrese dirección razón social cesionario: ")
    correo_cesionario = input("Ingrese correo  razón social cesionario: ")
    marca = input("Ingrese marca: ")

    #fecha acuerdo principal

    fecha_contrato = input("Ingrese fecha contrato principal: ")

    #datos bancarios

    numero_cuenta = input("Ingrese numero de cuenta: ")
    numero_clabe_interbancaria = input("Ingrese número clabe interbancaria: ")
    banco = input("Ingrese nombre del banco: ")

    #nombre del archivo

    nombre_archivo = f"Cesion de derechos. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("D:/salidas/mexico/")/ nombre_archivo

    contexto = {
        "NOMBRE_CEDENTE": nombre_cedente,
        "DOMICILIO_CEDENTE": domicilio_cedente,
        "CORREO_CEDENTE": correo_cedente,
        
        "RS_CESIONARIO": nombre_cesionario,
        "RL_CESIONARIO": nombre_rl_cesionario,
        "RFC_CESIONARIO": rfc_cesionario,
        "DOMICILIO_CESIONARIO": domicilio_cesionario,
        "CORREO_CESIONARIO": correo_cesionario,
        "MARCA": marca,
        "NOMBRE_CLAUSULA": nombre_clausula,
        "incluir_clausula_cuarta": incluir_clausula,


        "FECHA_ACUERDO_P":fecha_contrato,
        "NUMERO_CUENTA": numero_cuenta,
        "CLABE_INTERBANCARIA": numero_clabe_interbancaria,
        "BANCO": banco,
        "FECHA": fecha(date.today()),
    }

    #rellenar plantilla
    docx = DocxTemplate(plantilla)
    docx.render(contexto)
    docx.save(salida)

    print(f"Documento generado \n")
    print("*"*20)

if __name__ == "__main__":
    generar_cesion_fisica_a_moral()





