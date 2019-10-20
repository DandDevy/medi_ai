"""
author: Daniel Ashcroft
purpose: host the the main.py
"""
import os, time
from main import app
from concurrent.futures import ThreadPoolExecutor
import threading

# medi_ai app details
MAIN_FLASK_NAME = "main.py"
RUN_MAIN_IN_THREAD = True
SLEEP_TIME_IN_SECONDS = 2
HOST = "0.0.0.0"
DEBUG = False

# commands
CURL = "curl"
PYTHON = "python"
PUT_IN_BACKGROUND = "&"
SSH_R = "ssh -R"

# routes
TF_VERSION_ROUTE = "/tfversion"

# local configurations
LOCAL_PORT_NUMBER = "5002"
LOCALHOST_TFVERSION = "http://localhost:" + LOCAL_PORT_NUMBER + TF_VERSION_ROUTE
CHECK_LOCAL_TFVERSION = CURL + " " + LOCALHOST_TFVERSION

# remote configurations
SITE_NAME = "medi-ai"
SERVEO_DOT_NET = "serveo.net"
REMOTE_PORT = "80"
SERVEO_CALL = SITE_NAME + ":" + REMOTE_PORT +":localhost:" + LOCAL_PORT_NUMBER + " " + SERVEO_DOT_NET
REMOTE_ADDRESS = "https://" + SITE_NAME +"." + SERVEO_DOT_NET
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
    cmd(SSH_R + " " + SERVEO_CALL)
    return True

def startApp():
    """
    starts the flask app
    :return:
    :rtype:
    """
    app.debug = DEBUG
    app.run(host=HOST, port=LOCAL_PORT_NUMBER, threaded=True)


def manageMain():
    keepRunningMain = True
    while keepRunningMain:
        print("Lets keep running main")
        if not isMainRunning():
            print("restarting main")
            startApp()

        time.sleep(SLEEP_TIME_IN_SECONDS)

def manageHosting():
    keepHosting = True
    while keepHosting:
        print("Lets keep hosting")
        if not isRemoteHostRunning():
            print("restarting hosting")
            restartHosting()

        time.sleep(SLEEP_TIME_IN_SECONDS)

def host():
    executor = ThreadPoolExecutor(max_workers=4)
    executor.submit(manageHosting)
    executor.submit(manageMain)

host()
