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
    
    # We change the directory to the Venv folder to install the package there.
    os.chdir(f"{pathstring}/venv/{content[1]}")
    
    # The files are transmitted as "tar.gz". These are now unzipped and saved.
    with tarfile.open(content[0], "r") as archive:
        archive.extractall()
    
    # Then we change back to the root folder of rion. Unfortunately Linux behaves a bit stupid there    
    os.chdir(pathstring)

    # The version number is part of the package. Therefore it must be read out.
    version = content[0][abs(content[0][::-1].find("v-") - len(content[0])) - 1 : len(content[0]) - 7 : 1].replace("_", ".")

    # After the attempted installation we add the entry to the Rion database
    db.input_value(db_name, "installed", f"({content[0]}, {version}, {content[1]})")
