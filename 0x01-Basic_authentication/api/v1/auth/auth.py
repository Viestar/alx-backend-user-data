#!/usr/bin/env python3
""" Module for Authorisation on requirements, headers and users"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Class for Authorisation on requirements, headers and users"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False, For now, always until further implementation"""
        if excluded_paths is None or path is None:
            return True
        elif path in excluded_paths:
            return False
        # Ensures slash tolerance
        path = path.rstrip('/') + '/'  # Ensure path ends with a slash
        # Ensure excluded_paths end with a slash
        excluded_paths = [p.rstrip('/') + '/' for p in excluded_paths]

        # Returns False if path is in excluded_paths
        return path not in excluded_paths

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
