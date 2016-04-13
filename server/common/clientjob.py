'''
   Start and control the module responsible for client installation,
   the client test start and monitor the client start.
'''
import multiprocessing
import time
import os
import shutil
from check_update import Check_Update
from server_client import Server_Client
from downloadfile import downloadfile
from check_clientstatus import Check_Clientstatus
from modifyfile import ModifyFile


class ClientStarttest(Server_Client):
    def __init__(self, startclientip, localfile):
        self.startclientip = startclientip
        self.localfile = localfile
        self.filetar = localfile + ".tar.bz2"
        self.starttest()      
        
    def _scpfile(self):
        print self.filetar
        spawn_cmd = "scp %s root@%s:" % (self.filetar, self.startclientip)
        print spawn_cmd
        self._ssh(spawn_cmd, ' ')

    def _starttest(self):
        spawn_cmd = "ssh root@%s" % self.startclientip
        do_cmd = ("tar xf %s" % self.filetar, "python client/clienttest.py")
        self._ssh(spawn_cmd, do_cmd)

    def starttest(self):
        self._scpfile()
        self._starttest()

class ClientJob(multiprocessing.Process, Check_Clientstatus, Check_Update, ClientStarttest):
    def __init__(self, runclient, testiso, serverstatus):
        multiprocessing.Process.__init__(self)
        Check_Update.__init__(self)
        self.runclient = runclient
        self.testiso = testiso
        self.serverstatus = serverstatus

    def set_kstart(self):
        print self.runclient
        os.system("pwd")
        kssample = '/var/www/html/ks.sample'
        finalks = '/var/www/html/ks.cfg'
        setkscfgip = ModifyFile(self.runclient, "256.256.256.256",
                                finalks, kssample)

    def check_clientinstalled(self):
        '''
           check client install status,if timeout, take iso to
           isolist and mail to tester
        '''
        pass

    def allowclientrestart(self):
        while True:
            try:
                # self.check_clientinstalled()
                open("/tmp/installed", 'r')
                self.setserverdhcp("stop")
                open("/tmp/allowrestart", 'w')
                break
            except IOError:
                pass
            time.sleep(10)

    def setserverdhcp(self, cmdtype):
        if cmdtype == "start":
            os.system('systemctl start dhcpd')
        elif cmdtype == "stop":
            os.system('systemctl enable dhcpd')

    def checkclientlogin(self):
        '''
          Check client with testiso login status, if timeout,
          take iso to isolist and mail to tester.
        '''
        while True:
            clientlogin = self.checkinstallstatus()
            if clientlogin == 'ready':
                os.remove("/tmp/installed")
                os.renove("/tmp/allowrestart")
                self.setserverdhcp("start")
                break
            else:
                time.sleep(60)

    def Realeaseserver(self):
        '''Realease server'''
        self.server_status.put('True')

    def clientmonitoring(self):
        pass

    def isoinstall(self):
        print self.runclient
        self.downloadiso(self.testiso)
        self.mountiso(self.testiso)
        self.set_kstart()
        client_run = Server_Client(self.runclient)
        client_run._reboot()

    def run(self):
        self.isoinstall()
        self.allowclientrestart()
        self.checkclientlogin()
        clientjob = ClientStarttest(self.runclient, 'client')
        self.clientmonitoring()
        time.sleep(120)

# test case
# 1
test = ClientStarttest('192.168.32.46', 'client')
# a = test.checkclientinstalld()
# print a
