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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    POST /sessions
    Return: create a new session for the user
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        json_payload = jsonify(email=email, message="logged in")
        json_payload.set_cookie('session_id', session_id)
        return json_payload
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    DELETE /sessions
    destroy user session and redirect to GET
    """
    sesh_id = request.cookies.get("session_id")
    try:
        user = self._db.get_user_from_session_id(sesh_id)
        user_id = self._db.get(user.id)
        self._db.destroy_session(user_id)
        return redirect('/')
    except NoResultFound:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
