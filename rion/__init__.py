#!/usr/bin/env python3
"""
 Start modules for all imports
"""
import sys

import numpy as np

from . import errors
from . import runner


def handler() -> None:
    """
        Manages the CL arguments and distributes them to appropriate commands.
    """
    if sys.argv:
        # Deletes the path and the basic command from the array
        command_list = np.delete(np.array(sys.argv), [0, 1])

        # Transfer the NumPy array with all configs to the relevant functions.
        if sys.argv[1] == "install":
            # Converts the Numpy array back to a normal list
            runner.install(np.ndarray.to(command_list))
    else:
        errors.noinput()
