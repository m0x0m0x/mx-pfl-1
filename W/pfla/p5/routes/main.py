# ---------------------------------------
# Main.py - Main routest all tested here
# ---------------------------------------

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return render_template('index.html')

# Add to any blueprint or directly in app.py


@main_bp.route('/debug/check-redis')
def check_redis():
    import os

    from limiter_config import storage_uri

    redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
    redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

    return {
        "storage_uri": storage_uri[:50] + "..." if storage_uri else None,
        "redis_url_exists": bool(redis_url),
        "redis_token_exists": bool(redis_token),
        "actually_using_redis": "rediss://" in storage_uri if storage_uri else False,
        "vercel_env": os.getenv("VERCEL", "not set")
    }
