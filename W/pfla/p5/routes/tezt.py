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


@tezt_bp.route("/tezt_api2")
@limiter.limit("1 per minute")
def api2():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: black;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
            }
            .glow-text {
                color: red;
                font-size: 3rem;
                text-align: center;
                text-shadow: 
                    0 0 10px red,
                    0 0 20px red,
                    0 0 30px red,
                    0 0 40px darkred;
                animation: pulse 1.5s ease-in-out infinite;
            }
            @keyframes pulse {
                0%, 100% {
                    text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red;
                }
                50% {
                    text-shadow: 0 0 20px red, 0 0 40px red, 0 0 60px darkred;
                }
            }
        </style>
    </head>
    <body>
        <div class="glow-text">⚠️ RATE LIMITED ⚠️<br>1 CALL PER MINUTE</div>
    </body>
    </html>
    '''
