#!/usr/bin/env python3
''' Password Encryption and Validation Module '''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
        Generates a salted and hashed password.

        Returns:
                bytes: A byte string representing the salted, hashed password.
        '''
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Checks if provided password matches the hashed password
        Returns:
                bool: True if the provided password matches the hashed
                password, False otherwise.
        '''
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
