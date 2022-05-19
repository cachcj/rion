"""
    This is where the real magic happens
"""
# Loads the Error.py to manage errors if necessary
import errors

# Loads all basic installations details.
import self


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


def search(content: list) -> None:
    """
        Rion is now looking for packages
    """
    for i in content:
        print(i)


def remove(content: list) -> None:
    """
        Rion remove packages
    """
    for i in content:
        print(i)


def list(content: list) -> None:
    """
        Rion list packages
    """
    for i in content:
        print(i)


def freeze(content: list) -> None:
    """
        Rion freeze packages
    """
    for i in content:
        print(i)


def check(content: list) -> None:
    """
        Rion check packages
    """
    if self.is_install:
        for i in content:
            print(i)


def config(content: list) -> None:
    """
        Rion config packages
    """
    for i in content:
        print(i)


def install() -> None:
    """
    Load install skript
    """
    self.run_install()
