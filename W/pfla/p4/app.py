# -----------------------------
# V4 - Testing forms and post messages to endpoint
# Note - This project will also be organized
# -----------------------------

# --- Imports---
import secrets

from flask import Flask

from routes import main_bp, posts_bp

# --- Setup Flask App ---
app = Flask(__name__, template_folder='tempz')
app.secret_key = secrets.token_hex(16)

# --- Custom Headers ---
# Custom headers are for info for features requires seperate implementation


@app.after_request
def add_custom_headers(response):
    # Simple header message (always works, doesn't break content)
    response.headers['X-Greeting'] = 'Smell her Farts'
    response.headers['X-Rape-Kill'] = 'Lick Asss and pussy'
    return response


# --- Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(posts_bp)


# --- init ---
if __name__ == '__main__':
    print("\n📌 Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"  → {rule.endpoint}: {rule}")
    app.run(debug=True)
