# -----------------------------------
#  Debugging Routes here
# -----------------------------------

# --- Imports ---

import os

from flask import Blueprint

from limiter_config import limiter

debug_bp = Blueprint('debug', __name__)

# -- Routes ---

# 1 - Basic debug route


@debug_bp.route('/debug')
@limiter.limit("2 per hour")
def debug():
    return "Debug route is working"


# 2 - Check Redis configuration
@debug_bp.route('/debug/check-redis')
@limiter.limit("2 per hour")
def check_redis():
    from limiter_config import storage_uri

    # Get Redis URL
    redis_url = os.getenv("REDIS_URL")

    return {
        "storage_uri": str(storage_uri)[:50] + "..." if storage_uri else "None",
        "using_redis": storage_uri and storage_uri.startswith("rediss://"),
        "redis_url_exists": bool(redis_url),
        "redis_url_format": "✅ correct" if (redis_url and redis_url.startswith("rediss://")) else "❌ wrong or missing",
        "vercel_env": os.getenv("VERCEL", "not set"),
        "tip": "Set REDIS_URL with rediss:// format for production Redis"
    }


# 3 - Test Redis connection (simple)
@debug_bp.route('/debug/test-redis')
@limiter.limit("2 per hour")
def test_redis():
    import redis

    redis_url = os.getenv("REDIS_URL")

    if not redis_url:
        return {"error": "REDIS_URL environment variable not set"}

    if not redis_url.startswith("rediss://"):
        return {"error": "REDIS_URL must start with rediss://"}

    try:
        # Try to connect
        r = redis.Redis.from_url(redis_url)
        r.ping()  # Test connection

        return {
            "success": True,
            "message": "✅ Redis is working!",
            "host": redis_url.split('@')[1].split(':')[0] if '@' in redis_url else "unknown"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "tip": "Check if REDIS_URL is correct and Upstash database is active"
        }


@debug_bp.route('/debug/my-ip')
def my_ip():
    from flask import request

    # Get IP from different sources
    real_ip = request.headers.get(
        'X-Forwarded-For', 'not set').split(',')[0].strip()
    remote_addr = request.remote_addr

    return {
        "your_real_ip": real_ip,
        "remote_addr (what you see now)": remote_addr,
        "all_headers": {
            "X-Forwarded-For": request.headers.get('X-Forwarded-For'),
            "X-Real-IP": request.headers.get('X-Real-IP'),
        },
        "explanation": "Vercel proxies make requests appear from 127.0.0.1, but X-Forwarded-For has the real IP"
    }
