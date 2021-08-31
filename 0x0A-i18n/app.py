#!/usr/bin/env python3
"""
Flask set up, basic Babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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

    if g.user:
        locale = g.user.get('locale')
        if locale is not None and locale in Config.LANGUAGES:
            return locale

    return request.accept_languages.best_match(['LANGUAGES'])


def get_user():
    """
    get user dictionary from request
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    find a user if any and set as a global on flask.g.user
    """
    global_user = get_user()
    g.user = global_user


@babel.timezoneselector
def get_timezone():
    """
    get timezone
    """
    timezone = request.args.get('timezone')
    if timezone is not None and timezone in Config.LANGUAGES:
        return timezone

    if g.user:
        timezone = g.user.get('timezone')
        if timezone is not None and timezone in Config.LANGUAGES:
            return timezone

    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    GET
    Return: Flask app
    """
    return render_template('index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
