import os, platform

def systemInfo():
    system = platform.system()
    systemVersion = platform.version()
    pythonBuild = platform.python_build()
    pythonVersion = platform.python_version()

    systemInfo = " (" + system + " " + systemVersion + " | " + pythonBuild[0] + ")"
    return systemInfo

class insufficientAccessException(Exception):
    def __init__(self):
        super(insufficientAccessException, self).__init__("Nicht die passenden Rechte" + systemInfo())

class invalidAuthenticationException(Exception):
    def __init__(self):
        super(invalidAuthenticationException, self).__init__("Login nicht möglich" + systemInfo())