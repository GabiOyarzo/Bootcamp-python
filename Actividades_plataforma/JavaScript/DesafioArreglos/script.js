// Desafio arreglos
// Gabriela Oyarzo
// Fecha: 25 de mayo de 2023
// --------------------------------------------------------------------------------------------
// 1.- Siempre hambriento
// --------------------------------------------------------------------------------------------
function alwaysHungry(arr) {
    var x = []; 
    for(var aux1 = 0; arr.length > aux1; aux1++){
        if(arr[aux1] == "comida"){
            x.push("delicioso");
        }
    }
    if(x.length > 0){
        console.log(x)
    } else{
        console.log("Tengo Hambre")
    }
}
alwaysHungry([3.14, "comida", "pastel", true, "comida"]);
alwaysHungry([4, 1, 5, 7, 2]);
// --------------------------------------------------------------------------------------------
// 2.- Filtro paso alto
// --------------------------------------------------------------------------------------------
function highPass(arr, cutoff) {
    var filteredArr = [];
    // tu código aquí
    for(var aux1 = 0; aux1 < arr.length; aux1++){
        if(arr[aux1] > cutoff){
            filteredArr.push(arr[aux1]);
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); 

// 3.- Mejor que el promedio
function betterThanAverage(arr) {
    var sum = 0;
    for(var x = 0; x < arr.length; x++){
        sum = sum + arr[x];
    }
    var avg = (sum/(arr.length));
    var count = 0;
    for(var x = 0; x < arr.length; x++){
        if(arr[x] > avg){
            count++
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);

// 4.- Arreglo invertido

function reverse(arr) {
    // tu código aquí
    var arr1 = [];
    for(var i = arr.length-1; i >= 0; i--){
        arr1.push(arr[i]);
    }
    return arr1;
}  
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); 

// 5.- Arreglo de Fibonacci

function fibonacciArray(n) {
    var fibArr = [0 , 1];
    for(var i = 1; i < n; i++ ){
        if(i > 1){
            fibArr[i] = fibArr[i-1] + fibArr[i-2];
        }
    }
    return fibArr;
}
var result = fibonacciArray(10);
console.log(result); 
