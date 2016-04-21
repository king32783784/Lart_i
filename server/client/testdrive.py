'''
   Implementation test drive
'''
import os
import sys
import logging
from initdaemon import Daemon
from public import ReadPublicinfo
from runtest import RunTest
from preparetest import TestParpare
from logging_config import *



class TestDrive(Daemon, ReadPublicinfo, TestParpare):
    logger = logging.getLogger('client')
    homepath = os.getcwd()
    def __init__(self, setupxml, testxml):
        ReadPublicinfo.__init__(self, setupxml, testxml)  
        Daemon.__init__(self)
        self.testmode = self.setupinfo['xml_dict']['testtype'][0]
        self.setupxml = setupxml
        self.testxml = testxml
    
    def testselect(self):
        if self.testmode == 'default':
            self.logger.info('default test start')
            self._runtest()
        if self.testmode == 'custom':
            pass    # Interface

    def mktestdir(self, pertesttype, pertest):
        dirtypes = ['result', 'debug']
        dirlist = {}
        localpath = os.path.join(self.homepath, 'testresult/%s' % self.testmode)
        for pertype in dirtypes:
            dirpath = self.mkdirectory('%s' % localpath, '/',
                                       '%s' % pertesttype, '%s' %pertest,
                                       '%s' % pertype)
            dirlist[pertype] = dirpath
        return dirlist

    def _runtest(self): 
        testlist = self.dotestlist
        for pertesttype in testlist:
            for pertest in testlist[pertesttype]:
                pathlist = self.mktestdir(pertesttype, pertest)
                Logging_Config.setlogger(pertest, '%s/setup.out' % pathlist['debug'])
                stdout_logger = logging.getLogger(pertest)
                setup = StreamToLogger(stdout_logger, logging.INFO)
                sys.stdout = setup
                job = __import__('%s' % pertest)
                runjob = job.DoTest(self.setupxml, self.testxml, self.homepath)
                runjob._setup()
                Logging_Config.setlogger(pertest, '%s/result.out' % pathlist['result'])
                stdout_logger = logging.getLogger(pertest)
                test = StreamToLogger(stdout_logger, logging.INFO)
                sys.stdout = test
                runjob._runtest()
        

    def _run(self):
        self.logger.info('test start')
        self.testselect()


# testcase
# case1
#test = TestDrive('Testsetup_sample.xml', 'Test_parameter.xml')
#test._run()
#test='Perf_cpu'
#job = __import__('%s' % test)

