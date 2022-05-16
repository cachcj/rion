#!/usr/bin/env python3

import sys


def handler() -> None:
    """Gibt eine Liste der Steuerargumente zurück"""
    for i in sys.argv:
        print(i)
