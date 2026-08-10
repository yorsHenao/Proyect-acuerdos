// ================================
// Resumen antes de generar
// ================================

const RESUMEN_ITEMS = [
  { checkbox: "tiene_ads", label: "ADS", campos: [
      { id: "n_ads", etiqueta: "Porcentaje", sufijo: "%" },
  ]},
  { checkbox: "activa_bono_crecimiento", label: "Bono de Crecimiento", campos: [
      { id: "monto_bono_crecimiento", etiqueta: "Monto", prefijo: "$" },
  ]},
  { checkbox: "activa_bono_mercadotecnia", label: "Bono de Mercadotecnia", campos: [
      { id: "monto_bono_mercadotecnia", etiqueta: "Monto", prefijo: "$" },
  ]},
  { checkbox: "activa_bono_nuevas_aperturas", label: "Bono de Nuevas Aperturas", campos: [
      { id: "monto_nuevas_aperturas", etiqueta: "Monto", prefijo: "$" },
      { id: "num_establecimientos", etiqueta: "Establecimientos" },
      { id: "meses_apertura", etiqueta: "Meses para abrir" },
      { id: "maximo_bono", etiqueta: "Apoyo máximo", prefijo: "$" },
      { id: "periodo_amortizacion", etiqueta: "Amortización (meses)" },
  ]},
  { checkbox: "activa_fondo_mercadotecnia", label: "Fondo de Mercadotecnia", campos: [
      { id: "monto_fondo_mercadotecnia", etiqueta: "Monto", prefijo: "$" },
  ]},
  { checkbox: "activa_fondo_mercadotecnia_ooh", label: "Fondo de Mercadotecnia OOH", campos: [
      { id: "monto_fondo_mercadotecnia_ooh", etiqueta: "Monto", prefijo: "$" },
  ]},
  { checkbox: "activa_linea_nuevas_aperturas", label: "Línea de Nuevas Aperturas", campos: [
      { id: "monto_linea_nuevas_aperturas", etiqueta: "Monto", prefijo: "$" },
  ]},
  { checkbox: "activa_descuento_menu", label: "Descuento en Menú", campos: [
      { id: "n_descuento_menu", etiqueta: "Descuento", sufijo: "%" },
      { id: "n_meses_descuento_menu", etiqueta: "Meses" },
  ]},
  { checkbox: "activa_mark_down", label: "Mark Down", campos: [
      { id: "n_descuento_mark_down", etiqueta: "Inversión", sufijo: "%" },
  ]},
  { checkbox: "activa_publicaciones_redes", label: "Publicaciones en Redes", campos: [
      { id: "n_descuento_redes", etiqueta: "Publicaciones" },
  ]},
  { checkbox: "activa_platillos_top_seller", label: "Platillos Top Seller", campos: [
      { id: "n_cantidad_platillos", etiqueta: "Cantidad" },
      { id: "n_descuento_platillos", etiqueta: "Descuento", sufijo: "%" },
      { id: "n_meses_descuento_platillos", etiqueta: "Meses" },
  ]},
];

function construirResumen() {
  const lista = document.getElementById("resumen-lista");
  if (!lista) return;
  lista.innerHTML = "";

  // 1. Tipo de Persona (Fijo)
  const tipoPersonaInput = document.getElementById("tipo_persona") || document.querySelector('input[name="tipo_persona"]:checked');
  if (tipoPersonaInput && tipoPersonaInput.value) {
    lista.innerHTML += `<li><strong>Tipo de Persona:</strong> ${tipoPersonaInput.value}</li>`;
  }

  // 2. Vigencia (Fijo)
  const vigenciaInput = document.getElementById("vigencia_meses");
  if (vigenciaInput && vigenciaInput.value) {
    lista.innerHTML += `<li><strong>Vigencia:</strong> ${vigenciaInput.value} meses</li>`;
  }

  // 3. Comisión (Fijo)
  const comisionRadio = document.querySelector('input[name="tipo_comision"]:checked');
  if (comisionRadio) {
    if (comisionRadio.value === "fija") {
      const valor = document.getElementById("n_comision_fija")?.value || "";
      lista.innerHTML += `<li><strong>Comisión:</strong> Fija, ${valor}%</li>`;
    } else if (comisionRadio.value === "escalonada") {
      const modalidad = document.getElementById("modalidad_escalonada")?.value || "";
      const tramos = document.querySelectorAll("#bloque-c-escalonada .escalon").length;
      lista.innerHTML += `<li><strong>Comisión:</strong> Escalonada por ${modalidad} (${tramos} tramo${tramos === 1 ? "" : "s"})</li>`;
    }
  }

  // 4. Correos (Fijo)
  const correosInput = document.getElementById("correos") || document.getElementById("correo") || document.getElementById("email");
  if (correosInput && correosInput.value) {
    lista.innerHTML += `<li><strong>Correo(s):</strong> ${correosInput.value}</li>`;
  }

  // 5. Banco (Fijo)
  const bancoInput = document.getElementById("banco") || document.getElementById("banco_nombre");
  if (bancoInput && bancoInput.value) {
    lista.innerHTML += `<li><strong>Banco:</strong> ${bancoInput.value}</li>`;
  }

  // Bloques opcionales (solo si el checkbox está activo)
  RESUMEN_ITEMS.forEach((item) => {
    const checkbox = document.getElementById(item.checkbox);
    if (!checkbox || !checkbox.checked) return;

    const detalles = item.campos
      .map((campo) => {
        const input = document.getElementById(campo.id);
        const valor = input ? input.value : "";
        if (!valor) return null;
        return `${campo.etiqueta}: ${campo.prefijo || ""}${valor}${campo.sufijo || ""}`;
      })
      .filter(Boolean)
      .join(" · ");

    lista.innerHTML += `<li><strong>${item.label}:</strong> ${detalles}</li>`;
  });

  if (!lista.innerHTML) {
    lista.innerHTML = "<li>No se activó ninguna opción adicional.</li>";
  }
}

const btnAbrirResumen = document.getElementById("btn-abrir-resumen");
const modalResumen = document.getElementById("modal-resumen");
const btnCancelarResumen = document.getElementById("btn-cancelar-resumen");

window.addEventListener("load", () => {
  if (modalResumen) modalResumen.classList.add("oculto");
});

if (btnAbrirResumen) {
  btnAbrirResumen.addEventListener("click", (e) => {
    e.preventDefault();

    // Buscar elementos marcados con la clase 'input-error'
    // Se ignoran los que están ocultos (display:none, p. ej. por cambiar
    // de tipo de persona, tipo de comisión, o desactivar un bono/fondo),
    // porque un campo oculto ya no es obligatorio y el usuario no puede
    // corregirlo si no lo ve.
    const camposConError = Array.from(document.querySelectorAll(".input-error"))
    .filter((el) => el.closest(".oculto") === null);

    if (camposConError.length > 0) {
      const primerError = camposConError[0];

      // Hace scroll suave directo al primer error sin alert
      primerError.scrollIntoView({ behavior: "smooth", block: "center" });

      // Enfoca el campo sin cancelar la animación del scroll
      if (typeof primerError.focus === "function") {
        primerError.focus({ preventScroll: true });
      }

      return; // Detiene la apertura del modal si hay errores
    }

    construirResumen();
    if (modalResumen) {
      modalResumen.classList.remove("oculto");
      modalResumen.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
}

if (btnCancelarResumen) {
  btnCancelarResumen.addEventListener("click", () => {
    if (modalResumen) modalResumen.classList.add("oculto");
  });
}

// ================================
// Limpiar errores al escribir o cambiar
// ================================
document.addEventListener("input", limpiarErrorAlEscribir);
document.addEventListener("change", limpiarErrorAlEscribir);

function limpiarErrorAlEscribir(e) {
  const campo = e.target;
  if (!campo.classList || !campo.classList.contains("input-error")) return;

  const tieneValor = campo.type === "checkbox" || campo.type === "radio"
    ? campo.checked
    : Boolean(campo.value && campo.value.trim());

  if (!tieneValor) return;

  console.log("Limpiando error de:", campo.id || campo.name);
  campo.classList.remove("input-error");

  // Para radios/checkboxes, buscar el mensaje de error en la sección contenedora
  if (campo.type === "radio" || campo.type === "checkbox") {
    // Buscar la sección padre más cercana
    const seccion = campo.closest("section") || campo.closest(".container-radius") || campo.parentElement.parentElement;
    if (seccion) {
      const mensaje = seccion.querySelector(".mensaje-error");
      if (mensaje) {
        mensaje.remove();
        console.log("Removido mensaje de error de radio/checkbox");
      }
    }

    // También limpiar otros radios/checkboxes del mismo grupo
    const nombreCampo = campo.name;
    const otrosCampos = document.querySelectorAll(`input[name="${nombreCampo}"].input-error`);
    otrosCampos.forEach(otro => otro.classList.remove("input-error"));
  } else {
    // Para inputs de texto, buscar el mensaje inmediatamente después
    let hermano = campo.nextElementSibling;
    while (hermano) {
      if (hermano.classList && hermano.classList.contains("mensaje-error")) {
        hermano.remove();
        break;
      }
      hermano = hermano.nextElementSibling;
    }
  }
}