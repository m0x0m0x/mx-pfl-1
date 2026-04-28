# -------------------
# app.py - Testing flask api templates
# -------------------

# --- Imports ---
from flask import Flask, render_template
from flask_cors import CORS

# --- Main Code ---
app = Flask(__name__, template_folder='tempz')
CORS(app)

# --- Execution Function ---

# Index Ropute is rendering the file index.html from ./tempz folder


@app.route("/")
def index():
    myValue = 'Booty Smeller'  # Varaible Being Called in HTML
    myResult = 10 + 30  # Variable being called in HTML
    mylist = [10, 20, 30, 24]
    return render_template('index.html', myResult=myResult, myValue=myValue, mylist=mylist)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
