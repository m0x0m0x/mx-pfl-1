# -----------------------------------
#  Routes here for various types if tests
# -----------------------------------

# --- Imports ---

from flask import Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

tezt_bp = Blueprint('tezt', __name__)

# -- Routes ---

# 1 - Route for ensuring its working


@tezt_bp.route('/tezt')
def tezt():
    return "Route of Smell Panty"


# 2 - Route for actual testing of the rate limit
limiter = Limiter(
    get_remote_address,  # Uses the visitor's IP address automatically
    # Global limits for all routes
    default_limits=["100 per day", "10 per hour"]
)


@tezt_bp.route("/")
def home():
    return "Welcome! You're being rate limited."


@tezt_bp.route("/api")
@limiter.limit("5 per minute")  # Stricter limit just for this API
def api():
    return "This endpoint is limited to 5 calls per minute."
