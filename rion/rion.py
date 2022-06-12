"""
Rion Class
"""
import os
import string
from getpass import getpass
from os.path import exists
from pathlib import Path
from typing import TextIO

from rion.database import Database
from rion.errors import Errors
from rion.helper import Helper
from rion.package import Package


class Rion:
    """Rion Class"""

    def __init__(self, content: str) -> None:
        self.rion = Database("rion")
        self.content = content
        self.path_user = str(Path.home())
        self.path_config = f"{self.path_user}/rion.conf"
        self.path_db = f"{self.path_user}/rion.db"
        self.node = f"{self.path_user}/node"
        self.path = os.getcwd()
        self.error = Errors()
        self.pkg = Package()
        self.table = "installed"
        self.helper = Helper()

    @staticmethod
    def check() -> None:
        """
        Rion
        """

    def config(self) -> list:
        """
        Read username and password
        """

    def dlist(self) -> None:
        """
         Prints all installed packages
         """
        # outputty contains an array of all records from corresponding table
        outputty: list = self.rion.list_table("installed", "name")
        # Checks if the output is empty
        if len(outputty) == 0:
            self.error.error_message("The database is empty")
        # Set Path
        path = os.getcwd()
        # Switch to Rion
        os.chdir(self.helper.os_bindings(f"{self.path_user}/rion"))
        # check old lists
        if exists("rion_list.txt"):
            os.remove("rion_list.txt")
        # write new file
        docker: TextIO
        with open("rion_list.txt", "a", encoding="utf8") as docker:
            for runner in outputty:
                docker.write(
                    (str(runner).replace("(", "").replace(")", "").replace("'", ""))
                )
        # Return folder
        os.chdir(path)

    def freeze(self) -> None:
        """
        Prints all installed packages
        """
        # outputty contains an array of all records from corresponding table
        outputty: list = self.rion.list_table("installed", "name")
        # Checks if the output is empty
        if len(outputty) == 0:
            self.error.error_message("The database is empty")
        else:
            # If it is not empty, then spend it all
            for runner in outputty:
                print(str(runner).replace("(", "").replace(")", "").replace("'", ""))

    @staticmethod
    def install() -> None:
        """
        install packages
        """

    def installer(self) -> None:
        """
        Rion installer
        """
        # To install Rion we go to the user directory.
        os.chdir(self.path_user)
        # We overload the path management
        # with platform specific instances to prevent errors
        os.mkdir(self.helper.os_bindings("rion"))
        # Database Management
        self.rion.create_database()
        self.rion.create_table("installed", "name text, version text, venv text")
        # Config Managment
        with open("rion.conf", "w", encoding="utf8") as docker:
            docker.write("conf=rion\n")
        # Venv Management
        os.mkdir(self.helper.os_bindings("node"))
        # Go back to the folder
        os.chdir(self.path)

    def login(self) -> None:
        """
            Creates a user in the User Config
        """
        # create Correct list
        correct: str = string.ascii_letters + string.digits
        # Reads the username
        username: str = input("Username:")
        # Checks if the username is long enough
        if len(username) >= 5:
            # Checks if there are any illegal characters in the string
            for runner in username:
                if runner not in correct:
                    self.error.error_message("Wrong Syntax")
        else:
            self.error.error_message("User exist")
        # Reads the password
        password = getpass()
        # Checks if the password is long enough
        if len(password) >= 8:
            # Checks if there are any illegal characters in the string
            for runner in password:
                if runner not in correct:
                    self.error.error_message("Wrong Syntax")
        else:
            self.error.error_message("User exist")
        # Load the rion System
        os.chdir(self.helper.os_bindings(f"{self.path_user}/rion"))
        # Open the config file
        with open("rion.conf", encoding="utf8") as config:
            conflist: list = config.readlines()
            # Search for an existing user
            for runner in conflist:
                if "username" in runner:
                    self.error.error_message("User exist")
        # Change the mode for opening the file
        with open("rion.conf", "a", encoding="utf8") as config:
            # Creates a user in the User Config
            config.write(f"username={username}\n")
            config.write(f"password={password}\n")
        # Goes back to the initial directory
        os.chdir(self.path)

    @staticmethod
    def remove() -> None:
        """
        Rion
        """

    def search(self) -> None:
        """
        Search Package in Database
        """
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
            runner_layer_runner: str = module_layer[2: module_layer.index(",")][:-1]
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
