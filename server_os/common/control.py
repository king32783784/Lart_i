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

class ClientCheck(multiprocessing.Process, Check_Clientstatus):
    def __init__(self, totalclients, readyclients):
        multiprocessing.Process.__init__(self)
        self.totalclients = totalclients
        self.readyclients = readyclients

    def run(self):
        while True:
            for checkip in self.totalclients:
                client_do = Check_Clientstatus(checkip)
                clientstatus = client_do.checkstatus()
                if clientstatus == 'ready':
                    self.readyclients.put(checkip)
            time.sleep(30)


class IsoCheck(multiprocessing.Process, Check_Update):
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
    def __init__(self, readyclients, dotestisos):
        multiprocessing.Process.__init__(self)
        self.readyclients = readyclients
        self.dotestisos = dotestisos

    def run(self):
        while True:
            testiso = self.dotestisos.get()
            testclient = self.readyclients.get()
            starttestlist = []
            startclient = ClientStart(testclient, testiso)
            starttestlist.append(startclient)
            print testclient, testiso
            startclient.start()
            file('/tmp/daemon.pid', 'a+').write("%s\n" % startclient.pid)
            for startclient in starttestlist:
                startclient.join()
            time.sleep(30)


class Main(Daemon, IsoCheck, ClientCheck, TestControl):
    def __init__(self, setupinfo):
        Daemon.__init__(self)
        self.totalclients = setupinfo['xml_dict']['clientip']

    def _run(self):
        readyclients = multiprocessing.JoinableQueue()
        dotestisos = multiprocessing.JoinableQueue()
        controllist = []
        control = IsoCheck(dotestisos)
        controllist.append(control)
        control.start()
        file('/tmp/daemon.pid', 'a+').write("%s\n" % control.pid)
        control = ClientCheck(self.totalclients, readyclients)
        controllist.append(control)
        control.start()
        file('/tmp/daemon.pid', 'a+').write("%s\n" % control.pid)
        control = TestControl(readyclients, dotestisos)
        controllist.append(control)
        control.start()
        file('/tmp/daemon.pid', 'a+').write("%s\n" % control.pid)
        for control in controllist:
            control.join()
