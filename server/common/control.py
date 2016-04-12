import sys
import time
import multiprocessing
import linecache
from multiprocessing import Queue
from collections import deque
from parsing_xml import Parsing_XML
from initdaemon import Daemon
from check_update import Check_Update
from public import ReadPublicinfo
from check_clientstatus import Check_Clientstatus
from server_client import Server_Client
from startclient import ClientStart


class IsoCheck(multiprocessing.Process, Check_Update):
    '''
       Check whether there is a need to test ISO
    '''
    def __init__(self, dotestisos):
        self.dotestisos = dotestisos
        multiprocessing.Process.__init__(self)
        Check_Update.__init__(self)

    def run(self):
        firstiso = Check_Update().isoname
        self.dotestisos.put(firstiso)
        while True:
            gettestiso = Check_Update().isoname
            if gettestiso > firstiso:
                self.dotestisos.put(gettestiso)
            firstiso = gettestiso
            time.sleep(300)


class TestControl(multiprocessing.Process):
    '''
      For the client to invoke the control
    '''
    def __init__(self, dotestisos, totalclients):
        multiprocessing.Process.__init__(self)
        self.dotestisos = dotestisos
        self.totalclients = totalclients

    def _checkserverstatus(self, server_status):
        '''
         Query server is available or not
        '''
        while True:
            try:
                server_status.get(block=False)
                break
            except:
                time.sleep(3)

    def _checkclient(self):
        '''
           Query whether there is available to the client
        '''
        while True:
            for checkip in self.totalclients:
                client_do = Check_Clientstatus(checkip)
                clientstatus = client_do.checkstatus()
                if clientstatus == 'ready':
                    availableclient = checkip
                    break
            time.sleep(3)
        return availableclient

    def run(self):
        serverstatus = multprocessing.Queue()
        serverstatus.put('True')
        while True:
            self._checkserverstatus(serverstatus)
            testclient = self._checkclient()
            testiso = self.dotestisos.get()
            startclient = ClientStart(testclient, testiso, serverstatus)
            startclient.start()
            startclient.join()
            time.sleep(30)


class Main(Daemon, IsoCheck, TestControl):
    '''
    Start ISO queries and client control
    '''
    def __init__(self, setupinfo):
        Daemon.__init__(self)
        self.totalclients = setupinfo['xml_dict']['clientip']

    def _run(self):
        dotestisos = multiprocessing.JoinableQueue()
        controllist = []
        control = IsoCheck(dotestisos)
        controllist.append(control)
        control.start()
        file('/tmp/daemon.pid', 'a+').write("%s\n" % control.pid)
        control = TestControl(dotestisos, self.totalclients)
        controllist.append(control)
        control.start()
        file('/tmp/daemon.pid', 'a+').write("%s\n" % control.pid)
        for control in controllist:
            control.join()
