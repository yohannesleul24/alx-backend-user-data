#!/usr/bin/env python3
"""
   User passwords should NEVER be stored in plain
   text in a database
"""


import bcrypt


def hash_password(password: str) -> bytes:
    ''' Implement a hash_password function that expects one string
        argument name password and returns a salted, hashed
        password, which is a byte string.
        Use the bcrypt package to perform the hashing (with hashpw).
    '''
    encoded = password.encode()
    hashed_val = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed_val


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
       is_valid function expects 2 arguments and
        returns a boolean.
       Arguments:hashed_password: bytes type
                password: string type
       Use bcrypt to validate that the provided password matches the hashed
       password.
    '''
    valid = False
    pass_encoded = password.encode()
    if bcrypt.checkpw(pass_encoded, hashed_password):
        valid = True
    return valid
