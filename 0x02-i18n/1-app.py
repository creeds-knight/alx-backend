#!/usr/bin/env python3
"""
    Babel initial setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configuration class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


if __name__ == "__main__":
    app.run()
