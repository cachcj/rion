"""
login user
"""
import os
import string
from os.path import expanduser

from rion import errors


def runnable_login() -> None:
    """
    Creates a user in the User Config
    """
    # create Correct list
    correct = string.ascii_letters + string.digits

    # Reads out the current folder
    path = os.getcwd()

    # Reads the username
    username = input("Username:")

    # Checks if the username is long enough
    if len(username) >= 5:
        # Checks if there are any illegal characters in the string
        for runner in username:
            if runner not in correct:
                errors.errorsyntax()
    else:
        errors.nouser()

    # Reads the password
    password = input("Password:")

    # Checks if the password is long enough
    if len(password) >= 8:
        # Checks if there are any illegal characters in the string
        for runner in password:
            if runner not in correct:
                errors.errorsyntax()
    else:
        errors.nouser()

    # Load the rion System
    os.chdir(f"{expanduser('~')}/rion")

    # Open the config file
    with open("rion.conf", encoding="utf8") as config:
        conflist: list = config.readlines()

        # Search for an existing user
        for runner in conflist:
            if "username" in runner:
                errors.user_exists()

    # Change the mode for opening the file
    with open("rion.conf", "a", encoding="utf8") as config:
        # Creates a user in the User Config
        config.write(f"username={username}\n")
        config.write(f"password={password}\n")

    # Goes back to the initial directory
    os.chdir(path)
