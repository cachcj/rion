"""
List all packages
"""
import os
from os.path import exists
from pathlib import Path
from typing import TextIO

from rion import db
from rion import errors
from rion import helper


def runnable_dlist() -> None:
    """
    Prints all installed packages
    """

    # outputty contains an array of all records from corresponding table
    outputty: list = db.list_table("rion", "installed", "name")

    # Empty Database
    if len(outputty) == 0:
        # empty Database
        errors.emptydb()

    # Set Path
    path = os.getcwd()

    # Switch to Rion
    os.chdir(helper.os_bindings(f"{Path.home()}/rion"))

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
    os.chdir(path)
