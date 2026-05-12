import os

from flask import make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def custom_429_response(request_limit):

    from flask import request
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(
        f"🔴 RATE LIMITED: {request.endpoint} from {ip} - Limit: {request_limit.limit}")

    """Custom HTML response when rate limit is exceeded"""
    html = f'''
    <html>
    <body style="background:black; color:red; text-align:center; padding-top:10%">
        <h1 style="text-shadow:0 0 20px red">⚠️ RATE LIMIT REACHED! ⚠️</h1>
        <p>You've exceeded the limit: <strong>{request_limit.limit}</strong></p>
        <p>Please slow down and try again later.</p>
        <img src="https://i.ibb.co/hxYyJHVv/image.png" width="800">
        <br><br>
        <button onclick="location.reload()" style="padding:10px 20px; background:red; color:white; border:none; cursor:pointer">
            Try Again
        </button>
    </body>
    </html>
    '''
    return make_response(html, 429)


# ============================================
# STORAGE CONFIGURATION
# ============================================

# Use Redis only if running on Vercel with credentials
redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

if redis_url and redis_token:
    # Production on Vercel
    host = redis_url.replace("https://", "").replace("http://", "").rstrip("/")
    storage_uri = f"rediss://default:{redis_token}@{host}:443"
    print("✅ [limiter_config] Using Upstash Redis (production mode)")
else:
    # Local development
    storage_uri = "memory://"
    print("✅ [limiter_config] Using in-memory storage (local mode)")


# ============================================
# FLASK-LIMITER INITIALIZATION
# ============================================

limiter = Limiter(
    get_remote_address,
    default_limits=["100 per day", "10 per hour", "5 per minute"],
    on_breach=custom_429_response,
    storage_uri=storage_uri,
    strategy="fixed-window",      # Best for serverless (Vercel)
    swallow_errors=True,           # Don't crash if Redis fails
    headers_enabled=True,          # Show X-RateLimit headers
)
