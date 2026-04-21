# ----------------------------
# Version 2 of flask app
# ----------------------------

# --- Imports ---
from flask import Flask, request

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

# Route for Math
# Note the type casting which is being specified in the URL itself this could have also been done seperately


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<h2>{num1} + {num2} = {num1 + num2}</h2>"


@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1, num2):
    return f"<h2>{num1} ** {num2} = {num1 ** num2}</h2>"

# Handling url params


@app.route('/handle_url_params')
def handle_params():
    return str(request.args)

# IF-else statement adds error handling


@app.route('/handle_url_params2')
def handle_params2():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'<h2>{greeting}, {name}!</h2>'
    else:
        return '<h2 align="center">Missing required parameters</h2>'


    # --- Run App ---
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
