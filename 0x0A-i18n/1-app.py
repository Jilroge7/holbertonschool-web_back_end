#!/usr/bin/env python3
"""
Flask set up, basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config class for flask_babel
    """
    LANGUAGES = ['en', 'fr']
    app.config['BABEL_DEFAULT_LOCALE', 'BABEL_DEFAULT_TIMEZONE'] = 'en', 'UTC'


@app.route('/')
def index() -> str:
    """
    GET
    Return: Flask app
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
