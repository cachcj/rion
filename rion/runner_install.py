import tarfile
from rion import db

"""
install packages
"""


def runnable_install(content: str) -> None:
    """
    install packages
    """

    # specifying database loacation
    db_name: str = "rion.db"
    # setting config-file location
    pathtovenv: str = "rion.conf"

    # extract given archive
    with tarfile.open(content[0], "r") as archive:
        archive.extractall()

    # get Versionumber
    pos = abs(content[0][::-1].find("v-") - len(a)) - 1
    version = content[0][pos : len(a) - 7 : 1].replace("_", ".")

    db.input_value("rion.db", "installed", f"({content[0]}, {version})")
