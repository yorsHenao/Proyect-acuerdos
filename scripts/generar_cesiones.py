import re
import tempfile
from datetime import date
from pathlib import Path
from docxtpl import DocxTemplate

from scripts.formateo_name_razon_social import formatear_razon_social
from scripts.fechas import fecha

PERSONA_FISICA = "fisica"
PERSONA_MORAL = "moral"

PLANTILLAS_CESIONES = {
    (PERSONA_FISICA, PERSONA_FISICA): "cesion_fisica_a_fisica_mx.docx",
    (PERSONA_FISICA, PERSONA_MORAL):  "cesion_fisica_a_moral_mx.docx",
    (PERSONA_MORAL,  PERSONA_FISICA): "cesion_moral_a_fisica_mx.docx",
    (PERSONA_MORAL,  PERSONA_MORAL):  "cesion_moral_a_moral_mx.docx",
}


def _capitalizar_nombre(texto: str) -> str:
    """Capitaliza nombres de personas físicas o representantes respetando conectores comunes."""
    if not texto:
        return ""
    conectores = {"de", "del", "e", "y", "la", "las", "los", "en", "por", "con", "para"}
    palabras = texto.strip().split()
    resultado = []
    for i, p in enumerate(palabras):
        p_lower = p.lower()
        if i > 0 and p_lower in conectores:
            resultado.append(p_lower)
        else:
            resultado.append(p.capitalize())
    return " ".join(resultado)


def _limpiar_nombre_archivo(nombre: str) -> str:
    """Elimina caracteres prohibidos en nombres de archivo de Windows."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre).strip()


def generar_cesion(datos: dict, plantilla_path: Path, salida_path: Path = None) -> Path:
    """
    Genera el documento Word de Cesión de Derechos a partir de los datos validados
    y la plantilla seleccionada.
    """
    tipo_cedente = datos["tipo_cedente"]
    tipo_cesionario = datos["tipo_cesionario"]

    contexto = {}

    # --- Cedente ---
    if tipo_cedente == PERSONA_FISICA:
        nombre_cedente = _capitalizar_nombre(datos["nombre_cedente"])
        contexto["NOMBRE_CEDENTE"] = nombre_cedente
        contexto["CEDENTE_RFC"] = datos["rfc_cedente"].strip().upper()
        identificador_cedente = nombre_cedente
    else:
        rs_cedente = formatear_razon_social(datos["razon_social_cedente"])
        rl_cedente = _capitalizar_nombre(datos["representante_legal_cedente"])
        contexto["RS_CEDENTE"] = rs_cedente
        contexto["RS_CEDENTE_FIRMA"] = rs_cedente
        contexto["RL_CEDENTE"] = rl_cedente
        contexto["CEDENTE_RFC"] = datos["rfc_cedente"].strip().upper()
        identificador_cedente = rs_cedente

    # --- Cesionario ---
    if tipo_cesionario == PERSONA_FISICA:
        nombre_cesionario = _capitalizar_nombre(datos["nombre_cesionario"])
        contexto["NOMBRE_CESIONARIO"] = nombre_cesionario
        contexto["CESIONARIO_RFC"] = datos["rfc_cesionario"].strip().upper()
        identificador_cesionario = nombre_cesionario
    else:
        rs_cesionario = formatear_razon_social(datos["razon_social_cesionario"])
        rl_cesionario = _capitalizar_nombre(datos["representante_legal_cesionario"])
        contexto["RS_CESIONARIO"] = rs_cesionario
        contexto["RS_CESIONARIO_FIRMA"] = rs_cesionario
        contexto["RL_CESIONARIO"] = rl_cesionario
        contexto["CESIONARIO_RFC"] = datos["rfc_cesionario"].strip().upper()
        identificador_cesionario = rs_cesionario

    # --- Marca y Datos Bancarios ---
    contexto["MARCA"] = _capitalizar_nombre(datos["marca"])
    contexto["BANCO"] = _capitalizar_nombre(datos["banco"])
    contexto["NUMERO_CUENTA"] = str(datos["n_cuenta"]).strip()
    contexto["CLABE_INTERBANCARIA"] = str(datos["n_clabe"]).strip()

    # --- Fecha de generación ---
    contexto["FECHA"] = fecha(date.today())

    # --- Nombre y ruta de archivo de salida ---
    id_limpio = _limpiar_nombre_archivo(identificador_cesionario)
    nombre_archivo = f"{fecha(date.today())} Cesión de derechos. Rappi & {id_limpio}.docx"

    if salida_path is None:
        salida = Path(tempfile.gettempdir()) / _limpiar_nombre_archivo(nombre_archivo)
    else:
        salida = Path(salida_path)
        if salida.suffix != ".docx":
            salida = salida / nombre_archivo
        salida.parent.mkdir(parents=True, exist_ok=True)

    # --- Renderizado con docxtpl ---
    docx = DocxTemplate(str(plantilla_path))
    docx.render(contexto, autoescape=True)
    docx.save(str(salida))

    return salida