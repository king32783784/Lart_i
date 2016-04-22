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
from server_client import Server_Client
from clientjob import ClientJob


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
                print "start checkserverstatus"
                server_status.get(block=False)
                break
            except:
                time.sleep(3)
        print "checkserver ok"

    def _checkclient(self):
        '''
           Query whether there is available to the client
        '''
        availableclient = ''
        while availableclient is not True:
            for checkip in self.totalclients:
                client_do = Check_Clientstatus(checkip)
                clientstatus = client_do.checkstatus()
                if clientstatus == 'ready':
                    availableclient = checkip
                    break
            break
            time.sleep(3)
        print availableclient
        return availableclient

    def run(self):
        serverstatus = multiprocessing.Queue()
        serverstatus.put('True')
        while True:
            self._checkserverstatus(serverstatus)
            print "start client check"
            testclient = self._checkclient()
            print "client ok, %s" % testclient
            testiso = self.dotestisos.get()
            print "testiso is %s" % testiso
            startclient = ClientJob(testclient, testiso, serverstatus)
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
