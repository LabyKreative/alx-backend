#!/usr/bin/env python3
"""Flask App."""
from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route("/", strict_slashes=False)
def index() -> str:
    """Handles route."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
