"""
Delete Package
"""

import os
import sqlite3

def runnable_remove(db_name: str, content: str) -> None:
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
        # Connect to sqlite
        con = sqlite3.connect(f"{db_name}.db")
            # Create cursor object
        cur = con.cursor()

        # Deletes package from database
        cur.execute(f"DELETE FROM {db_name} where content = {content}")
        con.execute.commit()
        print(f"{content} has been removed from the database.")    
    # Show error if error
    except sqlite3.Error as error:
        print("There was an error: ", error)

    finally:
        con.close()
        cur = None
