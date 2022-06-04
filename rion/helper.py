# pylint: disable-all
# pylint: disable = E, W, R, C

"""
The module does all the things I am too lazy to do. sorry
"""

import ctypes
import os
import platform
import uuid


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


def os_bindings(path: str) -> str:
    """
    Changes the paths from Linux to Windows.
    It's really only about the backslash.
    """
    if "Windows" in platform.platform():
        return path.replace("/", "\\")

    return path


def uid() -> str:
    """
    Returns a unique random string
    """
    return str(uuid.uuid4()).replace("-", "")


def dimarray(notbeautiful: str) -> list:
    """
    We turn the tuple into a more dimensional array
    """
    notbeautiful = notbeautiful.replace("(", "")[1:-1].replace("'", "")
    return notbeautiful.replace("'", "").split(",")
