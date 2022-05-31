"""
Search command
"""


def runnable_search(db_name: str, content: str) -> None:
    """
    Suche in der Datenbank nach Namen
    """
    print(db_name + content)
