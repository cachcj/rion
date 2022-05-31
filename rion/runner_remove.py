"""
Delete Package
"""
from rion import db


def runnerable_remove(db_name: str, content: str) -> None:
    """
    Löscht Packete vom System und aus der Datenbank
    """
    db_namex = content + db_name
    print(db_namex)
