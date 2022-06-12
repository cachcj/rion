"""
Rion Class
"""
import os

from rion.database import Database
from pathlib import Path


class Rion:
    """Rion Class"""

    def __init__(self, content: str) -> None:
        self.rion = Database("rion")
        self.content = content
        self.user = str(Path.home())
        self.path_config = f"{self.user}/rion.conf"
        self.path_db = f"{self.user}/rion.db"
        self.node = f"{self.user}/node"
        self.path = os.getcwd()

    @staticmethod
    def check() -> None:
        """
        Rion
        """

    @staticmethod
    def config() -> None:
        """
        Rion
        """

    @staticmethod
    def dlist() -> None:
        """
        Rion
        """

    @staticmethod
    def freeze() -> None:
        """
        Rion
        """

    @staticmethod
    def install() -> None:
        """
        Rion
        """

    @staticmethod
    def installer() -> None:
        """
        Rion
        """

    @staticmethod
    def login() -> None:
        """
        Rion
        """

    @staticmethod
    def remove() -> None:
        """
        Rion
        """

    @staticmethod
    def search() -> None:
        """
        Rion
        """

    @staticmethod
    def update() -> None:
        """
        Rion
        """

    @staticmethod
    def upgrade() -> None:
        """
        Rion
        """
