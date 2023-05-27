// Javascript de Actividad  me gusta 
// Gabriela Oyarzo Escudero
// última actualización: 26/05/2023

function LogInOut() {
    estado = document.querySelector("#btn_login")
    if ( estado.innerText == "LogOut") {
        estado.innerText = "Login";
    } else  if (estado.innerText == "Login") {
        estado.innerText = "LogOut";
    }
}

function AddCont(selector) {
    var aux1 = document.querySelector(selector);
    var contador = parseInt(aux1.innerText);
    contador++;
    aux1.innerText = contador + " like(s)";
};
