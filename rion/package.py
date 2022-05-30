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
    date: str = ""
    description: str = ""
    license: str = ""
    sha: bytes = b""

    def __init__(
            self, name, dependency, version, path, venv, date, description, lmit, sha
    ) -> None:
        """
        parameterized constructor for packages
        """
        self.name = name
        self.dependency = dependency
        self.version = version
        self.path = path
        self.venv = venv
        self.date = date
        self.description = description
        self.lmit = lmit
        self.sha = sha
