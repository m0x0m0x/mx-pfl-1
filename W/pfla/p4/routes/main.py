# ----------------------------------
# Routes here will be imported in __init__.py , which is being imported via blueprints into app.py
# ----------------------------------

# -- Imports ---
from flask import render_template

from routes import bp

# --- Routes ---


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/other')
def other():
    return render_template('other.html')
