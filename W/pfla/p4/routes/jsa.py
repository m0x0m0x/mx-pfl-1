# -----------------------------------
# This has functions for sending JS via button click
# -----------------------------------


from flask import Blueprint, render_template

jsa_bp = Blueprint('jsa', __name__)

# Standard Route Entry Point


@jsa_bp.route('/jsa1')
def jsa1():
    return render_template('jsa.html')

# JS Wil go in here
