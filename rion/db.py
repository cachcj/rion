"""
    Database system and database handler
"""

import sqlite3


def create_database(db_name: str) -> None:
    """
    Creates a database with sqlite3 and mysql
    """
    # Creates the database via a Python Courser
    sqlite3.connect(f"{db_name}.db")


def courser(db_name: str) -> sqlite3.Connection:
    """
    Creates a courser
    """
    # Creates the database via a Python Courser
    return sqlite3.connect(f"{db_name}.db")


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


def list_table(db_name: str, db_table: str, db_header: str) -> list:
    """
    Return List of Table
    """
    # Creates a connection to the database
    con = sqlite3.connect(f"{db_name}.db")
    # Creates a courser that points to the database
    cur = con.cursor()
    # Creates an empty list
    container = []
    for row in cur.execute(f"SELECT * FROM {db_table} ORDER BY {db_header}"):
        container.append(row)
    return container


def print_table(db_name: str, db_table: str, db_header: str) -> None:
    """
    print List of Table
    """
    for i in list_table(db_name, db_table, db_header):
        print(i)
