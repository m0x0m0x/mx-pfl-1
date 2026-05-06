from flask import make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def custom_429_response(request_limit):
    # request_limit contains info about the specific limit that was hit
    html = f'''
    <html>
    <body style="background:black; color:red; text-align:center; padding-top:20%">
        <h1 style="text-shadow:0 0 20px red">RATE LIMIT REACHED!</h1>
        <p>Limit: {request_limit.limit}</p>
        <img src="https://i.ibb.co/hxYyJHVv/image.png" width="300">
    </body>
    </html>
    '''
    return make_response(html, 429)


limiter = Limiter(
    get_remote_address,
    default_limits=["100 per day", "10 per hour", "5 per minute"],
    on_breach=custom_429_response  # Attach the handler here
)
