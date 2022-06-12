"""
Search command
"""
from rion import db
from rion import errors
from rion import helper


def runnable_search(
    db_name: str, table_name: str, header_name: str, content: str
) -> None:
    """
    Search for name in database.
    """

    # Looks if parameters were passed
    if len(content) == 0:
        # you can't rewrite it because the string always exists.
        # Therefore, you should do it like this.
        errors.nosearchargs()

    # outputty contains an array of all records from corresponding table
    outputty: list = db.list_table(db_name, table_name, header_name)

    # We need three lists to represent the three differnt search priorities.
    exact: list = []
    moreorless: list = []
    indescrib: list = []

    # Now that we have them, we use this neet for loop, to go through the array
    # and add the items to the list, that we want.
    for igit in outputty:
        # Here we cast a tuple into a string.
        # This doesn't look very great, but it works.
        igit: str = str(igit)
        # We cut off everything useless from the original string,
        # so that only the package name remains.
        igitx: str = igit[2 : igit.index(",")][:-1]
        # The case occurs when the name is exactly the same.
        # Upper and lower case is respected.
        if igitx == content:
            exact.append(igit)
        # If the user input is anywhere in the string, the following statement is executed.
        elif content in igitx:
            moreorless.append(igit)
        elif content in igit:
            indescrib.append(igit)

    # For the output we create sublists to format that a bit nicer.
    subexact: list = []
    submoreorless: list = []
    subindescrib: list = []

    # The dimarray creates a multidimensional array from the tuple which consists of a string.
    if exact:
        for i in exact:
            subexact.append(helper.dimarray(i))
    if moreorless:
        for i in moreorless:
            submoreorless.append(helper.dimarray(i))
    if indescrib:
        for i in indescrib:
            subindescrib.append(helper.dimarray(i))

    # From here begins the output
    if subexact:
        print("======================================================")
        for i in range(len(subexact)):
            print(f"{subexact[i][0]} : {subexact[i][2]}")

    if submoreorless:
        print("======================================================")
        for i in range(len(submoreorless)):
            print(f"{submoreorless[i][0]} : {submoreorless[i][2]}")

    if subindescrib:
        print("======================================================")
        for i in range(len(subindescrib)):
            print(f"{subindescrib[i][0]} : {subindescrib[i][2]}")
