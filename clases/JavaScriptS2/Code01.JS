// Código basado en la primera parte de la plataforma de JavaScript
// Author: Gabriela Oyarzo
// última actualización: 23 de mayo de 2023
// ----------------------------------------------------------
// --------------- Condicionales---------------

// booleanos --> lógicos
var estáSoleado = true;
var estáLloviendo = false;

var number = 5;
console.log(number < 3); // esto imprimirá `false`

// los arreglos lógicos o booleanos aparecen tanto por una afirmación como por una comparación.

// ejemplo sol/lluvia

var estáSoleado = false;
var estáLloviendo = true;
    
if(estáSoleado) {
    console.log("Ocupa bloqueador");
}
    
if(estáLloviendo) {
    console.log("Lleva paraguas");
}

if(estáSoleado == true) {
    console.log("Además, utiliza un gorro");
}


// ejemplo lunes: odio o no

var today = new Date();
if(today.getDay() == 1) {
    console.log("Odio los lunes");
}
    
if(today.getDay() != 1) {
    console.log("¡Hoy está bien!");
}

// ejemplo transcrito con elseif

var today = new Date();
if(today.getDay() == 1) {
    console.log("Odio los lunes");
} else if(today.getDay() == 5) {
    console.log("Viernes? ¡Más bien bien-res!");
} else {
    console.log("¡Hoy está bien!");
}


// ejemplo condiones múltiples

var temperature = 60; // supongamos que son grados Fahrenheit
var estáLloviendo = false;
    
if(temperature >= 50) {
    if(!estáLloviendo) {
        console.log("¡Este es un buen día para dar un paseo!");
    }
}

// versión acortada, mezclando condicionantes

var temperature = 60; // supongamos que son grados Fahrenheit
var estáLloviendo = false;
    
if(temperature >= 50 && !lloviendo) {
    console.log("¡Este es un buen día para dar un paseo!");
}

// Operadores de módulo

var es5par = 5 % 2 == 0;
var es500par = 500 % 2 == 0;
    
console.log(es5Par);   // false
console.log(es500Par); // true

// aplicando modulo con otros valores
var es78DivisiblePor3 = 78 % 3 == 0;
console.log(es78DivisiblePor3); // true



