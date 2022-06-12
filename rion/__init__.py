"""
 Start modules for all imports
"""
import sys

import numpy as np

from rion.errors import Errors
from rion.rion import Rion


class Handler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def handler() -> None:
        """
        Manages the CL arguments and distributes them to appropriate commands.
        """

        if len(sys.argv) >= 2:
            # Deletes the path and the basic command from the array
            command_list = np.delete(np.array(sys.argv), [0, 1])

            # Create a variable that stores the main command.
            loader: str = sys.argv[1]

            # Converts the Numpy array back to a normal list
            flags: list[str] = np.ndarray.tolist(command_list)

            # Create Object
            riox = Rion(flags)

            # Transfer the NumPy array with all configs to the relevant functions.
            if loader == "install":
                riox.install()
            elif loader == "update":
                riox.update()
            elif loader == "remove":
                riox.remove()
            elif loader == "search":
                riox.search()
            elif loader == "freeze":
                riox.freeze()
            elif loader == "config":
                riox.config()
            elif loader == "check":
                riox.check()
            elif loader == "installer":
                riox.installer()
            elif loader == "login":
                riox.login()
            else:
                # If no command was found, it aborts the program.
                Errors("command was found")
        else:
            Errors("no input")
