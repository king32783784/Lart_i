import os
from parsing_xml import Parsing_XML


class ParameterAnalysis(Parsing_XML):

    def baseparameter(self, doitem):
        test = Parsing_XML(self.xmlfile, '')
        itembasecmd = test.parsing_label_list(doitem)
        test = itembasecmd[0].split(' ')
        itembasecmd = {}
        for pertest in test:
            testa = pertest.split('=')
            itembasecmd[testa[0]] = testa[1]
        return itembasecmd

    def specificparameter(self):
        pass

    def test_reboot(self):
        pass

    def run_cmd(self):
        pass

#testcase
#test = ParameterAnalysis('Test_parameter.xml', '')
#a = test.baseparameter('Perf_cpu')
