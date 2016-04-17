'''
   Implementation test drive
'''
from initdaemon import Daemon
from public import ReadPublicinfo
from preparetest import TestParpare


class testdrive(Daemon, TestParpare, ReadPublicinfo):
    def __init__(self, testitemname):
        self.testitem = testitemname

    def setup(self):
        a=self.baseddependency('make', 'gcc', 'g++', 'java', 'ls')
        print a
    
    def _run(self):
        testinfo = ReadPublicinfo()
        print testinfo.dotestlist
    
# testcase
# case1
test = testdrive('Perf_cpu')
test._run()
test.setup()
