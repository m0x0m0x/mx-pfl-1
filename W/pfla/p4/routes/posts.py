# -----------------------------------
# This file has routes of posts - was made for testing the project structure for multiple files
# -----------------------------------

from flask import Blueprint, flash, render_template, request

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts')
def posts():
    return render_template('posts.html')

# Route for Doing posts -
# Note this form functin is for f1.html - Note the POST is to this function located as posts.f1


@posts_bp.route('/f1', methods=['GET', 'POST'])
def f1():
    if request.method == 'GET':
        return render_template('f1.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'pantysmeller' and password == 'sniff':
            return flash('Login Successful! , Welcome Stink Lover!')
        else:
            return flash('Login Failed! , Fuckk Off')

    return render_template('f1.html')
