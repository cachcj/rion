"""
Delete Package
"""


from pathlib import Path
import os
from rion import helper
from rion import crypt
from rion import db


def runnable_installer() -> None:
    """
    load installer
    """
    # OS Path Modul
    path: str = helper.os_bindings(f"{str(Path.home())}/rion")
    Path(path).mkdir(parents=True, exist_ok=True)

    # Change base
    os.chdir(path)

    # Install Database
    db.create_database("rion")
    db.create_table("rion.db", "installed", "name text, version text, venv text")

    # Load Cipher
    key = crypt.gen_key()

    # Safe Key
    key = crypt.gen_key_as_string(key)

    # write key in conf
    with open("rion.conf", "a", encoding="utf8") as docker:
        docker.write(f"key={key}\n")

    # setup root venv
    path = helper.os_bindings(f"{str(Path.home())}/rion/node")
    Path(path).mkdir(parents=True, exist_ok=True)
