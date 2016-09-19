#!/usr/bin/env python
# coding=utf8
'''
   Name:Linux automated regression testing
   Function:Check the ISO changes
   Author:peng.li@i-soft.com.cn
   Time:20160413
'''
import os
import sys
import logging
import time
import xml.dom.minidom

from subprocess import PIPE, Popen, call
from optparse import OptionParser
from testdrive import TestDrive
from logging_config import Logging_Config

def getupdateid():
    dom=xml.dom.minidom.parse('/etc/update/updates.xml')
    itemlist=dom.getElementsByTagName('updates')
    item=itemlist[0]
    updateid=item.getAttribute("latest")
    return updateid

def setinituid():
    inituid = getupdateid()
    try:
        f = open('uid', 'w')
        f.write(inituid)
        f.closed
    except IOError:
        print "plealse check uid"

def checkidupdate():
    f = open('uid', 'r')
    lastuid = f.read().strip()
    f.closed
    while True:
        newuid = getupdateid()
        print newuid
        if newuid > lastuid:
            f = open('uid', 'w')
            f.write(newuid)
            f.closed
            break
        else:
            time.sleep(10)
            print "check now"
    return "TRUE"

def recivefile():
    parser = OptionParser()
    parser.add_option("-t", "--testxml", dest="testxmlname",
                      help="testxml")
    parser.add_option("-s", "--setupxml", dest="setupxmlname",
                      help="do not print status")
    (options, args) = parser.parse_args()
    xmlfiles = {}
    xmlfiles['testxml'] = os.path.abspath(options.testxmlname)
    xmlfiles['setupxml'] = os.path.abspath(options.setupxmlname)
    return xmlfiles

if __name__ == "__main__":
    Logging_Config.setlogger('client', 'client.log')
    sys.path.append(os.path.abspath('tests'))
    xmlfile = recivefile()
    setinituid()
    while True:
        checktype = checkidupdate()
        print checktype
        if checktype == "TRUE":
            call('systemctl stop isoft-update-daemon', shell=True)
            Mytestapp = TestDrive(xmlfile['setupxml'], xmlfile['testxml'])
            Mytestapp._run()
            print "start"
            call('systemctl start isoft-update-daemon', shell=True)
        else:
            time.sleep(300)
