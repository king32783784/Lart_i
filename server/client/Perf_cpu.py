'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from preparetest import TestParpare
from public import ReadPublicinfo
from testsetup import TestSetup


class Perf_cpu(TestParpare, ReadPublicinfo, TestSetup):
    tooltar = 'sysbench-0.4.12.tar.gz'

    def initialize(self):
        defectlist = self.baseddependency('gcc', 'make', 'automake', 'libtool')
        if len(defectlist) > 0:
            self.packageinstall(defectlist)

    def _setup(self):
        '''
         Setup before starting test
        '''
        toolurl = self.setupinfo['xml_dict']['testtoolurl'][0]
        filepath = self.testtooldownload(toolurl, self.tooltar)
        self.initialize()
        srcdir = self.decompressfile(filepath, self.__class__.__name__)
        os.chdir(srcdir)
        self._configure('--without-mysql')
        self._make('')

    def _runtest(self):
        pass
# testcase
a = Perf_cpu()
a.initialize()
a._setup()
