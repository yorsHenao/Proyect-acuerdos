const regexRazonesSociales = /[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9.,&\-\s]/g;
const regexNombres = /[^a-zA-ZáéíóúÁÉÍÓÚñÑ\-\s]/g;
const regexDirecciones = /[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9.,#\/\-\s]/g;
const regexRfc = /[^a-zA-Z0-9]/g;
const regexAlfanumerico = /[^a-zA-Z0-9\-\/\s]/g;
const regexCorreo = /[^a-zA-Z0-9@._+\-]/g;

function restringirCaracteres(id, regexNoPermitido, max) {
    const input = document.getElementById(id);

    if (input) {
        input.addEventListener("input", () => {
            input.value = input.value.replace(regexNoPermitido, "").slice(0, max);
        });
    }
}

function restringirRfc(id, max) {
    const input = document.getElementById(id);

    if (input) {
        input.addEventListener("input", () => {
            input.value = input.value.toUpperCase().replace(regexRfc, "").slice(0, max);
        });
    }
}

function limiteNumeros(id, max) {
    const input = document.getElementById(id);

    if (input) {
        input.addEventListener("input", () => {
            input.value = input.value.replace(/\D/g, "").slice(0, max);
        });
    }
}

function limitarInputNumerico(input, max) {
    input.value = input.value.replace(/\D/g, "").slice(0, max);
}

// Persona fisica
restringirCaracteres("razon_social_fisica", regexNombres, 100);
restringirRfc("rfc_fisica", 13);
restringirCaracteres("direccion_fisica", regexDirecciones, 200);
restringirCaracteres("marca_fisica", regexRazonesSociales, 100);

// Persona juridica
restringirCaracteres("razon_social_juridica", regexRazonesSociales, 100);
restringirRfc("rfc_juridica", 12);
restringirCaracteres("direccion_juridica", regexDirecciones, 200);
restringirCaracteres("representante_legal_juridica", regexNombres, 100);
restringirCaracteres("n_acta_constitutiva", regexAlfanumerico, 100);
restringirCaracteres("notario", regexNombres, 100);
limiteNumeros("numero_notaria", 20);
restringirCaracteres("ubicacion_notaria", regexDirecciones, 200);
restringirCaracteres("n_folio_mercantil", regexAlfanumerico, 100);
restringirCaracteres("marca_juridica", regexRazonesSociales, 100);

// Contactos
restringirCaracteres("correo_comercial", regexCorreo, 120);
restringirCaracteres("correo_aliado", regexCorreo, 120);

// Datos bancarios
limiteNumeros("n_clabe", 18);
limiteNumeros("n_cuenta", 10);
restringirCaracteres("banco", regexRazonesSociales, 100);

// Campos dinamicos de comision escalonada (creados al clonar escalones)
document.addEventListener("input", (evento) => {
    const input = evento.target;

    if (!input || input.tagName !== "INPUT") {
        return;
    }

    if (/^escalon_\d+_fin$/.test(input.id)) {
        limitarInputNumerico(input, 3);
    }

    if (/^escalon_\d+_porcentaje$/.test(input.id)) {
        limitarInputNumerico(input, 3);
    }
});

