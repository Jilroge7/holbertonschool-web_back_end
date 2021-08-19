#!/usr/bin/env python3
"""
Encrypting password module
"""
import bcrypt
import sys
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register a user instance
        """
        try:
            if self._db.find_user_by(email=email) is not None:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        check for valid password
        """
        try:
            user = self._db.find_user_by(email=email)
            passwd = password.encode('UTF-8')
            if bcrypt.checkpw(passwd, user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """
    accepts a passwd str and returns a salted hashed passwd
    byte string.
    """
    hashed = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
    return hashed
