# -----------------------------------
#  sesh.py = Sessions and Secrets
# -----------------------------------

# --- Imports ---

from flask import Blueprint

from limiter_config import limiter

sesh_bp = Blueprint('sesh', __name__)

# -- Routes ---

# 1 - Route for ensuring its working


@sesh_bp.route('/sesh_tezt')
def tezt():
    return "Sessions Test"


@sesh_bp.route("/sesh_tezt_api")
@limiter.limit("1 per minute")  # Stricter limit just for this API
def api():
    return "This endpoint is limited to 1 call per minute."

# Route or rendering the bootstrap
