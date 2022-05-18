from typing import List, Any


class Package:
    """
    Simple Python Package Class
    """
    name: str = ""
    dependency: list[str] = []
    version : str = ""
    path: str = ""

    def __init__(self, n, d, v, p) -> None:
        """
        parameterized constructor for packages
        """
        self.name = n
        self.dependency = d
        self.version = v
        self.path = p
