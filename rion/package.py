class Package:
    """
    Create a package
    """

    def __init__(self):
        self._venv = None
        self._version = None
        self._name = None

    # Getter

    def get_name(self):
        return self._name

    def get_version(self):
        return self._version

    def get_venv(self):
        return self._venv

    # Setter
    def set_name(self, content):
        self._name = content

    def set_version(self, content):
        self._version = content

    def set_venv(self, content):
        self._venv = content
