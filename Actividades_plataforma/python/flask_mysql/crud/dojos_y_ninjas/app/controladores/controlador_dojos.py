from flask import render_template, request, redirect
from app import app
from app.modelos.modelos_dojos import Dojo

@app.route('/dojos', methods=['GET'])
def obtener_dojos():
    lista_dojos = Dojo.obtener_todos()
    return render_template('dojos.html', lista_dojos=lista_dojos)

@app.route('/nuevo/dojo', methods=['POST'])
def crear_dojo():
    nuevo_dojo = {
        "nombre": request.form['nombre']
    }
    Dojo.crear_uno(nuevo_dojo)
    return redirect('/dojos')

@app.route('/dojo/<int:id>', methods=['GET'])
def obtener_dojo(id):
    data = {
        "id": id
    }
    informacion_dojo = Dojo.obtener_uno_con_ninjas(data)
    return render_template('dojo.html', informacion_dojo=informacion_dojo)    
