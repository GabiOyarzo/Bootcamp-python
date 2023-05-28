

function LogInOut() {
    estado = document.querySelector("#btn_login")
    contenedor = document.querySelector(".contenedor-grande")
    if ( estado.innerText == "LogOut") {
        estado.innerText = "Login";
        contenedor.remove()
        var loginPage =  document.createElement(".contenedor-perfil")
    } else  if (estado.innerText == "Login") {
        estado.innerText = "LogOut";
    }
}




function AddCont(element){
    contador = parseInt(element.innerText);
    contador ++;
    element.innerText = ( contador + " likes");
    alert("Ninja was liked");
};

