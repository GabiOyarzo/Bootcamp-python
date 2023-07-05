from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

# Localhost:5000/: haz que diga "¡Hola Mundo!"
@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'

# Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')
def dojo():
    return '¡Dojo!'

# Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:

# localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
# localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!"
# localhost:5000/say/john: haz que diga "¡Hola, John!"

@app.route('/say/<name>')
def say(name):
    if isinstance(name,str):
        print(name)
        return "¡Hola, " + name +"!"

# Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):

# localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
# localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
# localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces

@app.route('/repeat/<int:num>/<palabra>')
def repeat(num, palabra):
    if isinstance(palabra,str) & isinstance(num,int):
        vector = [palabra] * num
        resultado = " ".join(vector)
        print(resultado)
        return resultado
    

@app.route('/<path:ruta>')
def cualquiera(ruta):
        return "¡Lo siento! No hay respuesta. Inténtalo otra vez."


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración