#!/usr/bin/env python3
"""
session auth class inherits from auth
"""
from api.v1.auth.auth import Auth
from base64 import b64encode, b64decode
from models.user import User
from models.base import DATA
from typing import TypeVar


class SessionAuth(Auth):
    """
    inherits from auth
    """
    pass
