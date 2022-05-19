"""
    This is where the real magic happens
"""
import errors


def install(content: list) -> None:
    """
        install a package
    """
    for i in content:
        print(i)


def update(content: list) -> None:
    """
        updates the package list
    """
    # No control argument is used for updating the list
    if list:
        errors.neednoargs()
    else:
        print("do update")


def upgrade(content: list) -> None:
    """
        updates the package list
    """
    for i in content:
        print(i)
