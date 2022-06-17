"""
Rion Class
"""
import os
import os.path
import shutil
import string
import subprocess
from getpass import getpass
from os.path import exists
from pathlib import Path
from typing import TextIO

from rion import __init__
from rion.database import Database
from rion.errors import Errors
from rion.helper import Helper


class Rion:
    """Rion Class"""

    def __init__(self, content: object) -> None:
        self.rion = Database("rion")
        self.content = content
        self.path_user = str(Path.home())
        self.helper = Helper()
        self.path_config = f"{self.path_user}/rion.conf"
        self.path_db = f"{self.path_user}/rion.db"
        self.node = f"{self.path_user}/node"
        self.path = os.getcwd()
        self.error = Errors()
        self.table = "installed"
        self.identify = "ident"
        self.helper = Helper()
        self.user = __init__.read_config()

    @staticmethod
    def check() -> None:
        """
        Rion
        """

    def dlist(self) -> None:
        """
        Prints all installed packages
        """
        # outputty contains an array of all records from corresponding table
        outputty: list = self.rion.list_table(self.table, "name")
        # Checks if the output is empty
        if len(outputty) == 0:
            self.error.error_message("The database is empty")
        # Set Path
        path_now: str = os.getcwd()
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
        os.chdir(path_now)

    def freeze(self) -> None:
        """
        Prints all installed packages
        """
        # outputty contains an array of all records from corresponding table
        outputty: list = self.rion.list_table(self.table, self.identify)
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
        # We need to check if rion is already installed.
        if os.path.exists("rion"):
            # Since Rion is already installed it cannot be installed again.
            # Therefore, this is canceled.
            self.error.error_message("Rion is already installed.")
        else:
            # We overload the path management
            # with platform specific instances to prevent errors
            os.mkdir(self.helper.os_bindings("rion"))
            os.chdir(self.helper.os_bindings("rion"))
            # Database Management
            self.rion.create_database()
            self.rion.create_table(self.table, f"{self.identify} text, name text, version text, venv text")
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
        # Change the mode for opening the file
        with open("rion.conf", "a", encoding="utf8") as config:
            # Creates a user in the User Config
            config.write(f"username={username}\n")
            config.write(f"password={password}\n")
        # Goes back to the initial directory
        os.chdir(self.path)
        # Reload Config
        self.user = __init__.read_config()

    def remove(self) -> None:
        """
        Remove Package from venv
        """
        # Message
        print("Since here beside the name also the Venv and the version plays a role "
              "the uninstalling must be adapted somewhat. "
              "We ask for your understanding. ")
        if " " in self.content:
            # [name, venv, version]
            # Remove DB Entry
            pkg = Helper.make_init(self.content[0], self.content[1], self.content[2])
        else:
            name = self.content
            # input other data
            venv = input("Venv: ")
            # Test Venv Name
            if len(venv) <= 3:
                Errors.error_message("Venv Name is to short")
            # version
            version = input("Version: ")
            pkg = Helper.make_init(name, venv, version)
        # Fix Path
        path: str = os.getcwd()
        os.chdir(Helper.os_bindings(f"{self.path_user}/rion/node/{venv}"))
        if os.path.exists(pkg):
            # removing the file using the os.remove() method
            os.remove(pkg)
        self.rion.delete_package(self.table, self.identify, pkg)
        # go back
        os.chdir(path)

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
            # Consequently, there is an error
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

    def uninstall(self) -> None:
        """
        Uninstall Rion
        """
        # go to user folder
        os.chdir(self.path_user)
        # checking whether folder exists or not
        try:
            shutil.rmtree("rion")
        except OSError as error_log:
            self.error.error_message(str(error_log))

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

    def server(self) -> None:
        """
        Writes the connection parameters for the server into the Config
        """
        # Reads the server
        ipaddres: str = input("IP Adresse: ")
        # Read the Port
        port: str = input("Port: ")
        # check IP Adress (Syntax)
        for runner in ipaddres:
            if runner not in string.digits + ".":
                self.error.error_message("Wrong Syntax")
        # check Port
        if port not in ["22", "21", "2121"]:
            self.error.error_message("Wrong Port")
        # check if server or port exist
        os.chdir(self.helper.os_bindings(f"{self.path_user}/rion"))
        # load conf
        with open("rion.conf", "w", encoding="utf8") as runner:
            for line in runner.readlines():
                if "server" in line:
                    self.error.error_message("Server Exist")
                if "port" in line:
                    self.error.error_message("Port Exist")
            # write conf
            runner.write(f"server={ipaddres}")
            runner.write(f"port={port}")

        # Reload Config
        self.user = __init__.read_config()

    @staticmethod
    def version() -> None:
        """
        Upgrade Rion Version
        """
        subprocess.run("pip install -U rion", check=True)

    def venv(self, content) -> None:
        """
        create a new venv
        """
        path = os.getcwd()
        os.chdir(self.helper.os_bindings(f"{self.path_user}/rion"))
        if " " in content[1]:
            Errors.error_message("Wrong Syntax")
        if content[0] == "create":
            os.mkdir(content)
            print(f"create venv: {content[1]}")
        elif content[0] == "remove":
            os.remove(content[1])
            self.rion.delete_package(self.table, "venv", content[1])
        os.chdir(path)
