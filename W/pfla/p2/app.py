# ----------------------------
# Version 2 of flask app
# ----------------------------

# --- Imports ---
from flask import Flask

# --- Create App ---
app = Flask(__name__)

# --- Routes ---


# Index page
@app.route('/')
def index():
    return "<h1> Booty Dance Smill0 </h1>"


@app.route('/pusy')
def hello():
    return "<h2> Enjoy strong pussy stink</h2>"

# Handling Variables in URL - Url procesors


@app.route('/greet/<name>')
def greet(name):
    return f"<code></h1> Sup, {name}, My Niggaz </h1></code>"

# Route for adding two number


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<h2>{num1} + {num2} = {num1 + num2}</h2>"


# --- Run App ---
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
