"""
Read the config file
"""


def runnable_config(pathtoconfig: str) -> list:
    """
    Read username and password
    """
    user: str = ""
    pwd: str = ""

    # Helper
    replace("'", '"').split('"')[1]

    # File Open
    with open(pathtoconfig, encoding="utf8") as config:
        conflist: list = config.readlines()

    for runner in conflist:
        if "username" in runner:
            user = runner.replace("'", '"').split('"')[1]

        if "password" in runner:
            pwd = cutter.replace("'", '"').split('"')[1]

    return ["auth", [user, pwd]]
