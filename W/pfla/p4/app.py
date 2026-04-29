# -----------------------------
# V4 - Testing forms and post messages to endpoint
# Note - This project will also be organized
# -----------------------------

# -- Imports ---
from flask import Flask

from routes import bp  # Import the blueprint

# --- App Execution ---
app = Flask(__name__)
# Register the blueprint
app.register_blueprint(bp)

# --- logic ---

# --- init ---
if __name__ == '__main__':
    app.run(debug=True)
