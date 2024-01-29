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
        elif path not in excluded_paths:
            return True
        elif path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None, For now, always until further implementation """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None, For now, always until more implementation """
        return None
