# limiter_config.py
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create limiter here - no app yet
limiter = Limiter(
    get_remote_address,
    default_limits=["100 per day", "10 per hour", "1 per minute"]
)
