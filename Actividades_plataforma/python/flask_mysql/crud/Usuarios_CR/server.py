from flask import Flask, render_template, request, redirect, url_for
from user import User
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        new_user = User.create(first_name, last_name, email)  # Guarda el usuario creado en una variable
        if new_user:
            return redirect(url_for('users'))
        else:
            return "Error al crear el usuario"  # Maneja el caso de error al crear el usuario
    return render_template("newuser.html")

@app.route("/")
def index():
    return redirect(url_for('create_user'))

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)