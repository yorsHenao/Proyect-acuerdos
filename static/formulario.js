
const bloque_fisica = document.getElementById("bloque-fisica");
const bloque_juridica = document.getElementById("bloque-juridica");


const button_fisica = document.getElementById("tipo_persona_fisica");
const button_juridica = document.getElementById("tipo_persona_juridica");

button_fisica.addEventListener("change", () => {
    bloque_fisica.classList.remove("oculto");
    bloque_juridica.classList.add("oculto");
});

button_juridica.addEventListener("change", () => {
    bloque_fisica.classList.add("oculto");
    bloque_juridica.classList.remove("oculto");
});



const button_ads = document.getElementById("tiene_ads");
const n_ads = document.getElementById("porcentaje-ads");
const tipo_ads = document.getElementById("tipo_ads");
const porcentaje_ads_rappi = document.getElementById("porcentaje-ads-rappi");

function actualizarAdsRappi() {
    if (tipo_ads.value === "aliado_y_rappi") {
        porcentaje_ads_rappi.classList.remove("oculto");
    } else {
        porcentaje_ads_rappi.classList.add("oculto");
    }
}

button_ads.addEventListener("change", () => {
    if (button_ads.checked) {
        n_ads.classList.remove("oculto");
    } else {
        n_ads.classList.add("oculto");
    }
})

tipo_ads.addEventListener("change", actualizarAdsRappi);
actualizarAdsRappi();


const inf_c_fija = document.getElementById("bloque-comision-fija");
const inf_c_escalonada = document.getElementById("bloque-c-escalonada");
const modalidadEscalonada = document.getElementById("modalidad_escalonada");
const bloqueComisionOrdenes = document.getElementById("bloque-comision-ordenes");

function actualizarModalidadEscalonada() {
    const esOrdenes = modalidadEscalonada.value === "ordenes";
    bloqueComisionOrdenes.classList.toggle("oculto", !esOrdenes);
    document.querySelectorAll("#bloque-c-escalonada .escalon, #agregar_escalon").forEach((elemento) => {
        elemento.classList.toggle("oculto", esOrdenes);
    });
    document.querySelectorAll("#bloque-c-escalonada .escalon input").forEach((input) => {
        input.disabled = esOrdenes;
    });
    bloqueComisionOrdenes.querySelectorAll("input").forEach((input) => {
        input.disabled = !esOrdenes;
    });
}

const comision = document.querySelectorAll('input[name="tipo_comision"]');


comision.forEach((radio) => {
    radio.addEventListener("change", (e) => {

        if (e.target.value === "fija" ) {

            inf_c_fija.classList.remove("oculto");
            inf_c_escalonada.classList.add("oculto");
        } else {

            inf_c_fija.classList.add("oculto");
            inf_c_escalonada.classList.remove("oculto");
            actualizarModalidadEscalonada();
        }
    })
})

modalidadEscalonada.addEventListener("change", actualizarModalidadEscalonada);
actualizarModalidadEscalonada();


const bono_crecimiento = document.getElementById("monto-bono-crecimiento");
const bono_mercadotecnia = document.getElementById("monto-bono-mercadotecnia");
const bono_nuevas_aperturas = document.getElementById("bloque-bono-nuevas-aperturas");

const bloque_inf_aperturas = document.getElementById("bloque-inf-aperturas-previo");

const button_crecimiento = document.getElementById("activa_bono_crecimiento");
const button_mercadotecnia = document.getElementById("activa_bono_mercadotecnia");
const button_nuevas_aperturas = document.getElementById("activa_bono_nuevas_aperturas");


button_crecimiento.addEventListener("change", () => {
    if (button_crecimiento.checked) {
        bono_crecimiento.classList.remove("oculto");
    } else {
        bono_crecimiento.classList.add("oculto");
    }
})

button_mercadotecnia.addEventListener("change", () => {
    if (button_mercadotecnia.checked) {
        bono_mercadotecnia.classList.remove("oculto");
    } else {
        bono_mercadotecnia.classList.add("oculto");
    }
})


const panel_nuevas_aperturas = document.getElementById("panel-bono-nuevas-aperturas");

button_nuevas_aperturas.addEventListener("change", () => {
    if (button_nuevas_aperturas.checked) {
        panel_nuevas_aperturas.classList.remove("oculto");
    } else {
        panel_nuevas_aperturas.classList.add("oculto");
    }
})


const bloque_fondo_mercadotecnia = document.getElementById("monto-fondo-mercadotecnia");
const bloque_nuevas_aperturas = document.getElementById("monto-nuevas-aperturas");



const button_fondo_mercadotecnia = document.getElementById("activa_fondo_mercadotecnia");
const button_nuevas_aperturas_fondo = document.getElementById("activa_linea_nuevas_aperturas");

button_fondo_mercadotecnia.addEventListener("change", () => {
    if (button_fondo_mercadotecnia.checked) {
        bloque_fondo_mercadotecnia.classList.remove("oculto");
    } else {
        bloque_fondo_mercadotecnia.classList.add("oculto");
    }
})

button_nuevas_aperturas_fondo.addEventListener("change", () => {
    if (button_nuevas_aperturas_fondo.checked) {
        bloque_nuevas_aperturas.classList.remove("oculto");
    } else {
        bloque_nuevas_aperturas.classList.add("oculto");
    }
})


const inf_menu = document.getElementById("info-descuento-menu");
const inf_mark_down = document.getElementById("info-mark-down");
const inf_redes = document.getElementById("info-publicaciones-redes");
const inf_top_seller = document.getElementById("info-top-seller");

const button_descuento_menu = document.getElementById("activa_descuento_menu");
const button_mark_down = document.getElementById("activa_mark_down");
const button_redes = document.getElementById("activa_publicaciones_redes");
const button_top_seller = document.getElementById("activa_platillos_top_seller");

button_descuento_menu.addEventListener("change", () => {
    if (button_descuento_menu.checked) {
        inf_menu.classList.remove("oculto");
    } else {
        inf_menu.classList.add("oculto");
    }
})

button_mark_down.addEventListener("change", () => {
    if (button_mark_down.checked) {
        inf_mark_down.classList.remove("oculto");
    } else {
        inf_mark_down.classList.add("oculto");
    }
})

button_redes.addEventListener("change", () => {
    if (button_redes.checked) {
        inf_redes.classList.remove("oculto");
    } else {
        inf_redes.classList.add("oculto");
    }
})

button_top_seller.addEventListener("change", () => {
    if (button_top_seller.checked) {
        inf_top_seller.classList.remove("oculto");
    } else {
        inf_top_seller.classList.add("oculto");
    }
})


const contenedorEscalones = document.getElementById("bloque-c-escalonada");
const botonAgregar = document.getElementById("agregar_escalon");
const escalonMolde = document.querySelector(".escalon");

let contadorEscalones = 1;

botonAgregar.addEventListener("click", () => {
    // 1. Fotocopia
    const nuevoEscalon = escalonMolde.cloneNode(true);
    nuevoEscalon.setAttribute("data-escalon", contadorEscalones);

    // 2. Modificar Inputs
    const inputsClon = nuevoEscalon.querySelectorAll("input");
    inputsClon.forEach((input) => {
        input.id = input.id.replace("escalon_0", `escalon_${contadorEscalones}`);
        input.name = input.name.replace("escalon_0", `escalon_${contadorEscalones}`);

        if (input.type === "checkbox") {
            input.checked = false;
        } else if (input.type === "radio") {
            input.checked = (input.value === "no");
        } else {
            input.value = "";
        }
    });

    
    const labelsClon = nuevoEscalon.querySelectorAll("label");
    labelsClon.forEach((label) => {
        const forOriginal = label.getAttribute("for");
        if (forOriginal) {
            label.setAttribute("for", forOriginal.replace("escalon_0", `escalon_${contadorEscalones}`));
        }
    });
    
    const botonEliminar = document.createElement("button");
    botonEliminar.type = "button";
    botonEliminar.textContent = "Eliminar Escalón";
    botonEliminar.classList.add("boton-eliminar-escalon", "option-radius");

    nuevoEscalon.appendChild(botonEliminar);

    
    contenedorEscalones.insertBefore(nuevoEscalon, botonAgregar);
    contadorEscalones++;
});

contenedorEscalones.addEventListener("click", (evento) => {
    if (evento.target.classList.contains("boton-eliminar-escalon")) {
        const escalonAEliminar = evento.target.closest(".escalon");
        escalonAEliminar.remove();
    }
})




contenedorEscalones.addEventListener("change", (evento) => {
    const esRadioDeultimo = evento.target.name && evento.target.name.endsWith("_es_ultimo");

    if (esRadioDeultimo) {
        const escalonActual = evento.target.closest(".escalon");
        const CampoFin = escalonActual.querySelector('input[id$="_fin"]');

        if (evento.target.value === "si") {
            CampoFin.value = "";
            CampoFin.readOnly = true;
        } else {
            CampoFin.readOnly = false;
        }
    }
})


// scrollspy
const linksMenu = document.querySelectorAll(".menu-nav a");
const offsetDeteccion = 120;

function obtenerSeccionesMenuVisibles() {
    return Array.from(linksMenu)
        .map((link) => {
            const href = link.getAttribute("href");
            return href ? document.querySelector(href) : null;
        })
        .filter((seccion) => seccion && !seccion.classList.contains("oculto"));
}

function actualizarMenuActivo() {
    const seccionesVisibles = obtenerSeccionesMenuVisibles();
    if (seccionesVisibles.length === 0) {
        return;
    }

    // La línea de referencia se adapta al alto de pantalla.
    const lineaReferencia = Math.max(offsetDeteccion, window.innerHeight * 0.35);
    let seccionActual = seccionesVisibles[0];

    seccionesVisibles.forEach((seccion) => {
        const top = seccion.getBoundingClientRect().top;
        if (top <= lineaReferencia) {
            seccionActual = seccion;
        }
    });

    // Si ya estamos al final del documento, activar la última sección visible.
    const alturaDocumento = document.documentElement.scrollHeight;
    const fondoViewport = window.scrollY + window.innerHeight;
    if (fondoViewport >= alturaDocumento - 2) {
        seccionActual = seccionesVisibles[seccionesVisibles.length - 1];
    }

    linksMenu.forEach((link) => link.classList.remove("item-menu-activo"));

    const linkActivo = document.querySelector(`.menu-nav a[href="#${seccionActual.id}"]`);
    if (linkActivo) {
        linkActivo.classList.add("item-menu-activo");
    }
}

linksMenu.forEach((link) => {
    link.addEventListener("click", (evento) => {
        const href = link.getAttribute("href");
        const seccion = href ? document.querySelector(href) : null;
        if (!seccion) {
            return;
        }

        evento.preventDefault();
        const topObjetivo = seccion.getBoundingClientRect().top + window.scrollY - 84;
        window.scrollTo({ top: topObjetivo, behavior: "smooth" });
    });
});

window.addEventListener("scroll", actualizarMenuActivo);
window.addEventListener("resize", actualizarMenuActivo);
actualizarMenuActivo();

const MAX_DIGITOS_MONTO = 9;
const IDS_MONTOS = [
    "monto_bono_crecimiento",
    "monto_bono_mercadotecnia",
    "monto_nuevas_aperturas",
    "maximo_bono",
    "monto_fondo_mercadotecnia",
    "monto_linea_nuevas_aperturas",
];

function posicionTrasDigitos(texto, cantidadDigitos) {
    if (cantidadDigitos <= 0) {
        return 0;
    }
    let vistos = 0;
    for (let indice = 0; indice < texto.length; indice += 1) {
        if (texto[indice] !== ",") {
            vistos += 1;
        }
        if (vistos >= cantidadDigitos) {
            return indice + 1;
        }
    }
    return texto.length;
}

function valorMontoFormateado(texto, digitosAntesCursor) {
    let entero = texto.replace(/\D/g, "").replace(/^0+(?=\d)/, "");
    if (entero === "") {
        return { valor: "", cursor: 0 };
    }
    if (entero.length > MAX_DIGITOS_MONTO) {
        entero = entero.slice(0, MAX_DIGITOS_MONTO);
    }
    const formateado = entero.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    const cursor = digitosAntesCursor === null
        ? formateado.length
        : posicionTrasDigitos(formateado, digitosAntesCursor);
    return { valor: formateado, cursor };
}

function aplicarFormatoMonto(input, moverCursor) {
    const cursor = input.selectionStart ?? input.value.length;
    const digitosAntes = moverCursor
        ? input.value.slice(0, cursor).replace(/\D/g, "").length
        : null;
    const resultado = valorMontoFormateado(input.value, digitosAntes);
    input.value = resultado.valor;
    if (moverCursor && typeof input.setSelectionRange === "function") {
        input.setSelectionRange(resultado.cursor, resultado.cursor);
    }
}

function formatearMiles(input) {
    if (!input || input.dataset.montoFormateado === "si") {
        return;
    }
    input.dataset.montoFormateado = "si";
    input.addEventListener("input", () => aplicarFormatoMonto(input, true));
    input.addEventListener("paste", (evento) => {
        evento.preventDefault();
        const pegado = (evento.clipboardData || window.clipboardData).getData("text");
        const inicio = input.selectionStart ?? input.value.length;
        const fin = input.selectionEnd ?? input.value.length;
        input.value = input.value.slice(0, inicio) + pegado + input.value.slice(fin);
        aplicarFormatoMonto(input, true);
    });
    if (input.value.trim() !== "") {
        aplicarFormatoMonto(input, false);
    }
}

function inicializarMontosConComas() {
    const vistos = new Set();
    document.querySelectorAll(".input-monto").forEach((input) => {
        formatearMiles(input);
        vistos.add(input.id);
    });
    IDS_MONTOS.forEach((id) => {
        const input = document.getElementById(id);
        if (input && !vistos.has(id)) {
            input.classList.add("input-monto");
            formatearMiles(input);
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    inicializarMontosConComas();
    formatearEscritura(document.getElementById("n_acta_constitutiva"));

    const primerError = Array.from(document.querySelectorAll(".input-error"))
        .find((el) => el.closest(".oculto") === null);
    if (primerError) {
        primerError.scrollIntoView({ behavior: "smooth", block: "center" });
        primerError.focus();
    }
});

function formatearEscritura(input) {
    input.addEventListener("input", () => {
        const digitos = input.value.replace(/\D/g, "").replace(/^0+(?=\d)/, "");
        input.value = digitos.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    });
}



