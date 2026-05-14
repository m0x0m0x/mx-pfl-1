# -----------------------------------
#  sesh.py = Sessions and Secrets
# -----------------------------------

# --- Imports ---


from flask import Blueprint, render_template, session, make_response

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


@sesh_bp.route('/set-cookie')
def set_cookie():
    response =
