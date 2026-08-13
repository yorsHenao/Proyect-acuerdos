
const button_crear_acuerdo = document.getElementById("btn-crear-acuerdo");
const button_descargar_acuerdo = document.getElementById("btn-descargar-acuerdo");

button_descargar_acuerdo.addEventListener("click", () => {
    button_crear_acuerdo.classList.remove("oculto");
})