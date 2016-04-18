'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from client.preparetest import TestParpare
from client.public import ReadPublicinfo


class Perf_cpu(TestParpare, ReadPublicinfo):
    toolurl = self.setupinfo['xml_dict']['testtoolurl'][0]
    tooltar = 'sysbench-0.4.12.tar.gz'

    def _setup(self, toolurl, tooltar):
        ''' 
         Setup before starting test
        '''
        self.testtooldownload(toolurl, tooltar)

#testcase
a = Perf_cpu()
a._setup
