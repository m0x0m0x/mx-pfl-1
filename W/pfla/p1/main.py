# - Main Python file for flash

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Boooty Dancer"


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
    )
