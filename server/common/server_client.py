import os
import pexpect
import logging

lartlogger = logging.getLogger('Lart_i_server')

class Server_Client(object):
    def __init__(self, clientip):
        self.ip = clientip

    def _ssh(self, cmd, args):
        lartlogger.info('test')
        ssh_newkey = 'Are you sure you want to continue connecting (yes/no)?'
        try:
            clientlogin = pexpect.spawn('%s' % cmd)
            index = clientlogin.expect([pexpect.TIMEOUT, ssh_newkey,
                                        'password: '], timeout=3)
            if index == 0:
                lartlogger.debug("access %s faild" % self.ip)
                lartlogger.debug("Here is what %s said:" % self.ip)
                lartlogger.debug("%s %s" % (clientlogin.before, clientlogin.after))
            if index == 1:
                clientlogin.sendline('yes')
                clientlogin.expect('password: ')
                clientlogin.sendline('abc123')
                for arg in args:
                    clientlogin.sendline('%s' % arg)
                clientlogin.sendline('exit')
                clientlogin.interact()
            if index == 2:
                clientlogin.sendline('abc123')
                for arg in args:
                    clientlogin.sendline('%s' % arg)
                clientlogin.sendline('exit')
                clientlogin.interact()
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF):
            lartlogger.error(" server connect  %s timeout" % self.ip)

    def _reboot(self):
        spawn_cmd = "ssh root@%s" % self.ip
        args = ['reboot']
        lartlogger.info('client %s is reboot now' % self.ip)
        self._ssh(spawn_cmd, args)

    def _scpfile(self, clientip,  remotefile):
        spawn_cmd = "scp root@%s:%s ." % (clientip, remotefile)
        args = ()
        self._ssh(spawn_cmd, args)


# testa = Server_Client('192.168.32.46')
# testa._reboot()
