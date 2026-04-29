from flask import render_template

from routes import bp  # Import the blueprint from __init__


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/about')
def about():
    return render_template('about.html')
