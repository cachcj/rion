import sqlite3
from pprint import pprint


def create_database(name: str) -> None:
    """
    Creates a database with sqlite3 and mysql
    """
    # Creates the database via a Python Courser
    sqlite3.connect(f"{name}.db")


def create_table(db_name: str, db_table: str, db_header: str) -> None:
    """
    Creates the corresponding tables via an SQL block.
    """
    # Creates a connection to the database
    con = create_database(db_name)
    # Creates a courser that points to the database
    cur = con.cursor()
    # Creates the SQL Command
    table = f"CREATE TABLE {db_table} ({db_header})"
    # Executes the SQL
    cur.execute()
    # "Save" the changes
    con.commit()
    # Destroys the Courser
    cur = None


def out_table(db_name: str, db_table: str) -> None:
    """
    Output of database entries via SQL as array
    """
    # Stack Overflow: /53128279/how-to-print-output-from-sqlite3-in-python
    con = sqlite3.connect(db_name + ".db")
    # Creates the SQL Command and execute
    cursor = con.execute(f"PRAGMA table_info({db_table});")
    # Return the values
    print(cursor.fetchall())


def list_table(db_name: str, db_table: str, db_header: str) -> None:
    """ """
    # Creates a connection to the database
    con = create_database(db_name)
    # Creates a courser that points to the database
    cur = con.cursor()
    rows = cur.execute(f"SELECT {db_header} FROM {db_table}").fetchall()