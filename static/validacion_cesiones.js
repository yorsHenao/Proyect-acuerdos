const regexRazonesSociales = /[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9.,&\-\s]/g;
const regexNombres = /[^a-zA-ZáéíóúÁÉÍÓÚñÑ\-\s]/g;
const regexRfc = /[^a-zA-Z0-9]/g;
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

restringirCaracteres("nombre_cedente", regexNombres, 100);
restringirCaracteres("nombre_cesionario", regexNombres, 100);
restringirCaracteres("razon_social_cedente", regexRazonesSociales, 150);
restringirCaracteres("razon_social_cesionario", regexRazonesSociales, 150);
restringirCaracteres("representante_legal_cedente", regexNombres, 100);
restringirCaracteres("representante_legal_cesionario", regexNombres, 100);
restringirRfc("rfc_cedente_fisica", 13);
restringirRfc("rfc_cedente_moral", 12);
restringirRfc("rfc_cesionario_fisica", 13);
restringirRfc("rfc_cesionario_moral", 12);
restringirCaracteres("marca", regexRazonesSociales, 100);
restringirCaracteres("banco", regexRazonesSociales, 100);
limiteNumeros("n_clabe", 18);
limiteNumeros("n_cuenta", 16);
