# ----------------------------
# Version 2 of flask app
# ----------------------------

# --- Imports ---
import requests
from flask import Flask, Response, redirect, request

# --- Create App ---
app = Flask(__name__)

# --- Routes ---


# Index page
@app.route('/')
def index():
    return "<h1> Booty Dance Smill0 </h1>"


@app.route('/pusy')
def hello():
    return "<h2> Enjoy strong pussy stink</h2>"

# Handling Variables in URL - Url procesors


@app.route('/greet/<name>')
def greet(name):
    return f"<code></h1> Sup, {name}, My Niggaz </h1></code>"

# Route for Math
# Note the type casting which is being specified in the URL itself this could have also been done seperately


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<h2>{num1} + {num2} = {num1 + num2}</h2>"


@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1, num2):
    return f"<h2>{num1} ** {num2} = {num1 ** num2}</h2>"

# Handling url params


@app.route('/handle_url_params')
def handle_params():
    return str(request.args)

# IF-else statement adds error handling


@app.route('/handle_url_params2')
def handle_params2():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'<h2>{greeting}, {name}!</h2>'
    else:
        return '<h2 align="center">Missing required parameters</h2>'


# Making a post request on hello endpoint
@app.route('/hello', methods=['POST'])
def hellopost():
    return "<code> bootyFarted </code>"

# Making the same route with GET and POST


@app.route('/hellopg', methods=['GET', 'POST', 'PUT'])
def hellopg():
    if request.method == 'GET':
        return '<h3> GET REQUEST - SmellPanty</h3>'
    elif request.method == 'POST':
        return '<h3> POST - Pussy</h3>'
    elif request.method == 'PUT':
        return '<h2><b> PUT - SuckNFuck </b></h2>'
    else:
        return 'SmellFarts'

# Custom return response - Here its directing to an image


@app.route('/customz')
def customz():
    image_url = "https://cdn05.iwantclips.com/uploads/contents/videos/1939935/4ab04b98e05ba1a80072036a14fecbba.jpg"
    return redirect(image_url)


# Display image in the browser
@app.route('/customz2')
def customz2():
    # Example random image
    image_url = "https://cdn05.iwantclips.com/uploads/contents/videos/1939935/4ab04b98e05ba1a80072036a14fecbba.jpg"
    # Fetch image from URL
    img_response = requests.get(image_url)
    # Return as image
    return Response(img_response.content, mimetype='image/jpeg')

# Custom Response Second Example - This was given my AI , exactly what i wanted
# Black background , everything centered and spread woman ass


@app.route('/customz3')
def customz3():
    custom_html = """
    <html>
        <head><title>BootyFart</title></head>
        <body style="background-color: black; color: #00FF9F; text-align: center;">
            <h1>Welcome to the Custom Response Page</h1>
            <p>This page demonstrates a custom HTML response.</p>
            <img src="https://cdn05.iwantclips.com/uploads/contents/videos/1939935/4ab04b98e05ba1a80072036a14fecbba.jpg" alt="Random Image" style="width: 50%; border-radius: 10px;">
        </body>
    </html>
    """
    return Response(custom_html, mimetype='text/html')

# Custom Route 4 - From tutz


@app.route('/cu4')
def cu4():
    return 'such and fuck'


# Custom Headers
@app.after_request
def add_custom_headers(response):
    # Simple header message (always works, doesn't break content)
    response.headers['X-Greeting'] = 'Hi Friend'
    response.headers['X-My-App'] = 'Flask-Delivery-Service'
    response.headers['X-Backblaze-Status'] = 'Ready'
    response.headers['X-Rape-Kill'] = 'Lick Asss and pussy'
    return response


# --- Run App ---
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
