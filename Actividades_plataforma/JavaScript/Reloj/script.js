function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
      new Date().getMinutes() * 60 + 
      new Date().getHours() * 3600;
}

var min  = 0;
var hour = 0;
setInterval( function() {
    var time = getSecondsSinceStartOfDay();
    console.log(time);
    // your code here
    
}, 1000);





//En otro desafío, intenta usar lo que hemos aprendido para 
// hacer un reloj con manecillas móviles. Similar a setTimeout(), 
// que hemos usado para crear un retraso. También podemos usar 
// setInterval() para ejecutar alguna función cada período de tiempo. 
// En el caso de nuestro reloj, queremos que se actualice cada 1000 milliseconds.
