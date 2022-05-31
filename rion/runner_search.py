"""
Search command
"""
from rion import db


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
    
    ## Now print them in the right order
    if exact:
        print(exact)
    for i in moreorless:
        print(i)
    for i in indescrib:
        print(i)
