"""
    Database system and database handler
"""

import sqlite3
from pprint import pprint


def create_database(db_name: str) -> None:
    """
    Creates a database with sqlite3 and mysql
    """
    # Creates the database via a Python Courser
    sqlite3.connect(f"{db_name}.db")


def create_table(db_name: str, db_table: str, db_header: str) -> None:
    """
    Creates the corresponding tables via an SQL block.
    """
    # Creates a connection to the database
    con = sqlite3.connect(f"{db_name}.db")
    # Creates a courser that points to the database
    cur = con.cursor()
    # Creates the SQL Command
    table = f"CREATE TABLE {db_table} ({db_header})"
    # Executes the SQL
    cur.execute(table)
    # "Save" the changes
    con.commit()
    # close
    con.close()
    # Destroys the Courser
    cur = None


def input_value(db_name: str, db_table: str, db_content: str) -> None:
    """
    Creates the corresponding tables via an SQL block.
    """
    # Creates a connection to the database
    con = sqlite3.connect(f"{db_name}.db")
    # Creates a courser that points to the database
    cur = con.cursor()
    # Creates the SQL Command
    table = f"INSERT INTO {db_table} VALUES {db_content}"
    # Executes the SQL
    cur.execute(table)
    # "Save" the changes
    con.commit()
    # close
    con.close()
    # Destroys the Courser
    cur = None


def out_table(db_name: str, db_table: str):
    """
    Output of database entries via SQL as array
    """
    # src: https://stackoverflow.com/questions/53128279
    con = sqlite3.connect(db_name + ".db")
    # Creates the SQL Command and execute
    cursor = con.execute(f"PRAGMA table_info({db_table});")
    # Return the values
    pprint(cursor.fetchall())


def list_table(db_name: str, db_table: str, db_header: str):
    """
    Return List of Table
    """
    # Creates a connection to the database
    con = sqlite3.connect(f"{db_name}.db")
    # Creates a courser that points to the database
    cur = con.cursor()
    for row in cur.execute(f"SELECT * FROM {db_table} ORDER BY {db_header}"):
        print(row)
