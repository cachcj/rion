"""
Search command
"""


def runnerable_search(db_name: str, content: str) -> None:
    """
    Suche in der Datenbank nach Namen
    """
    # Platzhalter
    docker = db_name + content
    print(docker)
