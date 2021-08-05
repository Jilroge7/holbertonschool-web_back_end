#!/usr/bin/env python3
"""
Authentication system
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        public method require auth
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return (True)

        slash = "/"
        if path[-1] != slash:
            path += slash

        if path in excluded_paths:
            return (False)
        else:
            return (True)

    def authorization_header(self, request=None) -> str:
        """
        public method authorization header
        """
        authorize = 'Authorization'
        if request is None or request.headers.get(authorize) is None:
            return None

        return request.headers.get(authorize)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        public method current user
        """
        return (None)
