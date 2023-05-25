// Pizza dojo
// Gabriela Oyarzo
// última actualizacion: 25 de mayo de 2023

console.log('Se cambió el termino salsa por ingredientes')

function pizzaOven(tipoCorteza,tipoSalsa,quesos,ingredientes){
    var pizza = {};
    pizza.tipoCorteza = tipoCorteza;
    pizza.tipoSalsa = tipoSalsa;
    pizza.quesos = quesos;
    pizza.ingredientes = ingredientes;
    return pizza;
}

var pizza1 = pizzaOven("estilo Chicago","tradicional","mozzarella",["pepperoni","salchicha"]);
console.log(pizza1);

var pizza2 = pizzaOven("lanzada a mano","marinara",["mozzarella", "feta"],["champiñones", "aceitunas", "cebollas"]);
console.log(pizza2);

var pizza3 = pizzaOven("romana","picante","mantecoso",["carne","cebolla caramelizada","pimenton"]);
console.log(pizza3);

var pizza4 = pizzaOven("napolitana","BBQ","parmesano",["choclo", "aceitunas", "tomate"]);
console.log(pizza4);