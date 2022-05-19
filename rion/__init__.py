#!/usr/bin/env python3
"""
 Start modules for all imports
"""
import sys

import numpy as np

from rion import runner
from rion.errors import commandnotfound


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
        flags: list = np.ndarray.tolist(command_list)

        # Transfer the NumPy array with all configs to the relevant functions.
        if loader == "install":
            runner.install(flags)
        elif loader == "update":
            runner.update(flags)
        elif loader == "remove":
            runner.remove(flags)
        elif loader == "search":
            runner.search(flags)
        elif loader == "list":
            runner.dlist(flags)
        elif loader == "freeze":
            runner.freeze(flags)
        elif loader == "config":
            runner.config(flags)
        elif loader == "check":
            runner.check(flags)
        elif loader == "self":
            runner.install()
        else:
            # If no command was found, it aborts the program.
            commandnotfound()

    else:
        errors.noinput()
