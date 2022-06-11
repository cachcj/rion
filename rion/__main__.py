#!/usr/bin/env python3
"""
 Module to launch all core commands
"""
from . import handler


# test test function
def calc_add(zahl1: int, zahl2: int) -> int:
    return zahl1 + zahl2


if __name__ == "__main__":
    # enable entry points
    handler()
