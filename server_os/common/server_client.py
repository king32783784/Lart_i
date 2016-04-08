import os
import pexpect


class Server_Client():
    def __init__(self, clientip, args):
        self.ip = clientip
        self.args = args

    def _login(self):
        try:
            log = 'Are you sure you want to continue connecting (yes/no)? '
            clientlogin = pexpect.spawn('ssh root@%s' % self.ip)
            index = clientlogin.expect(['%s' % log, ':'], timeout=3)
            if index == 0:
                print "ssh %s error" % self.ip
            if index == 1:
                clientlogin.sendline('yes')
                clientlogin.expect('.')
                clientlogin.sendline('')
                clientlogin.expect(':')
                clientlogin.sendline('abc123')
                clientlogin.sendline('%s' % self.args)
                clientlogin.interact()
            if index == 2:
                client.sendline('abc123')
                client.sendline('%s' % self.args)
                clientlogin.interact()
        except pexpect.EOF:
            print "ssh %s error" % self.ip
'''
testcase:
testa = Server_Client('192.168.32.64')
testa._login()
'''
