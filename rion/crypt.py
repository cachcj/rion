"""
    Crypt Function
"""
import hashlib


class Crypt:
    """
    Crypt Class
    """

    def __int__(self):
        """
        Konstruktor
        """

    @staticmethod
    def sha256(fname: str) -> None:
        """
        Generate SHA Value of a file
        """
        sha256_hash = hashlib.sha256()
        with open(fname, "rb") as docker:
            for byte_block in iter(lambda: docker.read(4096), b""):
                sha256_hash.update(byte_block)
            print(sha256_hash.hexdigest())
