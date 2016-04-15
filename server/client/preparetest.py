'''
    Enable client-side test preparation
'''
import os 
import subprocess
from subprocess import PIPE, Popen


class TestParpare():
    def testtooldownload(self):
        '''
           download test tool
        '''
        pass

    def baseddependency(self, *args):
        '''
           Check test tool based on
        '''
        deletioncmdlist = []
        for arg in args:
            testcmd = Popen('which %s' % arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            testcmd.wait()
            exitcode = testcmd.poll()
            if exitcode != 0:
                deletioncmdlist.append(arg)
        return deletioncmdlist

    def joinpath(fun):
        def add_mkdir(self, default, sep, *args):
            try:
                default = os.path.join(default, sep.join(args))
                os.makedirs(default)
            except OSError:
                pass  
            return fun(self, default, sep, *args)
        return add_mkdir
 
    @joinpath
    def mkdirectory(self, default, sep, *args):
        '''
        Test results directory processing
        '''
        return default

    def logdirectory(self):
        '''
        Test log directory
        '''
        pass

    def installdirectory(self):
        '''
        Test tool installation directory
        '''
        pass

    def toolstorage(self):
        '''
        Test tool storage directory
        '''
        pass
# testcase
#a = TestParpare()
#b=a.mkdirectory('testresult/dafault', '/', 'performance', 'Perf_cpu', 'result')
#print b
#print a.baseddependency('make', 'gcc', 'g++', 'java', 'hello', 'ls')

