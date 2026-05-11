# -----------------------------------
#  Routes here for various types if tests
# -----------------------------------

# --- Imports ---

from flask import Blueprint

from limiter_config import limiter

tezt_bp = Blueprint('tezt', __name__)

# -- Routes ---

# 1 - Route for ensuring its working


@tezt_bp.route('/tezt')
def tezt():
    return "Route of Smell Panty"


@tezt_bp.route("/tezt_api")
@limiter.limit("1 per minute")  # Stricter limit just for this API
def api():
    return "This endpoint is limited to 1 call per minute."
