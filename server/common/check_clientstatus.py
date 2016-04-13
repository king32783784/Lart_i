'''
    check test machine's status
'''
import os
import pexpect
import linecache
from server_client import Server_Client


class Check_Clientstatus(Server_Client):
    def checkstatus(self):
        args=("/tmp/client_status")
        self._scpfile(self.ip, args)
        thestatus = linecache.getline("client_status", 1).strip('\n')
        try:
            os.remove('client_status')
        except OSError:
            pass
        if thestatus == 'locked':
            return "unready"
        else:
            return "ready"

    def checkinstallstatus(self):
        args=("/tmp/client_status")
        self._scpfile(self.ip, args)
        thestatus = linecache.getline("client_staus", 2).strip('\n')
        if thestatus == 'ready':
            return "ready"
        else:
            return "unready"

# tests = Check_Clientstatus('192.168.32.46')
# a = tests.checkstatus()
# print a