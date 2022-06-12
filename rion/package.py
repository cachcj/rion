"""
Package Class
"""


class Package:
    """
    Create a package
    """

    def __init__(self):
        """
        Konstruktor
        """
        self._venv = None
        self._version = None
        self._name = None

    # Getter

    def get_name(self):
        """
        Get Name
        @return:
        """
        return self._name

    def get_version(self):
        """
        Get Version
        @return:
        """
        return self._version

    def get_venv(self):
        """
        Get Venv
        @return:
        """
        return self._venv

    # Setter
    def set_name(self, content):
        """
        Set Name
        @param content:
        @return:
        """
        self._name = content

    def set_version(self, content):
        """
        Set Version
        @param content:
        @return:
        """
        self._version = content

    def set_venv(self, content):
        """
        Set Venv
        @param content:
        @return:
        """
        self._venv = content
