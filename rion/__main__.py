"""
 Module to launch all core commands
"""
from rion.__init__ import Handler

if __name__ == "__main__":
    # enable entry points
    Handler.handler()
