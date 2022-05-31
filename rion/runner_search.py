"""
Search command
"""
from rion import db


def runnerable_search(db_name: str, content: str) -> None:
    """
    Suche in der Datenbank nach Namen
    """
    x = db_name + content
    print(x)
