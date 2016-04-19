'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from runtest import RunTest

class Perf_cpu(RunTest):
    def __init__(self, setupxml, testxml):
        self.setupxml = setupxml
        self.testxml = testxml

    def _setup(self):
        '''
         Setup before starting test
        '''
        RunTest._depend('gcc', 'make', 'automake', 'libtool')
        RunTest._download(self.setupxml, self.testxml, 'Perf_cpu')
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
