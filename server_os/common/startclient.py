import multiprocessing
import time
import os
from check_update import Check_Update
from server_client import Server_Client
from downloadfile import downloadfile


class ClientStart(multiprocessing.Process, Server_Client, Check_Update):
    def __init__(self, runclient, testiso):
        multiprocessing.Process.__init__(self)
        Check_Update.__init__(self)
        self.runclient = runclient
        self.testiso = testiso
    
    def set_kstart(self):
        pass
    
    def checkcleintinstalld(self):
        pass

    def setserverdchp(self, cmdtype):
        if cmdtype == "enable":
            os.system('systemctl start dhcpd')
        elif cmdtype == "disable":
            os.system('systemctl enable dhcpd')
    
    def allowclientrestart(self):
        

    def checkclientlogin(self):
        pass

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
        time.sleep(120)             
        
