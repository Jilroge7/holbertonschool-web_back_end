#!/usr/bin/env python3
"""
Flask set up, basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config class for flask_babel
    """
    LANGUAGES = ['en', 'fr']
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get locale from request
    """
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    GET
    Return: Flask app
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
