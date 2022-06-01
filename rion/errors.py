"""
    Short Error Libary
"""

import sys

from termcolor import colored


def short(text: str) -> None:
    """
    Set a short array
    """
    print(colored(f"{text}", "red"))
    sys.exit(-1)


def noinput() -> None:
    """
    The user has not provided any arguments.
    """
    print(colored("The user has not made an entry. Please check your input.", "red"))
    sys.exit(-1)


def commandlist() -> None:
    """
    The user gets a list of commands.
    """
    print("List of commands")
    sys.exit(-1)


def neednoargs() -> None:
    """
    The Command does not need arguments.
    """
    print(colored("The Command does not need arguments.", "red"))
    sys.exit(-1)


def commandnotfound() -> None:
    """
    The command was not found.
    """
    print(colored("The command was not found.", "red"))
    sys.exit(-1)


def patherror() -> None:
    """
    The folder could not be created
    """
    print(colored("The folder could not be created.", "red"))
    sys.exit(-1)


def install_error(number: int) -> None:
    """
    Lists all errors during installation
    """
    if number == 1:
        print(colored("Rion has already been installed.", "red"))
    else:
        print(colored("No error code", "yellow"))
    sys.exit(-1)


def admin_error() -> None:
    """
    sudo / root / admin
    """
    print(colored("Please restart the program with admin rights.", "blue"))
    sys.exit(-1)


def argumentnotfound() -> None:
    """
    Required argument was not found.
    """
    print(colored("Required argument was not found.", "red"))
    sys.exit(-1)


def sqlerror(error: Exception) -> None:
    """
    SQL Error.
    """
    print(colored(str(error), "red"))
    sys.exit(-1)


def nosearchargs() -> None:
    """
    No parameters
    """
    print(colored("No parameters were passed to search. ", "red"))
    sys.exit(-1)
