// ==========================================================================
// Logica del Formulario de Cesion de Derechos (Rappi)
// ==========================================================================

document.addEventListener("DOMContentLoaded", () => {
    // Un bloque oculto sigue dentro del formulario. Si no se desactivan sus
    // campos, el navegador los envía vacíos y pisan al RFC del bloque visible.
    function mostrarBloque(bloque, visible) {
        if (!bloque) return;
        bloque.classList.toggle("oculto", !visible);
        bloque.querySelectorAll("input, select, textarea").forEach((campo) => {
            campo.disabled = !visible;
        });
    }

    // 1. Manejo dinamico de tipo de Cedente (Fisica vs Moral)
    const radiosTipoCedente = document.querySelectorAll('input[name="tipo_cedente"]');
    const bloqueCedenteFisica = document.getElementById("bloque-cedente-fisica");
    const bloqueCedenteMoral = document.getElementById("bloque-cedente-moral");

    function actualizarCedente() {
        const seleccionado = document.querySelector('input[name="tipo_cedente"]:checked');
        if (!seleccionado) return;

        radiosTipoCedente.forEach(radio => {
            const card = radio.closest(".radio-card-tipo");
            if (card) {
                if (radio.checked) {
                    card.classList.add("seleccionado");
                } else {
                    card.classList.remove("seleccionado");
                }
            }
        });

        const esFisica = seleccionado.value === "fisica";
        mostrarBloque(bloqueCedenteFisica, esFisica);
        mostrarBloque(bloqueCedenteMoral, !esFisica);
    }

    radiosTipoCedente.forEach(radio => {
        radio.addEventListener("change", actualizarCedente);
    });

    // 2. Manejo dinamico de tipo de Cesionario (Fisica vs Moral)
    const radiosTipoCesionario = document.querySelectorAll('input[name="tipo_cesionario"]');
    const bloqueCesionarioFisica = document.getElementById("bloque-cesionario-fisica");
    const bloqueCesionarioMoral = document.getElementById("bloque-cesionario-moral");

    function actualizarCesionario() {
        const seleccionado = document.querySelector('input[name="tipo_cesionario"]:checked');
        if (!seleccionado) return;

        radiosTipoCesionario.forEach(radio => {
            const card = radio.closest(".radio-card-tipo");
            if (card) {
                if (radio.checked) {
                    card.classList.add("seleccionado");
                } else {
                    card.classList.remove("seleccionado");
                }
            }
        });

        const esFisica = seleccionado.value === "fisica";
        mostrarBloque(bloqueCesionarioFisica, esFisica);
        mostrarBloque(bloqueCesionarioMoral, !esFisica);
    }

    radiosTipoCesionario.forEach(radio => {
        radio.addEventListener("change", actualizarCesionario);
    });

    // 3. Forzar RFC a mayusculas en tiempo real
    const inputsRfc = document.querySelectorAll('input[name="rfc_cedente"], input[name="rfc_cesionario"]');
    inputsRfc.forEach(input => {
        input.addEventListener("input", (e) => {
            e.target.value = e.target.value.toUpperCase();
        });
    });

    // 4. Forzar CLABE a solo digitos y max 18 caracteres
    const inputClabe = document.querySelector('input[name="n_clabe"]');
    if (inputClabe) {
        inputClabe.addEventListener("input", (e) => {
            e.target.value = e.target.value.replace(/\D/g, "").slice(0, 18);
        });
    }

    // Inicializar estado al cargar (o tras volver con form_data)
    actualizarCedente();
    actualizarCesionario();
});
