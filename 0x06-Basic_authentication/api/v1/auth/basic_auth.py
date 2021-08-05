#!/usr/bin/env python3
"""
basic auth class inherits from auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    inherits from auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        returns the base64 part for authorization
        """
        if authorization_header is None or type(authorization_header) != str:
            return (None)
        if authorization_header[0:5] == "Basic ":
            authorization_header.split(' ')
            return authorization_header[1]
