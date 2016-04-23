#!/usr/bin/env python
# coding=utf8
'''
   Name:Linux automated regression testing
   Function:Check the ISO changes
   Author:peng.li@i-soft.com.cn
   Time:20160330
'''
from common.control import *
from common.public import ReadPublicinfo
from common.logging_config import *

Logging_Config.setlogger('Lart_i_server', 'Lart_i_server.log')
lartlogger = logging.getLogger('Lart_i_server')
testxml = ReadPublicinfo()
setupinfo = testxml.setupinfo

if __name__ == "__main__":
    testxml = ReadPublicinfo()
    setupinfo = testxml.setupinfo
    lartserver = Main(setupinfo)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            lartlogger.info('lart_i server start')
            lartserver.start()
        elif 'stop' == sys.argv[1]:
            lartlogger.info('lart_i server stop')
            lartserver.stop()
        elif 'restart' == sys.argv[1]:
            lartlogger.info('lart_i server restart')
            lartserver.restart()
        else:
            lartlogger.error("unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print "useage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
