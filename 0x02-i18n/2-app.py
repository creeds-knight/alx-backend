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


@babel.localeselector
def get_locale():
    """
        This gets the locale for the webpage
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
        default route
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
