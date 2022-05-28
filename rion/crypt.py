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


def sha256(fname: str):
    """
    Generate SHA Value of a file
    """
    sha256_hash = hashlib.sha256()
    with open(fname, "rb") as docker:
        for byte_block in iter(lambda: docker.read(4096), b""):
            sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())
