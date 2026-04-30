from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return render_template('index.html')


@main_bp.route('/others')
def other():
    return render_template('other.html')
