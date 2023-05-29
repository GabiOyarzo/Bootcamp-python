// Javascript actividad: DojoWeather

// Cambio de ciudad
function ChangeCity(name){
    var city = document.querySelector(name)
    alert('Loading weather report to '+ city.innerText)
}

var MaxTOri = null; // Variable para guardar el contenido original
var MinTOri = null; // Variable para guardar el contenido original

// Cambio de unidad
function ConvertTemperature(grado, maxT, minT) {
    var maxTElements = document.querySelectorAll(maxT);
    var minTElements = document.querySelectorAll(minT);

    // Verificar si los valores originales ya han sido guardados
    if (MaxTOri === null && MinTOri === null) {
        MaxTOri = maxTElements[0].textContent;
        MinTOri = minTElements[0].textContent;
    }
    if (grado === "Celsius") {
            maxTElements.forEach(function(element) {
            element.textContent = MaxTOri;
        });
            minTElements.forEach(function(element) {
            element.textContent = MinTOri;
        });
    } else if (grado === "Fahrenheit") {
        var farMax = (parseInt(MaxTOri) * (9/5)) + 32;
        var farMin = (parseInt(MinTOri) * (9/5)) + 32;
            maxTElements.forEach(function(element) {
            element.textContent = farMax + "°";
        });
            minTElements.forEach(function(element) {
            element.textContent = farMin + "°";
        });
    } else if (grado === "Kelvin") {
        var kelMax = parseInt(MaxTOri) + 273.15;
        var kelMin = parseInt(MinTOri) + 273.15;
            maxTElements.forEach(function(element) {
            element.textContent = kelMax + "°";
        });
        minTElements.forEach(function(element) {
            element.textContent = kelMin + "°";
        });
    }
}

// Eliminar coockie
function AcceptCoockie(){
    var contenedor = document.querySelector("#coockie");
    contenedor.remove();
}
