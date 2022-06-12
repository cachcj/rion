"""
Rion Class
"""
import os
import tarfile
from pathlib import Path
from typing import Callable, Any

from rion.database import Database
from rion.package import Package


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

    def config(self) -> list:

        """
        Read username and password
        """

        user: str = ""
        pwd: str = ""

        # File Open
        with open(self.path_config, encoding="utf8") as config:
            conflist: list = config.readlines()

        for runner in conflist:
            if "username" in runner:
                user = runner.replace("'", '"').split('"')[1]

            if "password" in runner:
                pwd = runner.replace("'", '"').split('"')[1]

        return ["auth", [user, pwd]]

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

    def install(self) -> None:
        """
        install packages
        """
        # Create Package
        pkg = Package("None", "None", "None")

        # specifying database loacation
        db_name: str = "rion.db"

        # extract given archive
        pathstring: str = os.getcwd()

        # We change the directory to the Venv folder to install the package there.
        os.chdir(f"{pathstring}/venv/{self.content[1]}")

        # The files are transmitted as "tar.gz". These are now unzipped and saved.
        with tarfile.open(self.content[0], "r") as archive:
            archive.extractall()

        # Then we change back to the root folder of rion.
        # Unfortunately Linux behaves a bit stupid there
        os.chdir(pathstring)

        # The version number is part of the package. Therefore it must be read out.
        pos: Callable[[Any], int | Any] = lambda docker: abs(docker[::-1].find("v-") - len(docker)) - 1
        pkg.set_version(
            self.content[0][
                pos(self.content[0]) : len(self.content[0]) - 7 : 1
            ].replace("_", ".")
        )

        # After the attempted installation we add the entry to the Rion database
        self.rion.input_value(
            db_name,
            "installed",
            f"({self.content[0]}, {pkg.get_version()}, {self.content[1]})",
        )

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
