#!/usr/bin/env python
# coding=utf8
'''
   Name:Linux automated regression testing
   Function:Check the ISO changes
   Author:peng.li@i-soft.com.cn
   Time:20160413
'''
from optparse import OptionParser
from testdrive import TestDrive

def recivefile():
    parser = OptionParser()
    parser.add_option("-t", "--testxml", dest="testxmlname",
                      help="testxml")
    parser.add_option("-s", "--setupxml", dest="setupxmlname",
                      help="do not print status")
    (options, args) = parser.parse_args()
    xmlfiles = {}
    xmlfiles['testxml'] = options.testxmlname
    xmlfiles['setupxml'] = options.setupxmlname
    return xmlfiles

if __name__ == "__main__":
    xmlfile = recivefile()
    print xmlfile
    print xmlfile['setupxml']
    daemon = TestDrive(xmlfile['setupxml'], xmlfile['testxml'])
    daemon.start()
