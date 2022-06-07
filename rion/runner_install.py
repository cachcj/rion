"""
install packages
"""

import tarfile
import os
from rion import db


def runnable_install(content: str) -> None:
    """
    install packages
    """

    # specifying database loacation
    db_name: str = "rion.db"

    # extract given archive
    pathstring: str = os.getcwd()
    os.chdir(f"{pathstring}/venv/{content[1]}")
    with tarfile.open(content[0], "r") as archive:
        archive.extractall()
    os.chdir(pathstring)

    # get Versionumber
    pos = abs(content[0][::-1].find("v-") - len(content[0])) - 1
    version = content[0][pos : len(content[0]) - 7 : 1].replace("_", ".")

    # add to database
    db.input_value(db_name, "installed", f"({content[0]}, {version}, {content[1]})")
