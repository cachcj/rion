"""
    Short Error Libary
"""
from termcolor import colored


def noinput() -> None:
    """
    The user has not provided any arguments.
    """
    print(colored('The user has not made an entry. Please check your input.', 'red'))
