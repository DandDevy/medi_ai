import datetime
import socket

class Logger:

    def __init__(self):
        self.__FILE_LOCATION = "log.txt"

    def read(self):
        try:
            log_reader = open(self.__FILE_LOCATION, "r")
            try:
                res = log_reader.read()
                return res
            finally:
                log_reader.close()
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