#!/usr/bin/env python3
"""
Flask set up, basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config class for flask_babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get locale from request
    """
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def index() -> str:
    """
    GET
    Return: Flask app
    """
    return render_template('3-index.html')

translate = gettext('home_title', 'home_header')

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
