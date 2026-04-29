from flask import render_template

from routes import bp


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/other')
def other():
    return render_template('other.html')
