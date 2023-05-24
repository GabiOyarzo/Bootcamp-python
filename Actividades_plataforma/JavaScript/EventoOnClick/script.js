// Javascript de Actividad  OnClick   
// Gabriela Oyarzo Escudero
// fecha: 23/05/2023
// última actualización: 24/05/2023


function LogInOut(element) {
    element.innerText = "Logout";
}

function hide(element) {
    element.remove();
}

let contador1 = 5;
function AddCont1(element){
    contador1 ++;
    element.innerText = ( contador1 + " likes");
    alert("Ninja was liked");
};

let contador2 = 17;
function AddCont2(element){
    contador2 ++;
    element.innerText = ( contador2 + " likes");
    alert("Ninja was liked");
};