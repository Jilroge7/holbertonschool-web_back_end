#!/usr/bin/env python3
"""
Flask set up, route for i18n project
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    GET
    Return: Flask app
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port)
