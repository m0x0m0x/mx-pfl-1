# ----------------------------
# Version 2 of flask app
# ----------------------------

# --- Imports ---
from flask import Flask

# --- Create App ---
app = Flask(__name__)

# --- Routes ---


@app.route('/')
def home():
    return "<h1> Booty Dance Smill0 </h1>"


# --- Run App ---
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
