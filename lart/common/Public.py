import os
import linecache
import time
from checkid import checkupdateID


def os_name():
    f=open('/etc/os-release','r')
    theline=linecache.getline("/etc/os-release",5)
    osname_line=theline[13:-2]
    osname=osname_line.replace(' ','_')
    return osname

def resultprocess_dir():
    testosname=os_name()
    testID=checkupdateID()
    result_path=testosname + '_' + testID
    process_tool_dir='/var/cache/Isoft-desktop-autotest/Results-Processing/'
    process_result_path=process_tool_dir + 'Source_data/'
    process_source_dir=process_result_path + result_path
    resultprocess_dirname=process_source_dir + '/default'
    resultprocess_list = os.popen('ls %s' %process_result_path).read()
    if resultprocess_dirname not in resultprocess_list:
        os.system('mkdir -p %s' %resultprocess_dirname)
    resultprocessdir={'processresultpath':process_result_path,'processsource':process_source_dir,'resultdirname':result_path,'resultdir':resultprocess_dirname,'processtooldir':process_tool_dir}
    return resultprocessdir


