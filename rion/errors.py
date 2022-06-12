"""
    Short Error Class
"""

import sys

from termcolor import colored


class Errors:
    """
    Short Error Class
    """

    def __init__(self, text: str) -> None:
        print(colored(text, "red"))
        sys.exit(0)
