// Javascript actividad: DojoWeather

// Cambio de ciudad
function ChangeCity(name){
    var city = document.querySelector(name)
    alert('Loading weather report to '+ city.innerText)
}

// Guardando datos originales
var MaxTOri = null; 
var MinTOri = null; 

function ConvertTemperature(grado, maxT, minT){
    var MaxT = document.querySelectorAll(maxT);
    var MinT = document.querySelectorAll(minT);
    // Guardando datos originales
    if(MaxTOri === null && MinTOri === null){
        MaxTOri = MaxT[0].innerHTML;
        MinTOri = MinT[0].innerHTML;
    }
    // ---------------------------------------
    // Cambiando los valores según la unidad
    // ---------------------------------------
    if(grado === "Celsius"){
        MaxT.forEach(function(element) {element.textContent = MaxTOri});
        MinT.forEach(function(element) {element.textContent = MaxTOri });}
    else if(grado === "Fahrenheit"){
        MaxT.forEach(function(element) {element.textContent = (parseInt(MaxTOri)*(9/5) + 32) + "°"});
        MinT.forEach(function(element) {element.textContent = (parseInt(MinTOri)*(9/5) + 32) + "°"});}
    else if(grado === "Kelvin"){
        MaxT.forEach(function(element) {element.textContent = (parseInt(MaxTOri) + 273.15 ) + "°"});
        MinT.forEach(function(element) {element.textContent = (parseInt(MinTOri) + 273.15 ) + "°"});}
}


// Eliminar coockie
function AcceptCoockie(){
    var contenedor = document.querySelector("#coockie");
    contenedor.remove();
}
