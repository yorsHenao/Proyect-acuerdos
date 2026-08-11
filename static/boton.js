// Ocultar tipo de persona
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

//ocultar si no tiene ads

const button_ads = document.getElementById("tiene_ads");
const n_ads = document.getElementById("porcentaje-ads");

button_ads.addEventListener("change", () => {
    if (button_ads.checked) {
        n_ads.classList.remove("oculto");
    } else {
        n_ads.classList.add("oculto");
    }
})

// Ocultar comision 
const inf_c_fija = document.getElementById("bloque-comision-fija");
const inf_c_escalonada = document.getElementById("bloque-c-escalonada");

const comision = document.querySelectorAll('input[name="tipo_comision"]');


comision.forEach((radio) => {
    radio.addEventListener("change", (e) => {

        if (e.target.value === "fija" ) {

            inf_c_fija.classList.remove("oculto");
            inf_c_escalonada.classList.add("oculto");
        } else {

            inf_c_fija.classList.add("oculto");
            inf_c_escalonada.classList.remove("oculto");
        }
    })
})

//ocultar bonos
//se olcuto los campos de los valores,
//bonos nuevas aperturas, se oculto botones para previo y posterios. si se activa bono nuevas aperturas
// sale para establecer establecimientos y monto
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

//saca el bloque para agregar monto, establecimientos, meses, apoyo maximo, periodo de amortizacion
const panel_nuevas_aperturas = document.getElementById("panel-bono-nuevas-aperturas");

button_nuevas_aperturas.addEventListener("change", () => {
    if (button_nuevas_aperturas.checked) {
        panel_nuevas_aperturas.classList.remove("oculto");
    } else {
        panel_nuevas_aperturas.classList.add("oculto");
    }
})

// Fondos

const bloque_fondo_mercadotecnia = document.getElementById("monto-fondo-mercadotecnia");
const bloque_fondo_mercadotecnia_ooh = document.getElementById("monto-fondo-mercadotecnia-ooh");
const bloque_nuevas_aperturas = document.getElementById("monto-nuevas-aperturas");



const button_fondo_mercadotecnia = document.getElementById("activa_fondo_mercadotecnia");
const button_fondo_mercadotecnia_ooh = document.getElementById("activa_fondo_mercadotecnia_ooh");
const button_nuevas_aperturas_fondo = document.getElementById("activa_linea_nuevas_aperturas");

button_fondo_mercadotecnia.addEventListener("change", () => {
    if (button_fondo_mercadotecnia.checked) {
        // Desmarcar el otro checkbox de mercadotecnia
        button_fondo_mercadotecnia_ooh.checked = false;
        bloque_fondo_mercadotecnia_ooh.classList.add("oculto");
        bloque_fondo_mercadotecnia.classList.remove("oculto");
    } else {
        bloque_fondo_mercadotecnia.classList.add("oculto");
    }
})

button_fondo_mercadotecnia_ooh.addEventListener("change", () => {
    if (button_fondo_mercadotecnia_ooh.checked) {
        // Desmarcar el otro checkbox de mercadotecnia
        button_fondo_mercadotecnia.checked = false;
        bloque_fondo_mercadotecnia.classList.add("oculto");
        bloque_fondo_mercadotecnia_ooh.classList.remove("oculto");
    } else {
        bloque_fondo_mercadotecnia_ooh.classList.add("oculto");
    }
})

button_nuevas_aperturas_fondo.addEventListener("change", () => {
    if (button_nuevas_aperturas_fondo.checked) {
        bloque_nuevas_aperturas.classList.remove("oculto");
    } else {
        bloque_nuevas_aperturas.classList.add("oculto");
    }
})


// compromisos adiccionales

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


// Agregar / Eliminar Escalones de Comisión



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

    // 3. Modificar Labels
    const labelsClon = nuevoEscalon.querySelectorAll("label");
    labelsClon.forEach((label) => {
        const forOriginal = label.getAttribute("for");
        if (forOriginal) {
            label.setAttribute("for", forOriginal.replace("escalon_0", `escalon_${contadorEscalones}`));
        }
    });
    // 4. Crear Botón "Eliminar" (Una sola vez por clon)
    const botonEliminar = document.createElement("button");
    botonEliminar.type = "button";
    botonEliminar.textContent = "Eliminar Escalón";
    botonEliminar.classList.add("boton-eliminar-escalon", "option-radius");

    nuevoEscalon.appendChild(botonEliminar);

    // 5. Insertar en pantalla y sumar al contador
    contenedorEscalones.insertBefore(nuevoEscalon, botonAgregar);
    contadorEscalones++;
});

contenedorEscalones.addEventListener("click", (evento) => {
    if (evento.target.classList.contains("boton-eliminar-escalon")) {
        const escalonAEliminar = evento.target.closest(".escalon");
        escalonAEliminar.remove();
    }
})


/*Bloqueo "fin del escalonamiento"*/

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



// ================================
// Scroll Spy - resaltar sección activa en el menú
// ================================

// ================================
// Scroll Spy - resaltar sección activa en el menú
// ================================

const secciones = document.querySelectorAll(".card-section");
const linksMenu = document.querySelectorAll(".menu-nav a");
const offsetDeteccion = 100; // px desde el borde superior del viewport, línea de referencia

function actualizarMenuActivo() {
    let seccionActual = secciones[0];

    secciones.forEach((seccion) => {
        const top = seccion.getBoundingClientRect().top;
        if (top - offsetDeteccion <= 0) {
            seccionActual = seccion;
        }
    });

    linksMenu.forEach((link) => link.classList.remove("item-menu-activo"));

    const linkActivo = document.querySelector(`.menu-nav a[href="#${seccionActual.id}"]`);
    if (linkActivo) {
        linkActivo.classList.add("item-menu-activo");
    }
}

window.addEventListener("scroll", actualizarMenuActivo);
window.addEventListener("resize", actualizarMenuActivo);
actualizarMenuActivo(); // estado inicial al cargar la página


// Validacion de formulario

document.addEventListener("DOMContentLoaded", () => {
    const primerError = Array.from(document.querySelectorAll(".input-error"))
        .find((el) => el.closest(".oculto") === null);
    if (primerError) {
        primerError.scrollIntoView({ behavior: "smooth", block: "center" });
        primerError.focus();
    } 
})

// formatear monto

function formatearMiles(input) {
    input.addEventListener("input", () => {
        let soloNumeros = input.value.replace(/\D/g, "");

        input.value = soloNumeros.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    });
}

formatearMiles(document.getElementById("monto_bono_crecimiento"));
formatearMiles(document.getElementById("monto_bono_mercadotecnia"));
formatearMiles(document.getElementById("monto_nuevas_aperturas"));
formatearMiles(document.getElementById("maximo_bono"));
formatearMiles(document.getElementById("monto_fondo_mercadotecnia"));
formatearMiles(document.getElementById("monto_fondo_mercadotecnia_ooh"));
formatearMiles(document.getElementById("monto_linea_nuevas_aperturas"));

