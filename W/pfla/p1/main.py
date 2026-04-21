# - Main Python file for flash

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Boooty Dancer Dundo</h1>"


if __name__ == '__main__':
    app.run(
        debug=True,
    )
