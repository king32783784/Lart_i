import os
import time
from preparetest import TestParpare
from public import ReadPublicinfo
from testsetup import TestSetup
from parameter import ParameterAnltsis
from subprocess import call


class RunTest(TestParpare, TestSetup, ParameterAnalysis):
    
    @staticmethod
    def _depend(self, *args)
        defectlist = self.baseddependency(*args)
        if len(defectlist) > 0
            self.packageinstall(defectlist)

    def testresult(self):
        pass

    def runcmd(self, args):
        pass
 
    def stbmonitor(self):
        pass

    def exception(self):
        pass

    @staticmethod
    def _starttest():
        while True:
            print "hello"
            time.sleep(10)
