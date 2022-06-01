def runnable_config(pathToConfig: str) -> list:
    user: str = ""
    pwd: str = ""

    # Helper
    cutter = lambda beta: beta.replace("'", '"').split('"')[1]

    # File Open
    with open(pathToConfig, encoding="utf8") as config:
        conflist: list = config.readlines()

    for runner in conflist:
        if "username" in runner:
            user = cutter(runner)
        if "password" in runner:
            pwd = cutter(runner)

    return ["auth", [user, pwd]]
