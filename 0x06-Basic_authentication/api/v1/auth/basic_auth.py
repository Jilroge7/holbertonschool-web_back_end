#!/usr/bin/env python3
"""
basic auth class inherits from auth
"""
from api.v1.auth.auth import Auth
from base64 import b64encode, b64decode


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
        if authorization_header[0:6] != "Basic ":
            return (None)

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        decoded value of base64 str
        """
        if base64_authorization_header is None or type(
                base64_authorization_header
                ) != str:
            return (None)

        try:
            return b64decode(base64_authorization_header,
                             None, False).decode('UTF-8')
        except Exception:
            return (None)
