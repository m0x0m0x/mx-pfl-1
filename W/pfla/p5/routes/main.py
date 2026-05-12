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

    # Get raw env vars
    redis_url_raw = os.getenv("UPSTASH_REDIS_REST_URL")
    redis_token_raw = os.getenv("UPSTASH_REDIS_REST_TOKEN")

    # Check what the actual strings are
    return {
        "storage_uri": storage_uri[:100] if storage_uri else "None",
        "redis_url_raw_type": type(redis_url_raw).__name__,
        "redis_url_raw_value": redis_url_raw[:20] if redis_url_raw else "None",
        "redis_url_exists": bool(redis_url_raw),
        "redis_url_length": len(redis_url_raw) if redis_url_raw else 0,
        "redis_token_exists": bool(redis_token_raw),
        "vercel_env": os.getenv("VERCEL", "not set"),
        "all_env_vars": {k: v[:20] if v and len(v) > 20 else v for k, v in os.environ.items()
                         if 'UPSTASH' in k or 'REDIS' in k}  # Show all Redis-related env vars
    }
