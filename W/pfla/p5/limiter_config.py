import os

from flask import make_response, request
from flask_limiter import Limiter


# Custom function to get REAL IP from Vercel
def get_real_ip():
    """Get the real client IP address behind Vercel's proxy"""
    # Vercel sets these headers in order of trust
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        # X-Forwarded-For can be a list: "client, proxy1, proxy2"
        # The first IP is the real client
        return forwarded.split(',')[0].strip()

    # Fallback to standard remote_addr
    return request.remote_addr or 'unknown'


def custom_429_response(request_limit):
    ip = get_real_ip()
    print(
        f"😡 RATE LIMITED: {request.endpoint} from {ip} - Limit: {request_limit.limit}")

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

# Use REDIS_URL (correct way)
storage_uri = os.getenv("REDIS_URL")

if storage_uri and storage_uri.startswith("rediss://"):
    print("✅ [limiter_config] Using Upstash Redis (production mode)")
else:
    storage_uri = "memory://"
    print("✅ [limiter_config] Using in-memory storage (local mode)")


# ============================================
# FLASK-LIMITER INITIALIZATION
# ============================================

limiter = Limiter(
    get_real_ip,  # 👈 Changed from get_remote_address to get_real_ip
    default_limits=["100 per day", "10 per hour", "5 per minute"],
    on_breach=custom_429_response,
    storage_uri=storage_uri,
    key_prefix="my-flask-app-mx-pfla-p5:",
    strategy="fixed-window",
    swallow_errors=True,
    headers_enabled=True,
)
