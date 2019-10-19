"""
author: Daniel Ashcroft
purpose: host the the main.py
"""
import os

# commands
CURL = "curl"
PYTHON = "python"
PUT_IN_BACKGROUND = "&"

# project details
MAIN_FLASK_NAME = "main.py"
RUN_MAIN_IN_BACKGROUND = False

# routes
TF_VERSION_ROUTE = "/tfversion"

# local configurations
LOCAL_PORT_NUMBER = "5002"
LOCALHOST_TFVERSION = "http://localhost:" + LOCAL_PORT_NUMBER + TF_VERSION_ROUTE
CHECK_LOCAL_TFVERSION = CURL + " " + LOCALHOST_TFVERSION

# remote configurations
REMOTE_ADDRESS = "https://medi-ai.serveo.net"
REMOTE_TFVERSION = REMOTE_ADDRESS + TF_VERSION_ROUTE
CHECK_REMOTE_TFVERSION = CURL + " " + REMOTE_TFVERSION

TFVERSION_SUCCESS = "2.0.0"


def cmd(command):
    """
    performs a command line command
    :param command: url
    :type command: str 
    :return: an execution of the command
    :rtype: string
    """
    return os.popen(command).read()


def checkCmd(command, desiredOutput):
    """
    checks with curl if something is doing as it is supposed to
    :param command: command for the command line
    :type command: str
    :param desiredOutput: what you are testing
    :type desiredOutput: str
    :return: True or False
    :rtype: bool
    """
    res = False
    if cmd(command) == desiredOutput:
        res = True
    return res


def isMainRunning():
    """
    checks if the local main is running properly
    :return: True or False
    :rtype: Boolean
    """
    result = False
    if checkCmd(CHECK_LOCAL_TFVERSION, TFVERSION_SUCCESS):
        result = True
        print("test of ", CHECK_LOCAL_TFVERSION, " : SUCCESS")

    else:
        print("test of ", CHECK_LOCAL_TFVERSION, " : FAILURE")

    return result


def isRemoteHostRunning():
    """
    performs a remote hosting test
    :return: result
    :rtype: bool
    """
    res = False
    if checkCmd(CHECK_REMOTE_TFVERSION, TFVERSION_SUCCESS):
        res = True
        print("test of ", CHECK_REMOTE_TFVERSION, " : SUCCESS")

    else:
        print("test of ", CHECK_REMOTE_TFVERSION, " : FAILURE")
    return res


def restartHosting():
    pass


def restartMain():
    if RUN_MAIN_IN_BACKGROUND:
        cmd(PYTHON + " " + MAIN_FLASK_NAME + " " + PUT_IN_BACKGROUND)

    else:
        cmd(PYTHON + " " + MAIN_FLASK_NAME)


def host():
    if isMainRunning():
        if isRemoteHostRunning():
            print("FULL SUCCESS")

        else:
            restartHosting()

    else:
        restartMain()


host()
