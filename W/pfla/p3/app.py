# -------------------
# app.py - Testing flask api templates
# -------------------

# --- Imports ---
from flask import Flask
from flask_cors import CORS

# --- Main Code ---
app = Flask(__name__)
CORS(app)

# --- Execution Function ---


@app.route("/")
def index():
    return "Booty Scents"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
