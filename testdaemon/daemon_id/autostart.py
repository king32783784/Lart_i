#!/usr/bin/env python
#coding=utf8
'''Name:Isoft Desktop Autotest Tool
   Author:peng.li@i-soft.com.cn
   Time:20160120
'''

import os,sys,time
from checkid import checkupdateID
from downloadfile import downLoadTestFile
from analyticalxml import Analyticaltestlist
from testtool import testtool_extrac
from starttest.perf_test import perf_test
from result_process.Perfresult_process import Perf_result_process

System_order='/var/cache'
Test_order='Isoft-desktop-autotest'
TestXml_dladdress='http://192.168.32.18/4.0'
TestTool_dladdress='http://192.168.32.18/4.0/testtool'

TestListXml_name='TestList.xml'
TestToolPerf_name='autotest-Idat-v1.0.tar.bz2'
TestToolPerf_order='autotest-Idat'
TestPerfResult_order='Performance-result'

PerfRst_toolname='Results-Processing.tar.bz2'
PerfRst_order='Results-Processing'


Test_dir=os.path.join(System_order,Test_order)
TestListXml=os.path.join(Test_dir,TestListXml_name)
TestToolPerf=os.path.join(Test_dir,TestToolPerf_name)
TestPerfResult_dir=os.path.join(Test_dir,TestPerfResult_order)

TestListXml_url=os.path.join(TestXml_dladdress,TestListXml_name)
TestTool_Perf_url=os.path.join(TestTool_dladdress,TestToolPerf_name)

PerfRst_tool=os.path.join(Test_dir,PerfRst_toolname)
PerfRst_tool_url=os.path.join(TestTool_dladdress,PerfRst_toolname)

def env_setup():
    orderlist = os.popen('ls %s -a' %System_order ).read()
    if Test_order not in orderlist:
        os.system('mkdir %s' %Test_dir)
    orderlist = os.popen('ls %s' %Test_dir).read()
    if TestPerfResult_order not in orderlist:    
        os.system('mkdir -p %s' %TestPerfResult_dir)

def createDaemon():
#create -father thread
    try:
        if os.fork() > 0:
            os._exit(0)
    except OSError,error:
        print 'fork #1 failed: %d(%s)' %(error.errno,error.strerror)
        os._exit(1)

    os.chdir('/')
    os.setsid()
    os.umask(0)

#create - child thread
    try:
        pid = os.fork()
        if pid > 0:
            os._exit(0)
    except OSError,error:
        print 'fork #2 failed: %d(%s)' % (error.errno,error.strerror)
        os._exit(1)

    testControl() #function for test control

      
def testControl():
    baseid=checkupdateID()
    while True:
        updatid=checkupdateID()
        if updatid > baseid:
            env_setup()
            downLoadTestFile(TestListXml,TestListXml_url)
            baseid=updatid
            test_sys=Analyticaltestlist(TestListXml)
            test_type=test_sys['xml_type']
            test_list=test_sys['xml_item']
            for test_type_name in test_type:
                if test_type_name == 'performance':
                    orderlist = os.popen('ls %s -a' %Test_dir).read()
                    if TestToolPerf_name not in orderlist:
                        downLoadTestFile(TestToolPerf,TestTool_Perf_url)
                    if TestToolPerf_order not in orderlist:
                        testtool_extrac(TestToolPerf,Test_dir)
                    if PerfRst_toolname not in orderlist:
                        downLoadTestFile(PerfRst_tool,PerfRst_tool_url)
                    if PerfRst_order not in orderlist:
                        testtool_extrac(PerfRst_tool,Test_dir)
                    perf_item_list=test_list['performance']
                    perf_test(perf_item_list)
                    Perf_result_process()
                elif test_type_name == 'info':
                    orderlist = os.popen('ls %s -a' %Test_dir).read()
                    if TestToolPerf_name not in orderlist:
                        downLoadTestFile(TestToolPerf,TestTool_Perf_url)
                elif test_type_name == 'stability':
                #    downLoadTestFile(TestToolStab,TestTool_Stab_url)
                     print 'stability ok'
                elif test_type_name == 'function':
                    downLoadTestFile(TestToolFunt,TestTool_Funt_url)
        time.sleep(10)
if __name__=='__main__':
    createDaemon()
