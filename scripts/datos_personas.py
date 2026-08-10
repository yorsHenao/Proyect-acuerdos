
#funcion para terminal
def generar_datos_persona_fisica(contexto):
    contexto["RAZÓN_SOCIAL"] = input("Ingresa nombre razón social: ")
    contexto["RFC"] = input("Ingresa RFC: ")
    contexto["DIRECCIÓN"] = input("Ingresa dirección: ")
    contexto["MARCA"] = input("Ingresa marca: ")

#funcion para flask
def procesar_datos_persona_fisica(razon_social_persona_fisica, rfc_persona_fisica, direccion_persona_fisica, marca_persona_fisica, contexto):
    contexto["RAZÓN_SOCIAL"] = razon_social_persona_fisica
    contexto["RFC"] = rfc_persona_fisica
    contexto["DIRECCIÓN"] = direccion_persona_fisica
    contexto["MARCA"] = marca_persona_fisica


#funcion para terminal
def generar_datos_persona_juridica(contexto):
    contexto["RAZÓN_SOCIAL"] = input("Ingresa nombre razón social: ")
    contexto["REPRESENTANTE_LEGAL"] = input("Ingresa representante legal: ")
    #Datos acta constitutiva
    contexto["N_ESCRITURA"] = input("Ingresa número de escritura: ")
    contexto["FECHA_ESCRITURA"] = input("Ingresa fecha de escritura: ")
    contexto["N_LIC"] = input("ingresa nombre notario: ")
    contexto["NUMERO_NOTARIO"] = input("Ingresa número de notaría: ")
    contexto["UBICACIÓN_NOTARIA"] = input("Ingresa ubicación de la notaría: ")
    contexto["N_FOLIO"] = input("Ingresa número de folio mercantil: ")
    contexto["FECHA_FOLIO"] = input("Ingresa fecha de folio mercantil: ")
    
    contexto["N_RFC"] = input("Ingresa RFC: ")
    contexto["DIC_RAZÓN_SOCIAL"] = input("Ingresa direccion: ")
    contexto["MARCA"] = input("Ingresa marca: ")

def procesar_datos_persona_juridica(razon_social_juridica, representante_legal, n_escritura, fecha_escritura, n_lic, numero_notario, ubicacion_notaria, n_folio, fecha_folio, n_rfc, direcion_razon_social, marca_persona_juridica, contexto):
    contexto["RAZÓN_SOCIAL"] = razon_social_juridica
    contexto["REPRESENTANTE_LEGAL"] = representante_legal
    #Datos acta constitutiva
    contexto["N_ESCRITURA"] = n_escritura
    contexto["FECHA_ESCRITURA"] = fecha_escritura
    contexto["N_LIC"] = n_lic #nombre licenciado
    contexto["NUMERO_NOTARIO"] = numero_notario
    contexto["UBICACIÓN_NOTARIA"] = ubicacion_notaria
    contexto["N_FOLIO"] = n_folio
    contexto["FECHA_FOLIO"] = fecha_folio
    contexto["N_RFC"] = n_rfc
    contexto["DIC_RAZÓN_SOCIAL"] = direcion_razon_social
    contexto["MARCA"] = marca_persona_juridica


if __name__ == "__main__":
    contexto = {}
    generar_datos_persona_fisica(contexto)
    print("Datos persona física:", contexto)
    contexto.clear()
    generar_datos_persona_juridica(contexto)
    print("Datos persona jurídica:", contexto)

