#!/usr/bin/env python3
"""
session auth class inherits from auth
"""
from api.v1.auth.auth import Auth
from base64 import b64encode, b64decode
from models.user import User
from models.base import DATA
from typing import TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    """
    inherits from auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a session id
        """
        if user_id is None or type(user_id) != str:
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        get a user id from session id
        """
        if session_id is None or if type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)
