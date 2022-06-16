"""!
Database Class.
"""
import sqlite3


class Database:
    """!
    Database Class.
    """

    def __init__(self, db_name: str):
        """!
        Konstruktor.

        @param db_name  The name of the database.
        @return An instance of the Database Class with the specified name.
        """
        self.db_name = db_name

    def create_database(self) -> None:
        """!
        Creates a database with sqlite3.

        @return
        """
        # Creates the database via a Python Courser
        sqlite3.connect(f"{self.db_name}.db")

    def courser(self) -> sqlite3.Connection:
        """!
        Creates a courser.

        @return
        """
        # Creates the database via a Python Courser
        return sqlite3.connect(f"{self.db_name}.db")

    def create_table(self, db_table: str, db_header: str) -> None:
        """!
        Creates the corresponding tables via an SQL block.

        @param db_table Name of the table.
        @param db_header    Name of the column of the table.
        @return
        """
        # Creates a connection to the database
        con = sqlite3.connect(f"{self.db_name}.db")
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

    def input_value(self, db_table: str, db_content: str) -> None:
        """!
        Creates the corresponding tables via an SQL block.

        @param self
        @param db_table The name of the table.
        @param db_content   The values to be entered into the table.
        @return An entry in the table with the inputted values.
        """
        # Creates a connection to the database
        con = sqlite3.connect(f"{self.db_name}.db")
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

    def list_table(self, db_table: str, db_header: str) -> list:
        """!
        Return List from a Table.

        @param self
        @param db_table The name of the table to be sorted.
        @param db_header    The name of the variable by which the table should be sorted.
        @return
        """
        # Creates a connection to the database
        con = sqlite3.connect(f"{self.db_name}.db")
        # Creates a courser that points to the database
        cur = con.cursor()
        # Creates an empty list
        container = []
        for row in cur.execute(f"SELECT * FROM {db_table} ORDER BY {db_header}"):
            container.append(row)
        return container

    def print_table(self, db_table: str) -> None:
        """!
        Print List from a Table.

        @param self
        @param db_table The name of the table to be printed.
        @return
        """
        for i in self.list_table(self.db_name, db_table):
            print(i)

    def db_handler(self, sql_expression: str) -> None:
        """!
        A Simple SQL Handler for Primitive Queries.

        @param self
        @param sql_expression   The SQL expression to be executed.
        @return
        """
        # Creates a connection to the database
        con = sqlite3.connect(f"{self.db_name}.db")
        # Creates a courser that points to the database
        cur = con.cursor()
        # Executes the SQL
        cur.execute(sql_expression)
        # "Save" the changes
        con.commit()
        # close
        con.close()
        # Destroys the Courser
        cur = None

    def delete_package(self, db_table: str, package_list: str, content: str) -> None:
        """!
        Delete Packages from a SQL table.

        @param self
        @param db_table The name of the table to be modified.
        @param package_list
        @param content
        @return
        """
        # Creates a connection to the database
        con = sqlite3.connect(f"{self.db_name}.db")
        # Creates a courser that points to the database
        cur = con.cursor()
        # Creates the SQL DELETE Command
        table = f"DELETE FROM {db_table} WHERE {package_list}={content};"
        # Executes the SQL
        cur.execute(table)
        # "Save" the changes
        con.commit()
        # close
        con.close()
        # Destroys the Courser
        cur = None
