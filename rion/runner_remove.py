"""
Delete Package
"""

import os
import sqlite
from rion import db
from rion import errors

def runnable_remove(db_name: str, db_table: str, package: str) -> None:
    """
    Löscht Packete vom System und aus der Datenbank
    """
    db_namex = package + db_name
    print(db_namex)

    # If package exists on machine, delete it
    if os.path.exists(package):
        os.remove(package)
        print(f"{package} has been removed from your machine.")
    elif os.path.exists(package) is False:
        print(f"{package} cannot be found on your machine.")

    ## If package exists in database, delete it
    #try:
        ## Connect to sqlite
        #con = sqlite3.connect(f"{db_name}.db")
            ## Create cursor object
        #cur = con.cursor()

        ## Deletes package from database
        #cur.execute(f"DELETE FROM {db_table} WHERE {package}")
        #con.execute.commit()
        #print(f"{package} has been removed from the database.")
    ## Show error if error
    #except sqlite3.Error as error:
        #print("There was an error: ", error)

    #finally:
        #con.close()
        #cur = None
    try:
        db.delete_package(db_name, db_table, package)
        print(f"{package} has been removed from the database.")

    except sqlite3.Error as error:
        errors.sqlerror(error)
