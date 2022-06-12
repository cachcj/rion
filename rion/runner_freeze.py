"""
Outputs all packages
"""

from rion import db
from rion import errors


def runnable_freeze() -> None:
    """
    Prints all installed packages
    """

    # outputty contains an array of all records from corresponding table
    outputty: list = db.list_table("rion", "installed", "name")

    if len(outputty) == 0:
        # empty Database
        errors.emptydb()

    for runner in outputty:
        print(str(runner).replace("(", "").replace(")", "").replace("'", ""))
