import os
import linecache
import time
from parsing_xml import Parsing_XML


def testxmllocate():
    homedir = os.popen('pwd').read().strip('\n')
    local_xmlfile = os.path.join(homedir, 'setup.xml')
    return local_xmlfile


class ReadPublicinfo(Parsing_XML):
    setupxml = testxmllocate()

    def __init__(self):
        self.osname = self.os_name()
        self.setupinfo = self.setup_info()

    def os_name(self):
        f = open('/etc/os-release', 'r')
        theline = linecache.getline("/etc/os-release", 5)
        osname_line = theline[13:-2]
        osname = osname_line.replace(' ', '_')
        return osname

    def setup_info(self):
        '''
test_setup_info is Dictionary.
'xml_list': [u'isourl', u'checkfrequency', u'testtooldir',
u'isoserver', u'resultdir', u'comparingos', u'maillist']
'xml_dict': {u'resultdir': [u'default'], u'isourl':
[u'http://192.168.30.170/iso-images/'], u'testtooldir': 
[u'/var/cache'], u'checkfrequency': [u'60'], u'comparingos':
[u'default'], u'maillist': [u'peng.li@i-soft.com.cn'], u'isoserver':
[u'/var/www/html/testiso/']}}
        '''
        test_setup = Parsing_XML(self.setupxml, 'configlist')
        test_setup_info = test_setup.specific_elements()
        return test_setup_info

#    def testxmllocate(self):
#        homedir = os.popen('pwd').read().strip('\n')
#        local_xmlfile = os.path.join(homedir, 'setup.xml')
#        print local_xmlfile
#        return local_xmlfile
# TEST
# a=ReadPublicinfo()
# print a.setupinfo
