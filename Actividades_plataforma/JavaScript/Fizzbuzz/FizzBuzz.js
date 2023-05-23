// Fizzbuzz
// --------------------------------------------
// Gabriela Oyarzo Escudero
// Última actualización: 23 de mayo de 2023
// --------------------------------------------

for(let i = 1; i<=100;i++){
    // múltiplos de 3 y 5 --> FizzBuzz
    if(i%5 == 0 && i%3 == 0){
        console.log("FizzBuzz");
    }
    // multiplos de 3 --> Fizz
    else if(i%3 == 0){
    console.log("Fizz");
    }
    // múltiplos de 5 --> Buzz
    else if(i%5 == 0){
    console.log("Buzz");
    }
    else if(i%5 !== 0 && i%3 !== 0){
    console.log(i);
    }
}
