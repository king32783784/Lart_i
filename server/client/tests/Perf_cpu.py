'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from runtest import RunTest

class Perf_cpu(RunTest):

    def initialize(self):
        defectlist = self.baseddependency('gcc', 'make', 'automake', 'libtool')
        if len(defectlist) > 0:
            self.packageinstall(defectlist)

    def _setup(self):
        '''
         Setup before starting test
        '''
        toolurl = self.setupinfo['xml_dict']['testtoolurl'][0]
        tooltar = self.baseparameter('Test_parameter.xml')['xml_dict']['testool'][0]
        filepath = self.testtooldownload(toolurl, tooltar)
        self.initialize()
        srcdir = self.decompressfile(filepath, self.__class__.__name__)
        os.chdir(srcdir)
        self._configure('--without-mysql')
        self._make('LIBTOOL=/usr/bin/libtool install')

    def _runtest(self):
        basearg = self.baseparameter(self.__class__.__name__)
        cpu_max_prime=basearg['cpu_max_prime'].split(',')
        for max_prime in cpu_max_prime:
            cmd = "sysbench --test=%s --cpu-max-prime=%s run" % (basearg['test_type'], max_prime)
            print cmd
# testcase
#a = Perf_cpu()
#a.initialize()
#a._setup()
#a._runtest()
