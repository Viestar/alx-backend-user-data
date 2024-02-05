#!/usr/bin/env python3
""" Module for Authorisation on requirements, headers and users"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Class for Authorisation on requirements, headers and users"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if excluded_paths is None or path is None:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                """ # Remove the asterisk and check if 
                the path starts with the excluded path """
                base_excluded_path = excluded_path.rstrip('*')
                if path.startswith(base_excluded_path):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns None, For now, always until further implementation """
        if request is None:
            return None
        elif 'Authorisation' not in request.headers:
            return None
        return request.headers['Authorisation']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None, For now, always until more implementation """
        return None
