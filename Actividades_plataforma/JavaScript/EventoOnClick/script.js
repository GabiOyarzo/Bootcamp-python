// Javascript de Actividad  OnClick   
// Gabriela Oyarzo Escudero
// fecha: 23/05/2023
// última actualización: 24/05/2023

function LogInOut(element) {
    estado = element.innerText;
    if ( estado == "LogOut") {
        element.innerText = "Login";
    } else  if (estado == "Login") {
        element.innerText = "LogOut";
    }
}

function hide(element) {
    element.remove();
}

function AddCont(element){
    contador = parseInt(element.innerText);
    contador ++;
    element.innerText = ( contador + " likes");
    alert("Ninja was liked");
};

