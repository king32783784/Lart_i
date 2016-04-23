import sys
import time
import multiprocessing
import linecache
import logging
from multiprocessing import Queue
from collections import deque
from parsing_xml import Parsing_XML
from initdaemon import Daemon
from check_update import Check_Update
from public import ReadPublicinfo
from server_client import Server_Client
from clientjob import ClientJob
from check_clientstatus import Check_Clientstatus

lartlogger = logging.getLogger('Lart_i_server')

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
                lartlogger.info('%s is add to test ISO queue' % gettestiso)
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
                lartlogger.info("start checkserverstatus")
                server_status.get(block=False)
                break
            except:
                time.sleep(3)
        lartlogger.info("checkserver ok")

    def _checkclient(self):
        '''
           Query whether there is available to the client
        '''
        checktype = "FALSE"
        while checktype == "FALSE":
            for checkip in self.totalclients:
                client_do = Check_Clientstatus(checkip)
                clientstatus = client_do.checkstatus()
                if clientstatus == 'ready':
                    lartlogger.info("client %s: is ready" % checkip)
                    availableclient = checkip
                    checktype = "TRUE"
                else:
                    lartlogger.info("cliet %s: is not ready" % checkip)
            time.sleep(3)
        return availableclient

    def run(self):
        serverstatus = multiprocessing.Queue()
        serverstatus.put('True')
        while True:
            self._checkserverstatus(serverstatus)
            lartlogger.info("start client check")
            testclient = self._checkclient()
            testiso = self.dotestisos.get()
            lartlogger.info( "testiso is %s" % testiso)
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
