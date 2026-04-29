# -------------------
# app.py - Testing flask api templates
# -------------------

# --- Imports ---
import random

from flask import Flask, redirect, render_template, url_for
from flask_cors import CORS

# --- Main Code ---
app = Flask(__name__, template_folder='tempz')
CORS(app)

# --- Execution Function ---

# Index Ropute is rendering the file index.html from ./tempz folder


@app.route("/")
def index():
    # Variabeles for jinja templating
    myValue = 'Booty Smeller'  # Varaible Being Called in HTML
    myResult = 10 + 30  # Variable being called in HTML
    mylist = [10, 20, 30, 24]
    mylist2 = [random.randint(1, 100) for _ in range(10)]

    return render_template('index.html', myResult=myResult, myValue=myValue, mylist=mylist, mylist2=mylist2)

# i2 Route - tempz/i2.html - Testing base templating


@app.route("/i2")
def i2():
    # Variabeles for jinja templating
    myValue = 'Booty Smeller'  # Varaible Being Called in HTML
    myResult = 10 + 30  # Variable being called in HTML
    mylist = [10, 20, 30, 24]
    mylist2 = [random.randint(1, 100) for _ in range(10)]

    return render_template('i2.html', myResult=myResult, myValue=myValue, mylist=mylist, mylist2=mylist2)


# f1 - Filtering route - tempz/filter.html - Testing jinja filters

@app.route("/f1")
def filter1():
    some_text = "Sniff Her Ass"
    return render_template('filter.html', some_text=some_text)

# These are customn filters
# Reverse String


@app.template_filter('reverse_string')
def reverse_string(a):
    return a[::-1]

# Repeat Letters


@app.template_filter('repeat')
def repeat(b, times=2):
    return b * times

# Alternate Case


@app.template_filter('alt_case')
def alt_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

# Other endpoint


@app.route('/other')
def other():
    return render_template('other.html')


# Redirect


@app.route('/redirect_ep')
def redirectep():
    return redirect(url_for('other'))


# --- Main App Run ---
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
