import os
import pexpect


class Server_Client():
    def __init__(self, clientip):
        self.ip = clientip

    def _ssh(self, cmd, args):
        ssh_newkey = 'Are you sure you want to continue connecting (yes/no)?'
        try:
            clientlogin = pexpect.spawn('%s' % cmd)
            index = clientlogin.expect([pexpect.TIMEOUT, ssh_newkey,
                                        'password: '], timeout=3)
            print index
            if index == 0:
                print "error"
                print "%s can not login. Here is what SSH said:" % self.ip
                print clientlogin.before, clientlogin.after
            if index == 1:
                clientlogin.sendline('yes')
                clientlogin.expect('password: ')
                clientlogin.sendline('abc123')
                clientlogin.sendline('%s' % args)
                clientlogin.interact()
            if index == 2:
                clientlogin.sendline('abc123')
                clientlogin.sendline('%s' % args)
                clientlogin.interact()
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF):
            print "ssh %s timeout" % self.ip

    def _reboot(self):
        cmd = "ssh root@%s" % self.ip
        self._ssh(cmd, 'reboot')

    def _scpfile(self, clientip,  remotefile):
        cmd = "scp root@%s:%s ." % (clientip, remotefile)
        self._ssh(cmd, ' ')


# testa = Server_Client('192.168.32.46')
# testa._reboot()
