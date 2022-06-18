# pylint: disable-all
# pylint: disable = E, W, R, C

"""
The module does all the things I am too lazy to do. sorry
"""

import ctypes
import os
import os.path
import platform
import subprocess
import uuid
from pathlib import Path

from rion.errors import Errors


class Helper:
    """
    Helper Class
    """

    @staticmethod
    def testsudo() -> bool:
        """
        Checks if a script was started with admin or root rights.
        """
        test: bool = True
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            test = False
        return test

    @staticmethod
    def os_bindings(path: str) -> str:
        """
        Changes the paths from Linux to Windows.
        It's really only about the backslash.
        """
        if "Windows" in platform.platform():
            return path.replace("/", "\\")

        return path

    @staticmethod
    def uid() -> str:
        """
        Returns a unique random string
        """
        return str(uuid.uuid4()).replace("-", "")

    @staticmethod
    def dimarray(notbeautiful: str) -> list:
        """
        We turn the tuple into a more dimensional array
        """
        notbeautiful = notbeautiful.replace("(", "")[1:-1].replace("'", "")
        return notbeautiful.replace("'", "").split(",")

    @staticmethod
    def check(name: str, version: str, venv: str) -> bool:
        """
        Checks if a package is installed.
        """
        path: str = os.getcwd()
        name = f"{name}_v.{version}"
        if len(venv) == 0:
            venv = "venv"
        pathlib: list[str] = [str(Path.home()), "rion", "node", venv]
        for runner in pathlib:
            os.chdir(runner)
        bondage: bool = os.path.isfile(name)
        os.chdir(path)
        return bondage

    @staticmethod
    def ping(host):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        return subprocess.call(command) == 0

    @staticmethod
    def make_init(name: str, venv: str, version: str) -> str:
        return f"{name}_{version}_{venv}"

    @staticmethod
    def read_config(modul: str) -> dict:
        """
        Read the config
        """
        # create dict
        user = {"system": "rion"}
        if modul != "installer":
            # go to config file
            path: str = os.getcwd()
            os.chdir(Path.home())
            if not os.path.isdir("rion"):
                Errors.error_message("Rion ist not installed")
            os.chdir("rion")
            # open file
            try:
                with open("rion.conf", encoding="utf8") as runner:
                    for line in runner.readlines():
                        print(line)
                        # The config has no line breaks
                        line = line.replace(" ", "")
                        # Since the config has no descriptions, each line must have a =.
                        # The Config is not there for decoration but to store values.
                        if "=" not in line:
                            Errors.error_message("Wrong Syntax")
                        # Manipulating the Dictonary through the user configs.
                        line = line.replace("\n", "")
                        line = line.split("=")
                        user[line[0]] = line[1]
                # go back
                os.chdir(path)
            except Exception as error:
                Errors.error_message(str(error))
        return user
