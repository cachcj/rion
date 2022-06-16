"""!
Package Class
"""


class Package:
    """!
    Creates a package.
    """

    def __init__(self):
        """!
        Konstruktor.
        """
        self._venv = None
        self._version = None
        self._name = None

    # Getter

    def get_name(self):
        """!
        Gets Name of the Package.

        @return The name of the Package.
        """
        return self._name

    def get_version(self):
        """!
        Gets Version of the Package.

        @return The version of the Package.
        """
        return self._version

    def get_venv(self):
        """!
        Gets Venv of the Package.

        @return The venv of the Package.
        """
        return self._venv

    # Setter
    def set_name(self, content):
        """!
        Sets Name of the Package.

        @param content  The name of the Package.
        @return:
        """
        self._name = content

    def set_version(self, content):
        """!
        Set Version of the Package.

        @param content  The version of the Package.
        @return:
        """
        self._version = content

    def set_venv(self, content):
        """!
        Set Venv of the Package.

        @param content  The venve of the Package.
        @return:
        """
        self._venv = content
