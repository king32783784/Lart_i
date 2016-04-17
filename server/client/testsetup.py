import os
import subprocess
from subprocess import PIPE, Popen, call
from preparetest import TestParpare

class testsetup(TestParpare):
    '''
        Test project settings
    '''
    def toolinstall(self):
        pass

    def pacagemanger(self, *args):
        '''
           Check test tool based on
        '''
        for arg in args:
            try:
                if call('which %s' % arg, shell=True) is True:
                    break
            except OSError:
                pass
        print arg
    def packageinstall(self):
        defectlist = self.baseddependency('make', 'gcc', 'gcc-c++', 'java', 'ls')
        for defect in defectlist:
            call('dnf -y install %s' % defect, shell=True)

#testcase    
test = testsetup()
test.pacagemanger('dnf', 'yum')
