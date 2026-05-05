# -----------------------------------
# This file has routes of posts - was made for testing the project structure for multiple files
# -----------------------------------

import pandas as pd
from flask import Blueprint, render_template, request

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts')
def posts():
    return render_template('posts.html')

# Route for Doing posts -
# Note this form functin is for f1.html - Note the POST is to this function located as posts.f1
# Fiel types are restricted in fup.html - Where we define the explicit files that can be uploaded


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

# Uploading Files
# This code will check if any file is upploaded and then display a df or text content based on file type
# The file types are restricted -


@posts_bp.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    table_html = None
    text_content = None  # 👈 New variable for text files
    message = None

    if request.method == 'POST':
        file = request.files.get('file')

        if not file or file.filename == '':
            message = "⚠️ No file selected"
        elif file.content_type == 'text/csv':
            df = pd.read_csv(file.stream)
            table_html = df.to_html(index=False)
            message = f"✅ Loaded {len(df)} rows"
        elif file.content_type == 'text/plain':
            text_content = file.read().decode('utf-8')
            message = f"✅ Text file: {len(text_content)} chars"

    return render_template('fup.html',
                           message=message,
                           table_html=table_html,
                           text_content=text_content)
