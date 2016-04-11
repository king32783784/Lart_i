import multiprocessing
import time
from server_client import Server_Client

def testiso_install(testclientip='xxx.xxx.xxx.xxx', do_args='args'):
    testisoinstall = Server_Client(testclientip, do_args)

    
       
