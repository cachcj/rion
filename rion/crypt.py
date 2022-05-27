"""
Crypt - Modul
"""

import hashlib
from cryptography.fernet import Fernet
from numpy import byte


def gen_key() -> bytes:
    """
    Create a new key.
    """
    return Fernet.generate_key()


def gen_key_as_string(key: bytes) -> str:
    """
    Turns a key into a string
    """
    return key.decode("utf-8")


def new_instance(key: bytes) -> Fernet:
    """
    Load Instance
    """
    return Fernet(key)


def encrypt(key: bytes, message: str) -> byte:
    """
    Encrypt String
    """
    return Fernet(key).encrypt(message.encode())


def decrypt(key: bytes, message: str) -> str:
    """
    Decrypt String
    """
    return Fernet(key).decrypt(message).decode()


def md5(fname: str):
    """
    Return MD5 Value
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as docker:
        for chunk in iter(lambda: docker.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
