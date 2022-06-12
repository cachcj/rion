"""
Rion Class
"""
import os
from pathlib import Path

from rion.database import Database
from rion.errors import Errors
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
        self.error = Errors()
        self.pkg = Package()
        self.table = "installed"

    @staticmethod
    def check() -> None:
        """
        Rion
        """

    def config(self) -> list:
        """
        Read username and password
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
        install packages
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

    def search(self) -> None:
        # If there are spaces in the name the package will be rejected
        if " " in self.content:
            self.error.error_message("Wrong Package Syntax")
        # Looks if parameters were passed
        if len(self.content) == 0:
            # There are no flags and thus there are no packages to search for.
            # Consequently there is an error
            self.error.error_message("No content")
        # db_content contains an array of all records from corresponding table
        db_content = self.rion.list_table(self.table, "name")
        # We need three lists to represent the three differnt search priorities.
        exact: list = []
        moreorless: list = []
        indescrib: list = []
        # Now that we have them, we use this neet for loop, to go through the array
        # and add the items to the list, that we want.
        for module_layer in db_content:
            # Here we cast a tuple into a string.
            # This doesn't look very great, but it works.
            module_layer: str = str(module_layer)
            # We cut off everything useless from the original string,
            # so that only the package name remains.
            runner_layer_runner: str = module_layer[2 : module_layer.index(",")][:-1]
            # The case occurs when the name is exactly the same.
            # Upper and lower case is respected.
            if runner_layer_runner == self.content:
                exact.append(module_layer)
            # If the user input is anywhere in the string, the following statement is executed.
            elif self.content in runner_layer_runner:
                moreorless.append(module_layer)
            elif self.content in module_layer:
                indescrib.append(module_layer)

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
