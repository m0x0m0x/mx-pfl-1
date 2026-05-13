# -----------------------------
# V4 - Testing forms and post messages to endpoint
# Note - This project will also be organized
# -----------------------------

# --- Imports---
import secrets

from flask import Flask

# IMPORTANT: Import limiter BEFORE blueprints that use it
from limiter_config import limiter
from routes import boots1_bp, debug_bp, main_bp, sesh_bp, tezt_bp

# --- Setup Flask App ---
app = Flask(__name__, template_folder='tempz')
app.secret_key = secrets.token_hex(16)

# --- Initialize Limiter FIRST (before blueprints) ---
limiter.init_app(app)  # 👈 Moved BEFORE blueprint registration

# --- Custom Headers ---


@app.after_request
def add_custom_headers(response):
    # Simple header message (always works, doesn't break content)
    response.headers['X-Greeting'] = 'Smell her Farts'
    response.headers['X-Rape-Kill'] = 'Lick Asss and pussy'
    return response


# --- Register Blueprints (after limiter init) ---
app.register_blueprint(main_bp)
app.register_blueprint(tezt_bp)
app.register_blueprint(debug_bp)
app.register_blueprint(boots1_bp)
app.register_blueprint(sesh_bp)

# --- init ---
if __name__ == '__main__':
    print("\n📌 Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"  → {rule.endpoint}: {rule}")
    app.run(debug=True)
