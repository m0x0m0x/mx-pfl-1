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


@posts_bp.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    table_html = None  # 👈 New variable for the table

    if request.method == 'POST':
        file = request.files.get('file')

        if not file or file.filename == '':
            return render_template('fup.html', message="⚠️ No file selected")

        if file.content_type == 'text/csv':
            df = pd.read_csv(file.stream)
            # 👈 Generate table HTML
            table_html = df.to_html(classes='dataframe', index=False)
            message = f"✅ Loaded {len(df)} rows"

        elif file.content_type == 'text/plain':
            content = file.read().decode('utf-8')
            print(content)
            message = f"✅ Text file: {len(content)} chars"

    # 👇 Pass both message AND table_html to template
    return render_template('fup.html', message=message, table_html=table_html)
