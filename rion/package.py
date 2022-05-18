class Package:
    """
    Simple Python Package Class
    """
    name: str = ""
    dependency: list[str] = []
    version: str = ""
    path: str = ""

    def __init__(self, name, dependency, version, path) -> None:
        """
        parameterized constructor for packages
        """
        self.name = name
        self.dependency = dependency
        self.version = version
        self.path = path
