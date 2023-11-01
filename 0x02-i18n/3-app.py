#!/usr/bin/env python3
"""Flask App."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Babel Config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select and return supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """Handles route."""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
