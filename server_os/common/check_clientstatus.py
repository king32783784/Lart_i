'''
    check test machine's status
'''
import os
import pexpect
import linecache
from server_client import Server_Client


class Check_Clientstatus(Server_Client):
    def _scpfile(self):
        try:
            log = 'Are you sure you want to continue connecting (yes/no)? '
            scpfile = pexpect.spawn('scp root@%s:/tmp/client_status .'
                                    % self.ip)
            index = scpfile.expect(['%s' % log, ':'], timeout=3)
            if index == 0:
                print "check client_status timeout"
            if index == 1:
                scpfile.sendline('yes')
                scpfile.expect('.')
                scpfile.sendline('')
                scpfile.expect(':')
                scpfile.sendline('abc123')
                scpfile.interact()
            if index == 2:
                scpfile.sendline('abc123')
                scpfile.interact()
        except pexpect.EOF:
            print 'check client_status error'
 
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
'''
testcase:
tests = Check_Clientstatus('192.168.32.46', '')
a = tests.checkstatus()
print a
'''
