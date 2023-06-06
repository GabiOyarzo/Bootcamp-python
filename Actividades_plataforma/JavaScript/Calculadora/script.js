// Calculadora
// ----------------------------------------------
// Gabriela Oyarzo
// 29 de mayo de 2023
// ----------------------------------------------
var display = document.getElementById("display");
var num1 = '';
var num2 = '';
var operador = '';

function press(num) {
    num2 += num;
    display.innerText = num2;
}

function setOP(op) {
    display.innerText = op;
    operador = op;
    num1 = num2;
    num2 = '';
    
}
function clr() {
    num2.substring = '';
}

function calculate() {
    var resultado;
    switch (operador) {
        case '+':
            resultado = parseFloat(num1) + parseFloat(num2);
            break;
        case '-':
            resultado = parseFloat(num1) - parseFloat(num2);
            break;
        case '*':
            resultado = parseFloat(num1) * parseFloat(num2);
            break;
        case '/':
            resultado = parseFloat(num1) / parseFloat(num2);
            break;
        default:
            resultado = NaN; // Operador no válido
    }
    display.innerText = resultado;
    
}
