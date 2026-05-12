# -----------------------------------
#  Debugging Routes here
# -----------------------------------

# --- Imports ---

import os

from flask import Blueprint, request

from limiter_config import limiter

debug_bp = Blueprint('debug', __name__)

# -- Routes ---

# 1 - Basic debug route


@debug_bp.route('/debug')
@limiter.limit("2 per hour")
def debug():
    return {"status": "debug route working", "timestamp": "2026-05-12"}


# 2 - Check Redis configuration (NO sensitive data)
@debug_bp.route('/debug/check-redis')
@limiter.limit("2 per hour")
def check_redis():
    redis_url = os.getenv("REDIS_URL")

    return {
        "redis_configured": bool(redis_url and redis_url.startswith("rediss://")),
        "rate_limiting": "active",
        "environment": os.getenv("VERCEL_ENV", "development"),
        "tip": "Redis is configured and rate limiting is working"
    }


# 3 - Test Redis connection (simple)
@debug_bp.route('/debug/test-redis')
@limiter.limit("2 per hour")
def test_redis():
    import redis

    redis_url = os.getenv("REDIS_URL")

    if not redis_url:
        return {"error": "Redis not configured"}, 500

    if not redis_url.startswith("rediss://"):
        return {"error": "Invalid Redis configuration"}, 500

    try:
        r = redis.Redis.from_url(redis_url)
        r.ping()

        return {
            "success": True,
            "message": "Redis connection successful",
            "rate_limiting": "operational"
        }
    except Exception as e:
        return {
            "success": False,
            "error": "Redis connection failed",
            "message": str(e)
        }, 500


# 4 - Get your IP address (user-only, not stored in response)
@debug_bp.route('/debug/my-ip')
@limiter.limit("5 per minute")
def my_ip():
    # Get real IP behind proxy
    real_ip = request.headers.get(
        'X-Forwarded-For', 'unknown').split(',')[0].strip()

    return {
        "your_ip": real_ip,
        "message": "This IP is used for rate limiting"
    }


# 5 - Simple health check (public)
@debug_bp.route('/debug/health')
def health():
    return {
        "status": "healthy",
        "service": "api",
        "rate_limiting": "enabled"
    }


# 6 - Rate limit status for current user
@debug_bp.route('/debug/my-limits')
def my_limits():
    """Returns current rate limit headers information"""
    return {
        "message": "Check response headers for rate limit info",
        "headers_to_check": [
            "X-RateLimit-Limit",
            "X-RateLimit-Remaining",
            "X-RateLimit-Reset"
        ]
    }
