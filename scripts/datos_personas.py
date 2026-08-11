
def procesar_datos_persona_fisica(razon_social_persona_fisica, rfc_persona_fisica, direccion_persona_fisica, marca_persona_fisica, contexto):
    contexto["RAZÓN_SOCIAL"] = razon_social_persona_fisica
    contexto["RFC"] = rfc_persona_fisica
    contexto["DIRECCIÓN"] = direccion_persona_fisica
    contexto["MARCA"] = marca_persona_fisica


def procesar_datos_persona_juridica(razon_social_juridica, representante_legal, n_escritura, fecha_escritura, n_lic, numero_notario, ubicacion_notaria, n_folio, fecha_folio, n_rfc, direcion_razon_social, marca_persona_juridica, contexto):
    contexto["RAZÓN_SOCIAL"] = razon_social_juridica
    contexto["REPRESENTANTE_LEGAL"] = representante_legal
    contexto["N_ESCRITURA"] = n_escritura
    contexto["FECHA_ESCRITURA"] = fecha_escritura
    contexto["N_LIC"] = n_lic
    contexto["NUMERO_NOTARIO"] = numero_notario
    contexto["UBICACIÓN_NOTARIA"] = ubicacion_notaria
    contexto["N_FOLIO"] = n_folio
    contexto["FECHA_FOLIO"] = fecha_folio
    contexto["N_RFC"] = n_rfc
    contexto["DIC_RAZÓN_SOCIAL"] = direcion_razon_social
    contexto["MARCA"] = marca_persona_juridica
