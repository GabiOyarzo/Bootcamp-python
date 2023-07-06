# Contador
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para firmar las sesiones

@app.route('/')
def index():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 0
    if 'contador' in session:
        contador = session['contador']
    else:
        contador = 0
    return render_template("index.html", visitas=session['visitas'], contador=contador)

@app.route('/incrementar/<int:num>')
def incrementar(num):
    if 'contador' in session:
        session['contador'] += num
    else:
        session['contador'] = num
    return redirect(url_for('index'))

@app.route('/resetear')
def resetear():
    if 'contador' in session:
        session['contador'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)