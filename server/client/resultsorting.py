import re

class ResultSorting(object):
    def readfile(self, resultfile):
        fopen = open(resultfile, 'r')
        f = fopen.read().strip()
        return f

    def datasearch(self, searchmode, resultfile):
        f = self.readfile(resultfile)
        array = []
        re_list = re.findall(r"%s" % searchmode,f, re.S)
        for i in re_list:
            array.append(i)
        return array
# useage
# a=ResultSorting()
# sysbench_mem
# count=2097152
# b=a.datasearch("Operations performed: 2097152 \((.*?)ops\/sec\)", "result.out")
# c=a.datasearch("8192.00 MB transferred \((.*?)MB\/sec\)", "result.out")
# sysbench_cpu
# d=a.datasearch("execution time \(avg\/stddev\):(.*?)\/0.00)", "result.out")

