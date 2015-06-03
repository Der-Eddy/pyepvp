import os, platform

def systemInfo():
    system = platform.system()
    systemVersion = platform.version()
    pythonBuild = platform.python_build()
    pythonVersion = platform.python_version()

    systemInfo = " (" + system + " " + systemVersion + " | " + pythonBuild[0] + ")"
    return systemInfo

user = ["user"]
guest = ["guest"]
moderators = ["coadmin", "globalmod", "moderator"]
editorial = ["editor", "translator", "podcaster", "broadcaster", "eventplanner"]
undergroundUsers = ["level3", "level2"]
premiumUsers = ["premium"] + moderators + undergroundUsers + editorial

def hasPermissions(ranks, group):
    if ranks == user and group == guest:
        insufficientAccessException(guest=True)
    hasRight = False
    for rank in ranks:
        if rank in group:
            hasRight = True
            continue
    if hasRight == False:
        raise insufficientAccessException(group)
        return False
    else:
        return True

class insufficientAccessException(Exception):
    def __init__(self, neededRanks=["user"], guest=False):
        if guest == True:
            super(insufficientAccessException, self).__init__("You will need atleast an user session!" + systemInfo())
        else:
            super(insufficientAccessException, self).__init__("You will need atleast one of " + str(neededRanks) + " ranks to use that" + systemInfo())

class emptyObjectException(Exception):
    def __init__(self, objectName):
        super(insufficientAccessException, self).__init__("Empty Object \"" + objectName + "\" given (Parsing Error?)" + systemInfo())

class invalidAuthenticationException(Exception):
    def __init__(self):
        super(invalidAuthenticationException, self).__init__("Login doesn't work (Wrong Username or Password?)" + systemInfo())

class requestFailedException(Exception):
    def __init__(self):
        super(requestFailedException, self).__init__("Elitepvpers.com not reachable" + systemInfo())

class requestDatabaseException(Exception):
    def __init__(self):
        super(requestFailedException, self).__init__("Elitepvpers.com Database not reachable (Backup Time?)" + systemInfo())