'''
   Implementation test drive
'''
from initdaemon import Daemon
from public import ReadPublicinfo


class testdrive(Daemon):
    def _run(self):
        testinfo = ReadPublicinfo()
        print testinfo.dotestlist
    
# testcase
# case1
test = testdrive()
test._run()
