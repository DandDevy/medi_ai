import datetime
import socket
from threading import Condition, RLock
class Logger:
    __instance = None
    __FILE_LOCATION = "log.txt"
    __rlock = RLock()
    __condition = Condition()
    __read_in_use = False

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Logger.__instance == None:
            Logger()
        return Logger.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Logger.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self

    def read(self):

        try:
            while(Logger.__read_in_use):
                Logger.__condition.wait()

            Logger.__read_in_use = True
            Logger.__condition.acquire()
            log_reader = open(self.__FILE_LOCATION, "r")
            try:
                res = log_reader.read()
                log_reader.close()

                Logger.__read_in_use = False
                return res
            finally:
                Logger.__read_in_use = False
                log_reader.close()
                Logger.__condition.release()

        except Exception as e:
            return e

    def log(self, type, user_ip):

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        message = "date & time=" + str(datetime.datetime.now()) + "\t\tlocal hostname & ip="+ hostname + " " + str(IPAddr) + "\t\tuser ip=" + str(user_ip) +"\t\ttype=" + type + ";\n"
        try:
            log_reader = open(self.__FILE_LOCATION, "a")
            try:
                res = log_reader.write(message)
                return res
            finally:
                log_reader.close()
        except Exception as e:
            return e


# logger = Logger()
# logge1 = Logger.getInstance()
# r = logge1.read()
# print(r)
# logge2 = Logger.getInstance()

# for i in range(10):
#     logger.log("test", "172.28.5.199")
# r= logger.read()
#
# print(r)
# log = open("log.txt","a")
# log.write("asdasd\n")
# log.write("asdasd\n")
# log.write("asdasd\n")
# log.close()

# logreader = open("log.txt", "r")
# res = logreader.read()
# print(res)
# logreader.close()