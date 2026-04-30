# -----------------------------------
# This file has routes of posts - was made for testing the project structure for multiple files
# -----------------------------------

from flask import Blueprint, render_template, request

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts')
def posts():
    return render_template('posts.html')

# Route for Doing posts -
# Note this form functin is for f1.html - Note the POST is to this function located as posts.f1


@posts_bp.route('/f1', methods=['GET', 'POST'])
def f1():
    message = None  # Simple variable instead of flash

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'pantysmeller' and password == 'sniff':
            message = 'Login Successful! Welcome Stink Lover!'
        else:
            message = 'FuckOff Bastards.'

    return render_template('f1.html', message=message)
