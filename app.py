from pathlib import Path
from flask import Flask, render_template, request, send_file, redirect, url_for, session
import os
import io
from dotenv import load_dotenv
from datetime import datetime
from scripts.generar_acuerdo import generar_acuerdo, fecha
from scripts.validaciones import validar_formulario

load_dotenv()


def fecha_larga(fecha_iso: str) -> str:
    """Convierte 'YYYY-MM-DD' (input type=date) a texto en español."""
    return fecha(datetime.strptime(fecha_iso, "%Y-%m-%d").date())


def entero_monto(valor: str) -> int:
    return int(valor.replace(".", ""))

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


app.secret_key = os.getenv("SECRET_KEY")
if not app.secret_key:
    raise ValueError("La variable de entorno SECRET_KEY es requerida")

@app.route("/")
def formulario():
    errores = session.pop("errores", {})
    form_data = session.pop("form_data", {})
    return render_template("formulario.html", errores=errores, form_data=form_data)

PERSONA_FISICA = "fisica"
PERSONA_JURIDICA = "juridica"

PLANTILLAS = {
    (PERSONA_FISICA, False):   "acuerdo_sin_ads_persona_fisica.docx",
    (PERSONA_FISICA, True):    "acuerdo_con_ads_persona_fisica.docx",
    (PERSONA_JURIDICA, False): "acuerdo_sin_ads_juridica.docx",
    (PERSONA_JURIDICA, True):  "acuerdo_con_ads_juridica.docx",
}


@app.route("/generar", methods=["POST"])
def generar():
    errores = validar_formulario(request.form)
    if errores:
        session["errores"] = errores
        # Convertir form data a diccionario normal para guardar en sesión
        session["form_data"] = dict(request.form)
        return redirect(url_for("formulario"))

    datos = {}



    #---tipo persona----

    datos["tipo_persona"] = request.form["tipo_persona"]

    if datos["tipo_persona"] == PERSONA_FISICA:
        datos["razon_social"] = request.form["razon_social_fisica"]
        datos["rfc"] = request.form["rfc_fisica"]
        datos["direccion"] = request.form["direccion_fisica"]
        datos["marca"] = request.form["marca_fisica"]

    else:
        datos["razon_social"] = request.form["razon_social_juridica"]
        datos["rfc"] = request.form["rfc_juridica"]
        datos["representante_legal"] = request.form["representante_legal_juridica"]
        datos["direccion"] = request.form["direccion_juridica"]
        datos["marca"] = request.form["marca_juridica"]
        datos["n_acta_constitutiva"] = request.form["n_acta_constitutiva"]
        datos["fecha_acta_constitutiva"] = fecha_larga(request.form["fecha_acta_constitutiva"])
        datos["notario"] = request.form["notario"]
        datos["numero_notaria"] = request.form["numero_notaria"]
        datos["ubicacion_notaria"] = request.form["ubicacion_notaria"]
        datos["n_folio"] = request.form["n_folio_mercantil"]
        datos["fecha_folio_mercantil"] = fecha_larga(request.form["fecha_folio_mercantil"])

    #---- vigencia ----
    datos["vigencia"] = int(request.form["vigencia_meses"])

    #--- ads ----
    datos["tiene_ads"] = "tiene_ads" in request.form
    if datos["tiene_ads"]:
        datos["n_ads"] = int(request.form["n_ads"])

    #--- comision ---
    datos["tipo_comision"] = request.form["tipo_comision"]

    if datos["tipo_comision"] == "escalonada":
        datos["tipo_comision"] = request.form["modalidad_escalonada"]

    if datos["tipo_comision"] == "fija":
        datos["n_comision_fija"] = int(request.form["n_comision_fija"])
    else:
        tramos = []
        indice = 0
        while f"escalon_{indice}_porcentaje" in request.form:
            tramo = {
                "porcentaje": int(request.form[f"escalon_{indice}_porcentaje"]),
                "es_ultimo": request.form.get(f"escalon_{indice}_es_ultimo") == "si",
            }
            if not tramo["es_ultimo"]:
                campo_fin = request.form[f"escalon_{indice}_fin"]
                if datos["tipo_comision"] == "ventas":
                    tramo["monto_fin"] = float(campo_fin)
                elif datos["tipo_comision"] == "ordenes":
                    tramo["orden_fin"] = int(campo_fin)
                else:
                    tramo["mes_fin"] = int(campo_fin)
            tramos.append(tramo)
            indice += 1
        datos["tramos_comision"] = tramos

        # --- exclusividad ---
    datos["exclusividad"] = request.form["exclusividad"]

    # --- bonos ---
    datos["aplica_bono_crecimiento"] = "activa_bono_crecimiento" in request.form
    if datos["aplica_bono_crecimiento"]:
        datos["monto_bono_crecimiento"] = entero_monto(request.form["monto_bono_crecimiento"])

    datos["aplica_bono_mercadotecnia"] = "activa_bono_mercadotecnia" in request.form
    if datos["aplica_bono_mercadotecnia"]:
        datos["monto_bono_mercadotecnia"] = entero_monto(request.form["monto_bono_mercadotecnia"])

    datos["aplica_bono_nuevas_aperturas"] = "activa_bono_nuevas_aperturas" in request.form
    if datos["aplica_bono_nuevas_aperturas"]:
        datos["tipo_nuevas_aperturas"] = request.form["tipo_nuevas_aperturas"]
        datos["monto_nuevas_aperturas"] = entero_monto(request.form["monto_nuevas_aperturas"])
        datos["num_establecimientos"] = int(request.form["num_establecimientos"])
        datos["meses_apertura"] = int(request.form["meses_apertura"])
        datos["maximo_bono"] = entero_monto(request.form["maximo_bono"])
        datos["periodo_amortizacion"] = int(request.form["periodo_amortizacion"])

    # --- fondos ---
    datos["aplica_fondo_mercadotecnia"] = "activa_fondo_mercadotecnia" in request.form
    if datos["aplica_fondo_mercadotecnia"]:
        datos["monto_fondo_mercadotecnia"] = entero_monto(request.form["monto_fondo_mercadotecnia"])

    datos["aplica_fondo_mercadotecnia_ooh"] = "activa_fondo_mercadotecnia_ooh" in request.form
    if datos["aplica_fondo_mercadotecnia_ooh"]:
        datos["monto_fondo_mercadotecnia_ooh"] = entero_monto(request.form["monto_fondo_mercadotecnia_ooh"])

    datos["aplica_linea_nuevas_aperturas"] = "activa_linea_nuevas_aperturas" in request.form
    if datos["aplica_linea_nuevas_aperturas"]:
        datos["monto_linea_nuevas_aperturas"] = entero_monto(request.form["monto_linea_nuevas_aperturas"])

    # --- compromisos adicionales ---
    datos["aplica_descuento_menu"] = "activa_descuento_menu" in request.form
    if datos["aplica_descuento_menu"]:
        datos["n_descuento_menu"] = int(request.form["n_descuento_menu"])
        datos["n_meses_descuento_menu"] = int(request.form["n_meses_descuento_menu"])

    datos["aplica_mark_down"] = "activa_mark_down" in request.form
    if datos["aplica_mark_down"]:
        datos["n_descuento_mark_down"] = int(request.form["n_descuento_mark_down"])

    datos["aplica_publicaciones_redes"] = "activa_publicaciones_redes" in request.form
    if datos["aplica_publicaciones_redes"]:
        datos["n_descuento_redes"] = int(request.form["n_descuento_redes"])

    datos["aplica_platillos_top_seller"] = "activa_platillos_top_seller" in request.form
    if datos["aplica_platillos_top_seller"]:
        datos["n_cantidad_platillos"] = int(request.form["n_cantidad_platillos"])
        datos["n_descuento_platillos"] = int(request.form["n_descuento_platillos"])
        datos["n_meses_descuento_platillos"] = int(request.form["n_meses_descuento_platillos"])

    # --- correos ---
    datos["correo_comercial"] = request.form["correo_comercial"]
    datos["correo_aliado"] = request.form["correo_aliado"]

    # --- datos bancarios ---
    datos["titular"] = datos["razon_social"]
    datos["n_clabe"] = request.form["n_clabe"]
    datos["n_cuenta"] = request.form["n_cuenta"]
    datos["banco"] = request.form["banco"]

# --- elegir plantilla y generar ---
    try:
        plantilla = BASE_DIR / "formatos" / PLANTILLAS[(datos["tipo_persona"], datos["tiene_ads"])]
        salida = generar_acuerdo(datos, plantilla)

        session["archivo_generado"] = str(salida)
        session["nombre_descarga"] = salida.name


        session["form_data"] = dict(request.form)
    
    except (ValueError, FileNotFoundError, PermissionError) as e:
        return render_template(
            "formulario.html",
            errores={"_general": str(e)},
            form_data=request.form,
        )
    return redirect(url_for("confirmacion"))

@app.route("/confirmacion")
def confirmacion():
    ruta_archivo = session.get("archivo_generado")
    nombre_descarga = session.get("nombre_descarga")
    if not ruta_archivo:
        return redirect(url_for("formulario"))
    return render_template("confirmacion.html", nombre_descarga=nombre_descarga)


@app.route("/nuevo")
def nuevo():

    session.pop("archivo_generado", None)
    session.pop("nombre_descarga", None)

    session.pop("form_data", None)

    return redirect(url_for("formulario"))

@app.route("/descargar")
def descargar():
    ruta_archivo = session.get("archivo_generado")
    nombre_descarga = session.get("nombre_descarga")

    if not ruta_archivo:
        return redirect(url_for("formulario"))

    try:
        with open(ruta_archivo, "rb") as f:
            contenido = f.read()
    except FileNotFoundError:
        session.pop("archivo_generado", None)
        session.pop("nombre_descarga", None)
        return render_template(
            "formulario.html",
            errores={"_general": "Este enlace de descarga ya no está disponible. Genera el acuerdo nuevamente."},
            form_data={},
        )

    try:
        os.remove(ruta_archivo)
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

    session.pop("archivo_generado", None)
    session.pop("nombre_descarga", None)

    return send_file(
        io.BytesIO(contenido),
        as_attachment=True,
        download_name=nombre_descarga,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")