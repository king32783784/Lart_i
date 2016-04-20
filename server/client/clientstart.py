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
    xmlfiles['testxml'] = os.path.abspath(options.testxmlname)
    xmlfiles['setupxml'] = os.path.abspath(options.setupxmlname)
    return xmlfiles

if __name__ == "__main__":
    sys.path.append(os.path.abspath('tests'))
    xmlfile = recivefile()
    Mytestapp = TestDrive(xmlfile['setupxml'], xmlfile['testxml'])
    Mytestapp.start()
