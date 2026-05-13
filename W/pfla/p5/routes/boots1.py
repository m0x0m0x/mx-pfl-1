# -----------------------------------
#  boots1.py - Routes for testing Boostrap
# -----------------------------------

# --- Imports ---

from flask import Blueprint, render_template

from limiter_config import limiter

boots1_bp = Blueprint('boots1', __name__)

# -- Routes ---

# 1 - Route for ensuring its working


@boots1_bp.route('/bptezt')
def tezt():
    return "Route of Smell Panty Boots1"


@boots1_bp.route("/bp_tezt_api")
@limiter.limit("1 per minute")  # Stricter limit just for this API
def api():
    return "This endpoint is limited to 1 call per minute."

# Route or rendering the bootstrap


@boots1_bp.route('/bpb1')
def bpb1():
    return render_template('bp1.html')
