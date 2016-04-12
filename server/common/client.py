import multiprocessing
import time
from check_clientstatus import Check_Clientstatus
from check_update import Check_Update


class ClientStart(multiprocessing.Process, Check_Clientstatus,
                  Check_Update):
    def __init__(self, clientip, testiso):
        multiprocessing.Process.__init__(self)
        self.clientip = clientip
        self.testiso = testiso
 
    def isoinstall(self):
   #     self.download(self.testiso)
   #     client_install = Check_Clientstatus(self.clientip, ' ')
   #     clientstatus = clien_install.checkstatus()
   #     if clientstatus == 'ready':
   #         client_install._login()
        print "%s" % self.clientip
        time.sleep(3)
        print "%s" % self.testiso 

    def run(self):
        self.isoinstall()

client_ips = ['192.168.32.1', '192.168.32.2']
test_isos = ['testiso1', 'testiso2', 'testiso3']
plist = []
for clientip in client_ips:
    p = ClientStart(clientip, 'testiso1')
    plist.append(p)
    p.start()
for p in plist:
    p.join()  
           

 

