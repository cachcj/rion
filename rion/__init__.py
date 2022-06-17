"""
 Start modules for all imports
"""
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np
from rion.errors import Errors

from rion.rion import Rion


def handler() -> None:
    """
    Manages the CL arguments and distributes them to appropriate commands.
    """
    # time Handler
    start = datetime.now()

    # Load Error Object
    errorx = Errors()

    if len(sys.argv) >= 2:
        # Deletes the path and the basic command from the array
        command_list = np.delete(np.array(sys.argv), [0, 1])

        # Create a variable that stores the main command.
        loader: str = sys.argv[1]

        # Converts the Numpy array back to a normal list
        flags: object = np.ndarray.tolist(command_list)

        # Create Object
        riox = Rion(flags)

        # Transfer the NumPy array with all configs to the relevant functions.
        if loader == "install":
            riox.install()
        elif loader == "update":
            riox.update()
        elif loader == "upgrade":
            riox.upgrade()
        elif loader == "version":
            riox.version()
        elif loader == "remove":
            riox.remove()
        elif loader == "search":
            riox.search()
        elif loader == "freeze":
            riox.freeze()
        elif loader == "check":
            riox.check()
        elif loader == "installer":
            riox.installer()
        elif loader == "uninstall":
            riox.uninstall()
        elif loader == "login":
            riox.login()
        elif loader == "server":
            riox.server()
        else:
            # If no command was found, it aborts the program.
            errorx.error_message("no command was found")
    else:
        errorx.error_message("no input")

    # End Time Managment
    diff = datetime.now() - start
    print(f"run: {diff.total_seconds()}s")


def read_config() -> dict:
    """
    Read the config
    """
    # create dict
    user = {"system": rion}
    # go to config file
    path: str = os.getcwd()
    os.chdir(Path.home())
    if not os.path.isdir("rion"):
        subprocess.run("rion installer")
        time.sleep(1)
    os.chdir("rion")
    # open file
    with open("rion.conf", "w", encoding="utf8") as runner:
        for line in runner.readlines():
            # The config has no line breaks
            line = line.replace(" ", "")
            # Since the config has no descriptions, each line must have a =.
            # The Config is not there for decoration but to store values.
            if "=" not in line:
                Errors.error_message("Wrong Syntax")
            # Manipulating the Dictonary through the user configs.
            line = line.split("=")
            user[line[0]] = line[1]
    # go back
    os.chdir(path)
    return user
