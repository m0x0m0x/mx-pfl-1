# -------------------
# app.py - Testing flask api templates
# -------------------

# --- Imports ---
from flask import Flask

# --- Main Code ---
app = Flask(__name__)

# --- Execution Function ---


@app.route("/")
def index():
    return "Booty Scents"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
