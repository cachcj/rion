"""
    This is where the real magic happens
"""

from rion import runner_search
from rion import runner_remove
from rion import runner_installer
from rion import runner_dlist
from rion import runner_freeze
from rion import runner_config
from rion import runner_check
from rion import runner_update
from rion import runner_upgrade
from rion import runner_install


def install(content: list) -> None:
    """
    install a package
    """
    runner_install.runnable_install("rion.db", content)


def update(content: list) -> None:
    """
    updates the package list
    """
    runner_update.runnable_update("rion.db", content)


def upgrade(content: list) -> None:
    """
    updates the package list
    """
    runner_upgrade.runnable_upgrade("rion.db", content)


def search(content: list) -> None:
    """
    Rion is now looking for packages
    """
    runner_search.runnable_search("rion.db", "available", "pkg_name", content)


def remove(content: list) -> None:
    """
    Rion remove packages
    """
    runner_remove.runnable_remove("rion.db", "available", "pkg_name", content)


def dlist(content) -> None:
    """
    Rion list packages
    """
    runner_dlist.runnable_dlist("rion.db", content)


def freeze(content: list) -> None:
    """
    Rion freeze packages
    """
    runner_freeze.runnable_freeze("rion.db", content)


def check(content: list) -> None:
    """
    Rion check packages
    """
    runner_check.runnable_check("rion.db", content)


def config(content: list) -> None:
    """
    Rion config packages
    """
    runner_config.runnable_config("rion.db", content)


def init() -> None:
    """
    Load install skript
    """
    runner_installer.runnable_installer()
