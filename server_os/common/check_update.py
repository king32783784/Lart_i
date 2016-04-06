import urllib2
import re
import os
from downloadfile import downloadfile
from public import ReadPublicinfo


class Check_Update(ReadPublicinfo):
    def __init__(self):
        ReadPublicinfo.__init__(self)
        self.setup = self.setup_info()
        self.isoname = self.getisoname()

    def get_htmlcontent(self, xmlurl, remode):
        try:
            html_Context = urllib2.urlopen(xmlurl).read()
        #    print html_Context
        except urllib2.HTTPError:
            print "ok"  # need report this error  to tester by mail
        html_Context = unicode(html_Context, 'utf-8')
        return re.findall(r"%s" % remode, html_Context)

    def getisoname(self):
        xmlurl = self.setup['xml_dict']['isourl'][0]
        remode = "href=\"(.+).iso\">"
        targetiso = self.get_htmlcontent(xmlurl, remode)
        if len(targetiso) == 1:
            return targetiso[0] + '.iso'
        elif len(targetiso) < 1:
            return targetiso  # need report this error  to tester by mail
        else:
            getiso = targetiso[0]
            for iso in targetiso:
                if iso > getiso:
                    getiso = iso
            return getiso + '.iso'

    def getisomd5(self):
        xmlurl = os.path.join(self.setup['xml_dict']['isourl'][0],
                              self.isoname) + '.md5sum'
        remode = "(.+)"
        targetmd5 = self.get_htmlcontent(xmlurl, remode)
        return targetmd5[0]

    def downloadiso(self):
        remode = "href=\"(.+).iso\">"
        isoname = self.get_htmlcontent(self.setup['xml_dict']['isourl'][0],
                                       remode)
        locatedir = os.path.join(self.setup['xml_dict']['isoserver'][0],
                                 self.isoname)
        isourl = os.path.join(self.setup['xml_dict']['isourl'][0],
                              self.isoname)
        downloadfile(locatedir, isourl)
        filemd5 = os.popen('md5sum %s' % locatedir).read()
        md5standard = self.getisomd5()
        if filemd5[0:32] == md5standard[0:32]:
            return "yes"
        else:
            return "no"
'''
test=Check_Update()
test.downloadiso()
'''
'''
def test(url):
    try:
        html_Context = urllib2.urlopen(url).read()
    except urllib2.HTTPError:
        print "ok"
    html_Context = unicode(html_Context, 'utf-8')
    targetiso = re.findall(r"href=\"(.+).iso\">", html_Context)
    if len(targetiso) != 0:
        print targetiso
    else:
        print "no iso"
test("http://192.168.32.18/4.0/")
'''
