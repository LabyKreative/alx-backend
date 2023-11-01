#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Babel  Config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.debug = False
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Handles route."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
