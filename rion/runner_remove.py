"""
Delete Package
"""

import os
import sqlite3
from rion import db
from rion import errors

def runnable_remove(db_name: str, table_name: str, pkg_name: str, content: str) -> None:
    """
    Löscht Packete vom System und aus der Datenbank
    """
    db_namex = content + db_name
    print(db_namex)

    # If package exists on machine, delete it
    if os.path.exists(content):
        os.remove(content)
        print(f"{content} has been removed from your machine.")
    elif os.path.exists(content) is False:
        print(f"{content} cannot be found on your machine.")

    # If package exists in database, delete it 
    try:
        db.delete_package(db_name, table_name, pkg_name, content)
        print(f"{content} has been removed from the database.")

    except sqlite3.Error as error:
        errors.sqlerror(error)
