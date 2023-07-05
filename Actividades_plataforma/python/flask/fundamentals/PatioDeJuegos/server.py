## Patio de juegos
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/<int:x>/<color>')
def play(x, color):
    return render_template("index.html", color=color, times=x)

if __name__ == "__main__":
    app.run(debug=True)


