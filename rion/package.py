"""
    Package Class
"""

class Package:
    """
    Simple Python Package Class
    """
    name: str = ""
    dependency: list[str] = []
    version: str = ""
    path: str = ""
    venv: str = ""

    def __init__(self, name, dependency, version, path, venv) -> None:
        """
        parameterized constructor for packages
        """
        self.name = name
        self.dependency = dependency
        self.version = version
        self.path = path
        self.venv = venv
