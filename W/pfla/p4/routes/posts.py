# -----------------------------------
# This file has routes of posts - was made for testing the project structure for multiple files
# -----------------------------------

from flask import Blueprint, render_template

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts')
def posts():
    return render_template('posts.html')
