"""
Search command
"""
from rion import db
from rion import helper


def runnable_search(
    db_name: str, table_name: str, header_name: str, content: str
) -> None:
    """
    Search for name in database.
    """
    outputty: list = db.list_table(db_name, header_name, table_name)

    ## We need three lists to represent the three differnt search priorities.
    exact: list = []
    moreorless: list = []
    indescrib: list = []

    ## Now that we have them, we use this neet for loop, to go through the array
    ## and add the items to the list, that we want.
    for igit in outputty:
        igit: str = str(igit)
        igitx: str = igit[2 : igit.index(",")][:-1]

        if igitx.__eq__(content):
            exact.append(igit)
        elif content in igitx:
            moreorless.append(igit)
        elif content in igit:
            indescrib.append(igit)

    xexact: list = []
    xmoreorless: list = []
    xindescrib: list = []

    ## Now put them in the right order
    if exact:
        for i in exact:
            xexact.append(helper.dimarray(i))
    if moreorless:
        for i in moreorless:
            xmoreorless.append(helper.dimarray(i))
    if indescrib:
        for i in indescrib:
            xindescrib.append(helper.dimarray(i))

    if xexact:
        print("======================================================")
        for i in range(len(xexact)):
            print(f"{xexact[i][0]} : {xexact[i][2]}")

    if xmoreorless:
        print("======================================================")
        for i in range(len(xmoreorless)):
            print(f"{xmoreorless[i][0]} : {xmoreorless[i][2]}")

    if xindescrib:
        print("======================================================")
        for i in range(len(xindescrib)):
            print(f"{xindescrib[i][0]} : {xindescrib[i][2]}")
