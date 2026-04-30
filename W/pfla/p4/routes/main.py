# ---------------------------------------
# Main.py - Main routest all tested here
# ---------------------------------------

from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return render_template('index.html')


@main_bp.route('/others')
def other():
    return render_template('other.html')


# Route for Doing posts
@main_bp.route('/f1', methods=['GET', 'POST'])
def f1():
    if request.method == 'GET':
        return render_template('f1.html')
    elif request.method == 'POST':
        return ""

    return render_template('f1.html')
