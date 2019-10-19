"""
author: Daniel Ashcroft
purpose: host the the main.py
"""
import os
CHECK_TFVERSION = "curl http://localhost:5002/tfversion"
TFVERSION_SUCCESS = "2.0.0"

def checkmain():
    res = False
    tfversion = os.popen(CHECK_TFVERSION).read()

    if tfversion == TFVERSION_SUCCESS:
        res = True
        print("test of curl http://localhost:5002/tfversion : SUCCESS")


def host():
    checkmain()

host()