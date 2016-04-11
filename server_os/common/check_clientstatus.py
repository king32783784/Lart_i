'''
    check test machine's status
'''
import os
import pexpect
import linecache
from server_client import Server_Client


class Check_Clientstatus(Server_Client):
    def checkstatus(self):
        self._scpfile()
        thestatus = linecache.getline("client_status", 1).strip('\n')
        os.system('rm -rf client_status')
        if thestatus == 'locked':
            return "unready"
        else:
            return "ready"

    def checkinstallstatus(self):
        pass

# tests = Check_Clientstatus('192.168.32.46')
# a = tests.checkstatus()
# print a
