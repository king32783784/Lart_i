import multiprocessing
import time
import os
import shutil
from check_update import Check_Update
from server_client import Server_Client
from downloadfile import downloadfile
from check_clientstatus import Check_Clientstatus
from modifyfile import ModifyFile


class ClientStart(multiprocessing.Process, Check_Clientstatus, Check_Update):
    def __init__(self, runclient, testiso):
        multiprocessing.Process.__init__(self)
        Check_Update.__init__(self)
        self.runclient = runclient
        self.testiso = testiso
    
    def set_kstart(self):
        setkscfgip = ModifyFile(self.runclient, "256.256.256.256", "ks.sample", "ks.cfg")
        shutil.move("ks.cfg", "/var/www/html/")      
    
    def allowclientrestart(self):
        while True:
             try:
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
        while True:
            clientlogin = self.checkinstallstatus()
            if clientlogin == 'ready':
                os.remove("/tmp/installed")
                os.renove("/tmp/allowrestart")
                self.setserverdhcp("start")
                break 
            else:
                time.sleep(60)              

    def clientstart(self):
        pass

    def clientmonitoring(self):
        pass
  
    def isoinstall(self):
        self.downloadiso(self.testiso)
        self.mountiso(self.testiso) 
        self.set_kstart()
        client_run = Server_Client(self.runclient)
        client_run._reboot()

    def run(self):
        self.isoinstall()
        self.allowclientrestart()
        self.checkclientlogin()
        self.clientstart()
        self.clientmonitoring()
        time.sleep(120)   
          
# test case
# 1
#est = ClientStart('192.168.32.46', 'iso1')
#a = test.checkclientinstalld()
#print a
