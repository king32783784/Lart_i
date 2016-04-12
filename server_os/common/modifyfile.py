import re


class ModifyFile():
    def __init__(self, newcontent, oldcontent, modifyfile):
        self.newcontent = newcontent
        self.oldcontent = oldcontent
        self.modifyfile = modifyfile
        self._modifyfile()

    def _modifyfile(self):
        fp = open(self.modifyfile, 'r')
        filelines = fp.readlines()
        fp.close()
        fp = open(self.modifyfile, 'w')
        for eachline in filelines:
            filebuffer = re.sub(self.oldcontent, self.newcontent, eachline)
            fp.writelines(filebuffer)
        fp.close()

# test case
# ip = ModifyFile("--ip=192.168.32.48", "--ip=192.168.32.47", "ks.cfg")
