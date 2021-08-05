#!/usr/bin/env python3
"""
Authentication system
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        public method require auth
        """
        path = False
        return (path)

    def authorization_header(self, request=None) -> str:
        """
        public method authoration header
        """
        return (request)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        public method current user
        """
        return (request)
