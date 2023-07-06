# Encuesta Dojo
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para firmar las sesiones

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    nombre = request.form['nombre']
    dojo_location = request.form['dojo_location']
    favorite_language = request.form['favorite_language']
    comment = request.form['comment']
    session['nombre'] = nombre
    session['dojo_location'] = dojo_location
    session['favorite_language'] = favorite_language
    session['comment'] = comment
    return redirect(url_for('result'))

@app.route('/result')
def result():
    nombre = session.get('nombre')
    dojo_location = session.get('dojo_location')
    favorite_language = session.get('favorite_language')
    comment = session.get('comment')

    return render_template('result.html', nombre=nombre, dojo_location=dojo_location, favorite_language=favorite_language, comment=comment)
if __name__ == '__main__':
    app.run(debug=True)
