import os
import subprocess
import tarfile
import shutil
from subprocess import PIPE, Popen, call
from preparetest import TestParpare
from public import ReadPublicinfo


class TestSetup(TestParpare, ReadPublicinfo):
    '''
        Test project settings
    '''

    def decompressfile(self, filepath, filename):
        fileformat = filepath.split('.')[-1]
        tarfilepath = self.mkinstalldir()
        tmpfilepath = os.path.join(tarfilepath, 'packet')
        try:
            filedecompress = tarfile.open("%s" % filepath,
                                          "r:%s" % fileformat)
            filedecompress.extractall(path=tmpfilepath)
            filedecompress.close()
        except IOError as err:
            print "%s decompressfile  error : %s" % (filename, err)
        except tarfile.CompressionError as err:
            print "Decompressfile faild, %s" % err
        bindir = os.path.join(tarfilepath, filename)
        call('mv %s/* %s' % (tmpfilepath, bindir), shell=True)
        return bindir

    def _runsh(self, shcmd):
        try:
            call('sh %s' % shcmd, shell=True)
        except:
            pass

    def _configure(self, args):
        try:
            call('./configure %s' % args, shell=True)
        except:
            pass

    def _make(self, args):
        try:
            call('make clean', shell=True)
        except:
            pass
        try:
            call('make %s' % args, shell=True)
        except:
            pass
    def _rmfile(self, args):
        try:
            os.remove(args)
        except OSError:
            pass

    def _cpfile(self, src, dst):
        try:
            shutil.copy('%s' % src, '%s' % dst)
            print "mv ok"
        except:
            pass
        print "hello"
            
    def pacagemanger(self, *args):
        '''
           Check test tool based on
        '''
        for arg in args:
            try:
                retcode = call('which %s' % arg, shell=True)
                if retcode == 0:
                    return arg
                    break
            except OSError:
                pass

    @staticmethod
    def packageinstall(defectlist):
        packagetool = self.pacagemanger('dnf', 'yum', 'apt-get')
        for defect in defectlist:
            call('%s -y install %s' % (packagetool, defect), shell=True)

# testcase
# test = testsetup()
# test.packageinstall()
# test.toolinstall('sysbench-0..12', 'tmp')
