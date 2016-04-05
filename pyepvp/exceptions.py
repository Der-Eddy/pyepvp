import os, platform

def systemInfo():
    '''
    Basically only used for debug purposes.
    '''
    system = platform.system()
    systemVersion = platform.version()
    pythonBuild = platform.python_build()
    pythonVersion = platform.python_version()

    systemInfo = " (OS: " + system + " " + systemVersion + " | Python Version: " + pythonBuild[0] + ")"
    return systemInfo

user = ["user"]
guest = ["guest"]
moderators = ["coadmin", "globalmod", "moderator"]
editorial = ["editor", "translator", "podcaster", "broadcaster", "eventplanner"]
undergroundUsers = ["level3", "level2"]
formerRanks = ["founder", "formerstaff", "formervolunteer"]
premiumUsers = ["premium"] + moderators + undergroundUsers + editorial

def hasPermissions(ranks, group=guest):
    '''
    Checks if user has permissions for a method, emits insufficientAccessException if not.
    '''
    if ranks in guest:
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

class pyepvpBaseException(Exception):
    def __init__(self, message="Exception? Something went wrong"):
        super(pyepvpBaseException, self).__init__(message + systemInfo())

class tbmSecretwordException(Exception):
    def __init__(self, methodName):
        super(tbmSecretwordException, self).__init__("No Secretword defined for \"" + methodName + "\" method" + systemInfo())

class emptyObjectException(Exception):
    def __init__(self, objectName):
        super(emptyObjectException, self).__init__("Empty Object \"" + objectName + "\" given (Parsing Error?)" + systemInfo())

class noAuthenticationException(Exception):
    def __init__(self):
        super(noAuthenticationException, self).__init__("Provide a username and password" + systemInfo())

class invalidAuthenticationException(Exception):
    def __init__(self):
        super(invalidAuthenticationException, self).__init__("Login doesn't work (Wrong Username or Password?)" + systemInfo())

class requestFailedTBMAPIException(Exception):
    def __init__(self):
        super(requestFailedTBMAPIException, self).__init__("Could not retrieve from TBM API (Wrong Secretword?)" + systemInfo())

class requestFailedException(Exception):
    def __init__(self):
        super(requestFailedException, self).__init__("Elitepvpers.com not reachable" + systemInfo())

class requestDatabaseException(Exception):
    def __init__(self):
        super(requestDatabaseException, self).__init__("Elitepvpers.com Database not reachable (Backup Time 4:30?)" + systemInfo())
