// Ejemplos plataforma:


// Lección 1: predecir resultado
var a = 25;
a = a - 13;
console.log(a / 2);
//--> el resultado es: 6

a = "hola";
console.log(a + " hola");
//--> el resultado es: hola hola

// Lección 2: predice los bucles
for (var i = 0; i < 10; i++) {
    console.log(i);
    i = i + 3; // le suma 3 a i, pero el bucle mismo también le agrega 1. 
}

console.log("fuera del bucle " + i);
//--> el resultado es: 0 4 8 y fuera del bucle 12

// Lección 3 : predice lo que hace el código
function getTotal(arrayOfNumbers) {
    var sum = arrayOfNumbers[0];
    for (var i = 0; i < arrayOfNumbers.length; i++) {
        sum += arrayOfNumbers[i];
        console.log("la suma actual es: " + sum);
        // La suma actual es: (i=0) --> sum(1) + 1 --> 2
        // La suma actual es: (i=0) --> sum(2) + 3 --> 5
        // La suma actual es: (i=0) --> sum(5) + 5 --> 10
    }
    console.log("el total es: " + sum);
    // La suma actual es: (i=0) --> sum(5) + 5 --> 10

}
getTotal([1, 3, 5]);
//--> el resultado es: 10


// ----------------------------------------------------------------------
// Siempre está Soleado
// ----------------------------------------------------------------------
var estáSoleado = true;
var temperatura = 45; // supongamos que son grados Fahrenheit
var estáLloviendo = false;
var quéLlevar = "Debería llevar: ";

if (estáSoleado) {
    quéLlevar += "gafas, ";
}
if (temperatura < 50) {
    quéLlevar += "un abrigo, ";
}
if (estáLloviendo) {
    quéLlevar += "un paraguas, ";
}
quéLlevar += "y una sonrisa!";

console.log(quéLlevar);
// --> Denería llevar: gafas (soleado: true), un abrigo (t°<50°F) y una sonrisa!


// ----------------------------------------------------------------------
// Prepárate para la cuenta regresiva
// ----------------------------------------------------------------------
for (var i = 10; i > 0; i--) {
    if (i != 2) {
        console.log(i);
    } else {
        console.log("ignición!");
    }
}

console.log("despegue!");
// Console: 10,9,8,7,6,5,4,3,ignición!,1,Despegue!

// ----------------------------------------------------------------------
// Contar positivos
// ----------------------------------------------------------------------
var contarPositivos = 0;
var números = [3, 4, -2, 7, 16, -8, 0];
    
// tu código aquí
for(var i = 0; i < números.length;i++){
    if(números[i]%2 == 0){
        contarPositivos ++;
    }
} 
    
console.log("hay " + contarPositivos + " valores positivos");


