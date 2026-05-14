# -----------------------------------
#  sesh.py = Sessions and Secrets
# -----------------------------------

# --- Imports ---


from flask import Blueprint, flash, make_response, render_template, request, session

from limiter_config import limiter

sesh_bp = Blueprint('sesh', __name__, url_prefix='/session')


# -- Routes ---

# 1 - Route for ensuring its working


@sesh_bp.route('/sesh_tezt')
def tezt():
    return (render_template('sesh.html', message='Session Test Shit'))


@sesh_bp.route("/sesh_tezt_api")
@limiter.limit("1 per minute")  # Stricter limit just for this API
def api():
    return "This endpoint is limited to 1 call per minute."


# Testing out sessions stting

@sesh_bp.route('/set-data')
def set_data():
    session['name'] = 'Busra'
    session['Fetish'] = 'Fart'
    flash('Session data has been set successfully!', 'success')
    return (render_template('sesh.html', message='Session Data Set from /set-data'))


# Get the data
@sesh_bp.route('/get-data')
def get_data():
    if 'name' in session.keys() and 'Fetish' in session.keys():
        name = session['name']
        other = session['Fetish']
        return (render_template('sesh.html', message=f'Name: {name}, love Fetish: {other}'))
    else:
        return (render_template('sesh.html', message='Session Data Not Found'))

# Clearing the data


@sesh_bp.route('/clear-session')
def clear_session():
    session.clear()
    return (render_template('sesh.html', message='Session Raped'))

# -- Cookie Tests here ---


# Setting Cookie
@sesh_bp.route('/set-cookie')
def set_cookie():
    response = make_response(render_template(
        'sesh.html', message='CookeInherAss'))
    response.set_cookie('cookie_ass_name', 'cookie_pussy_value')
    return response

# Getting Cookie


@sesh_bp.route('/get-cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_ass_name']
    return (render_template('sesh.html', message=f'Cookie Value: {cookie_value}'))

# Remove Cookies


@sesh_bp.route('/remove-cookie')
def remove_cookie():
    response = make_response(render_template(
        'sesh.html', message='Cookie Removed'))
    response.set_cookie('cookie_ass_name', '', expires=0)
    return response

# Create Login Page


@sesh_bp.route('/sesh-login')
def sesh_login():
    return render_template('sesh_login.html')
