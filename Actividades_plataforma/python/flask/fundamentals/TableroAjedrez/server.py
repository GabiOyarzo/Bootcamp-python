## Tablero de ajedrez
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:nx>/<int:ny>/<color1>/<color2>')
def tablero(nx, ny, color1, color2):
    return render_template("index.html", color1=color1, color2=color2, nx=nx, ny=ny)

if __name__ == "__main__":
    app.run(debug=True)
