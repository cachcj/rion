"""!
    Short Error Class
"""

import sys

from termcolor import colored


class Errors:
    """!
    Short Error Class
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def error_message(text: str) -> None:
        """!
        Resumes an error.
        """
        print(colored(text, "red"))
        sys.exit(0)
