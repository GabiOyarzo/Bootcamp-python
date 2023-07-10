from flask import render_template, redirect, request
from dojos_y_ninjas_app import app
from dojos_y_ninjas_app.modelos import dojo, ninja

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninja.html',dojos= dojo.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')