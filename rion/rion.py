from rion.database import Database
from rion.errors import Errors


class Rion:
    def __init__(self, content: str) -> None:
        self.rion = Database("rion")
        self.content = content

    def check(self) -> None:
        pass

    def config(self) -> None:
        pass

    def dlist(self) -> None:
        pass

    def freeze(self) -> None:
        pass

    def install(self) -> None:
        pass

    def installer(self) -> None:
        pass

    def login(self) -> None:
        pass

    def remove(self) -> None:
        pass

    def search(self) -> None:
        pass

    def update(self) -> None:
        pass

    def upgrade(self) -> None:
        pass
