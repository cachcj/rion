from . import package as pkg


def new_package(name, dependency, version, path) -> object:
    """
        Create a new package
    """
    return pkg(name, dependency, version, path)
