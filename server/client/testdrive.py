'''
   Implementation test drive
'''
import os
import sys
from initdaemon import Daemon
from public import ReadPublicinfo
from runtest import RunTest
from preparetest import TestParpare


class TestDrive(Daemon, ReadPublicinfo, TestParpare):
    def __init__(self, setupxml, testxml):
        ReadPublicinfo.__init__(self, setupxml, testxml)  
        Daemon.__init__(self)
        self.testmode = self.setupinfo['xml_dict']['testtype'][0]
        self.setupxml = setupxml
        self.testxml = testxml
    
    def testselect(self):
        if self.testmode == 'default':
            self._runtest()
        if self.testmode == 'cusfun':
            pass    # Interface

    def mktestdir(self, pertesttype, pertest):
        dirtypes = ['result', 'debug']
        for pertype in dirtypes:
            self.mkdirectory('testresult/%s' % self.testmode, '/',
                             '%s' % pertesttype, '%s' %pertest,
                             '%s' % pertype)

    def _runtest(self): 
        testlist = self.dotestlist
        for pertesttype in testlist:
            for pertest in testlist[pertesttype]:
                self.mktestdir(pertesttype, pertest)
                print pertest
                job = __import__('%s' % pertest)
                test = job.DoTest(self.setupxml, self.testxml)
                test._setup()
                test._runtest()
        

    def _run(self):
        self.testselect()


# testcase
# case1
#test = TestDrive('Testsetup_sample.xml', 'Test_parameter.xml')
#test._run()
#test='Perf_cpu'
#job = __import__('%s' % test)

