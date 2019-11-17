"""
author: Daniel Ashcroft
purpose: host the the main.py
"""
import os, time, requests, json
from main import app
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from pyngrok import ngrok

# thread details
MAX_THREAD_POOL_WORKERS = 4

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


# route test
TF_VERSION_ROUTE = "/tfversion"
# response
TFVERSION_SUCCESS = "2.0.0"

# local configurations
LOCAL_PORT_NUMBER = "5002"
LOCALHOST_TFVERSION = "http://localhost:" + LOCAL_PORT_NUMBER + TF_VERSION_ROUTE
CHECK_LOCAL_TFVERSION = CURL + " " + LOCALHOST_TFVERSION

# remote configurations
remote_address = ""
NGROK_LOCAL_SERVER = "http://localhost:4040"
NGROK_LOCAL_SERVER_TUNNEL_ROUTE = NGROK_LOCAL_SERVER +"/api/tunnels"
NGROK_CALL = "ngrok http " + LOCAL_PORT_NUMBER


#medi_screen
MEDI_SCREEN_WEBSITE = "http://mediscreen.tech"
MEDI_SCREEN_UPDATE_URL = MEDI_SCREEN_WEBSITE + "/updateURL.php?url="
MEDI_SCREEN_WEBSITE_UPDATE_URL_SUCCESS_RESULT = "Update received"
MEDI_SCREEN_WEBSITE_SUCCESS = "<Response [200]>"



def cmd(command):
    """
    performs a command line command
    :param command: url
    :type command: str
    :return: an execution of the command
    :rtype: string
    """
    return os.popen(command).read()


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

def getRemoteAddress():


    tunnel_url = requests.get(NGROK_LOCAL_SERVER_TUNNEL_ROUTE).text
    j = json.loads(tunnel_url)
    print(j)
    tunnel_url = j['tunnels'][0]['public_url']  # Do the parsing of the get
    print(tunnel_url)
    tunnel_url = tunnel_url.replace("https", "http")
    return tunnel_url




def isRemoteHostRunning():
    """
    checks if the remote is working properly
    :return: result
    :rtype: bool
    """
    site = getRemoteAddress()
    print("\n\n\nREMOTE ADDRESS : " + site + "\n\n\n")
    if checkCmd(CURL + " " + site + TF_VERSION_ROUTE, TFVERSION_SUCCESS):
        print("the website is HOSTING!")
        return True

    else:
        print("the website isn't HOSTING!")
        return False

def restartHosting():
    """
    Restarts the ngrok hosting
    :return:
    :rtype:
    """
    print("going to call:", NGROK_CALL)
    cmd(NGROK_CALL)

def inform_website_of_site_name_change():
    try:
        url = getRemoteAddress()
        res = requests.get(MEDI_SCREEN_UPDATE_URL + url)
        print(res)
        if res == MEDI_SCREEN_WEBSITE_UPDATE_URL_SUCCESS_RESULT or MEDI_SCREEN_WEBSITE_SUCCESS:

            print("\n\n\n\n---SUCCESS ON WEBSITE UPDATE FOR URL CHANGE -------\n\n\n")

        else:
            print("\n\n\n\n---FAILURE ON WEBSITE UPDATE FOR URL CHANGE -------\n\n\n")
    except Exception as e:
        print(e)

def update_med_screen():
    while True:
        inform_website_of_site_name_change()
        time.sleep(SLEEP_TIME_IN_SECONDS)



def manageHosting():
    keepHosting = True
    while keepHosting:
        print("Lets keep hosting")
        if not isRemoteHostRunning():
            print("restarting hosting")
            restartHosting()
            time.sleep(SLEEP_TIME_IN_SECONDS)
            inform_website_of_site_name_change()
        time.sleep(SLEEP_TIME_IN_SECONDS)


def run():
    executor = ThreadPoolExecutor(max_workers=MAX_THREAD_POOL_WORKERS)
    executor.submit(update_med_screen)
    executor.submit(manageMain)
    # pMain = Process(target=manageMain)
    # pMain.start()
    # pHost = Process(target=manageHosting)
    # pHost.start()


# run()

update_med_screen()


# print(ngrok.__version__)

#
#
# public_url = ngrok.connect(5002)
#
# tunnels = ngrok.get_tunnels()
# print(tunnels)
# print("public_url:", public_url)
# print("public_url:", type(public_url))