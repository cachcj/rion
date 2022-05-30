"""
The module does all the things I am too lazy to do. sorry
"""

# pylint: disable = E, W, R, C

import ctypes
import os
import platform


def testsudo() -> bool:
    """
    Checks if a script was started with admin or root rights.
    """
    test: bool = True
    try:
        is_admin = os.getuid() == 0
        print(is_admin)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        test = False
    return test


def os_bindings(path: str) -> str:
    """
    Changes the paths from Linux to Windows.
    It's really only about the backslash.
    @rtype: object
    """
    if "Windows" in platform.platform():
        return path.replace("/", "\\")

    return path
