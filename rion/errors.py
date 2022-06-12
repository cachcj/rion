"""
    Short Error Class
"""

import sys

from termcolor import colored


class Errors:
    def __init__(self, text: str) -> None:
        print(colored(self.text, "red"))
        sys.exit(0)
