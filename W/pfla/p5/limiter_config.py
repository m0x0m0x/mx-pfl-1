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
# STORAGE CONFIGURATION - FIXED FOR REDIS:// URL
# ============================================

# Use the CORRECT Redis connection string (not REST API)
storage_uri = os.getenv("REDIS_URL")  # 👈 Changed to REDIS_URL

if storage_uri and storage_uri.startswith("rediss://"):
    # ✅ Production on Vercel with correct Redis URL
    print("✅ [limiter_config] Using Upstash Redis (production mode)")
    # Extract host for logging (hide password)
    host = storage_uri.split(
        '@')[1].split(':')[0] if '@' in storage_uri else "unknown"
    print(f"   Connected to: {host}")
else:
    # 🧪 Local development or missing Redis URL
    storage_uri = "memory://"
    print("✅ [limiter_config] Using in-memory storage (local mode)")
    print("   Set REDIS_URL environment variable for persistent rate limiting")


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
