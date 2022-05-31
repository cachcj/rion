"""
Delete Package
"""

from pathlib import Path
import os
from rion import helper
from rion import crypt
from rion import db


def runnable_install() -> None:
    """
    load installer
    """
    # OS Path Modul
    path: str = helper.os_bindings(f"{os.path.expanduser('.')}/rion")
    Path(path).mkdir(parents=True, exist_ok=True)

    # Change base
    os.chdir(path)

    # Install config
    with open("config.txt", "w", encoding="utf8") as docker:
        docker.write("rion_conf\n")

    # Install Database
    db.create_database("Packages")
    db.create_table("Packages", "Package", "name text, version text")

    # Load Cipher
    key = crypt.gen_key()

    # Safe Key
    key = crypt.gen_key_as_string(key)

    # write key in conf
    with open("config.txt", "a", encoding="utf8") as docker:
        docker.write(f"key={key}\n")

    # Install Venv Manager
    with open("venv.txt", "w", encoding="utf8") as docker:
        docker.write("Venv Manager\n")

    # setup root venv
    path += helper.os_bindings("/venv/node")
    Path(path).mkdir(parents=True, exist_ok=True)

    # write rion as root venv
    with open("venv.txt", "a", encoding="utf8") as docker:
        docker.write("/venv/node\n")
