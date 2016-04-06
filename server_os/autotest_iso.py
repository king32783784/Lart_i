#!/usr/bin/env python
# coding=utf8
'''Name:Linux automated regression testing
   Function:Check the ISO changes
   Author:peng.li@i-soft.com.cn
   Time:20160330
'''
import os
import sys
import time
import datetime
from common.parsing_xml import Parsing_XML
from common.initdaemon import Daemon
from common.check_update import Check_Update
from common.public import ReadPublicinfo


class Iso_Install(Daemon, Check_Update):
    def __init__(self, isourl, checkfrequency):
        Daemon.__init__(self)
        Check_Update.__init__(self)
        self.isourl = isourl
        self.checkfrequency = checkfrequency

    def isoinstall(self):
        gettestiso = Check_Update().isoname
        self.downloadiso()        

    def _run(self):
        firstiso = Check_Update().isoname
        self.isoinstall()
        while True:
            gettestiso = Check_Update().isoname
            if gettestiso > firstiso: 
                self.isoinstall()
            firstiso = gettestiso          
            time.sleep(int(self.checkfrequency[0]))

if __name__ == "__main__":
    testxml = ReadPublicinfo()
    daemon = Iso_Install(testxml.setupinfo['xml_dict']['isourl'],
                              testxml.setupinfo['xml_dict']
                              ['checkfrequency'])
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "useage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
