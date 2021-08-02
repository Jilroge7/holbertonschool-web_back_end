#!/usr/bin/env python3
"""
Encrypting password module
"""
from typing import AnyStr
import bcrypt


def hash_password(password: str) -> bytes:
    """
    accepts a passwd str and returns a salted hashed passwd
    byte string.
    """
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
