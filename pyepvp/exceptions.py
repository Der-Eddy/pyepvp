import os, platform

def systemInfo():
    system = platform.system()
    systemVersion = platform.version()
    pythonBuild = platform.python_build()
    pythonVersion = platform.python_version()

    systemInfo = " (" + system + " " + systemVersion + " | " + pythonBuild[0] + ")"
    return systemInfo

moderators = ["coadmin", "globalmod", "moderator"]
undergroundUsers = ["level3", "level2"]
shoutboxUsers = ["premium"]
shoutboxUsers.extend(moderators)
shoutboxUsers.extend(undergroundUsers)

def hasPermissions(ranks, group):
    hasRight = False
    for rank in ranks:
        if rank in group:
            hasRight = True
            continue
    if hasRight == False:
        raise insufficientAccessException()
        return False
    else:
        return True

class insufficientAccessException(Exception):
    def __init__(self):
        super(insufficientAccessException, self).__init__("Nicht die passenden Rechte" + systemInfo())

class invalidAuthenticationException(Exception):
    def __init__(self):
        super(invalidAuthenticationException, self).__init__("Login nicht möglich" + systemInfo())

class requestFailedException(Exception):
    def __init__(self):
        super(requestFailedException, self).__init__("Elitepvpers nicht erreichbar" + systemInfo())

class requestDatabaseException(Exception):
    def __init__(self):
        super(requestFailedException, self).__init__("Elitepvpers Datenbank nicht erreichbar (Ist Backup Zeit?)" + systemInfo())