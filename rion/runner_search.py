"""
Search command
"""
from rion import db


def runnerable_search(db_name: str) -> None:
    """
    Suche in der Datenbank nach Namen
    """
    courser = db.courser(db_name)
    print(courser)
