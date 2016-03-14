
import os
'''
 Test dependent package setup
'''
class packet_install():

    def __init__(self,name):
        self.name=name

    def check_ostype(self):
        with open('/etc/os-release','r') as f:
            read_data=f.read()
            return read_data
    
    def check_tool(self,install_manager,packetlist):
        packetlistkeys=packetlist.keys()
        for keys in packetlistkeys:
            install_cmd=install_manager + ' ' + 'install -y' + ' ' + packetlist[keys] + '>/dev/null 2>&1'  
            return_value=os.system('which %s >/dev/null 2>&1' %keys)
            if return_value == 0:
                pass
            else:
                try:
                    os.system('%s' %install_cmd)
                except:
                    print '%s install faild' %install_tool

    def check_lib(self,install_manager,libname):
        return_value=os.system('ls %s >/dev/null 2>&1' %libname)
        if return_value == 0:
            pass
        elif 'X11' in libname:
            try:
                os.system('dnf install -y xorg-x11* 2>&1')
            except:
                print '%s install faild' %libname
    
       
def Perf_setup(testtype):
    tool_install=packet_install('tool')
    packetlist={'gcc':'gcc','pandoc':'pandoc','patch':'patch'}
    ptstest_list=['Perf_compression','Perf_encoding','Perf_graphics','Perf_compiler']
    ostypeinfo=tool_install.check_ostype()
    if 'iSoft Desktop' in ostypeinfo or 'Fedora' in ostypeinfo:
        tool_install.check_tool('dnf',packetlist)
    elif 'Deepin' in ostypeinfo:
        tool_install.check_tool('apt-get',packetlist)
    if testtype == 'Perf_cpu':
        if 'iSoft Desktop' in ostypeinfo or 'Fedora' in ostypeinfo:
            packetlist={'aclocal':'automake','libtool':'libtool'}
            tool_install.check_tool('dnf',packetlist)               
        elif 'Deepin' in ostypeinfo:
            packetlist={'aclocal':'automake','libtool':'libtool-bin'}
            tool_install.check_tool('apt-get',packetlist)     
    if testtype == 'Perf_os':
        if 'iSoft Desktop' in ostypeinfo or 'Fedora' in ostypeinfo:
            packetlist={'x11perf':'x11perf'}
            tool_install.check_tool('dnf',packetlist)
            liblist={'/usr/include/X11/Xlib.h':'xorg-x11*'}
            tool_install.check_lib('dnf',liblist)
        elif 'Deepin' in ostypeinfo:
            packetlist={'x11perf':'x11-apps'}
            tool_install.check_tool('apt-get',packetlist)
    if testtype in ptstest_list:
        os.system('pip install pexpect')
        if 'iSoft Desktop' in ostypeinfo or 'Fedora' in ostypeinfo:
            packetlist={'php':'php-xml','wget':'wget'}
            tool_install.check_tool('dnf',packetlist)
        elif 'Deepin' in ostypeinfo:
            packetlist={'php':'php','wget':'wget'}
            tool_install.check_tool('apt-get',packetlist)
