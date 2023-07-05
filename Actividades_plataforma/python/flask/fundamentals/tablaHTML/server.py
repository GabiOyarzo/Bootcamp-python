## Tabla
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lista')
def render_lists():
    # Nombre usuarios
    usuarios_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", estudiantes = usuarios_info)

# Con ruta erronea
@app.route('/<path:ruta>')
def cualquiera(ruta):
        return "¡Hey! Esta no es la ruta"

if __name__ == "__main__":
    app.run(debug=True)
