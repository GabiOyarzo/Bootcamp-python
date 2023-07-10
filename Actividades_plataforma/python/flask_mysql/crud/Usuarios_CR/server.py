from flask import Flask, render_template, request, redirect, url_for
from user import User

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route("/create", methods=["POST"])
def create_user():
    data = {
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'] }
    User.save(data)
    return render_template('users.html',users=User)

@app.route("/")
def index():
    return redirect('/create')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
