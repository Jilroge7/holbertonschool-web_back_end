#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, abort, request
from auth import Auth
import os


app = Flask(__name__)
AUTH = Auth()

@app.route('/', methods=['GET'])
def simple() -> str:
    """ GET /
    Return:
      simple flask app
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    POST /users
    Return: registered user's email
    and successful message
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
      AUTH.register_user(email, password)
      return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
      return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
