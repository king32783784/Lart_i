import os,sys,shutil,time
import linecache,re
from perf_setup import Perf_setup
from daemon_id.Public import os_name,resultprocess_dir
'''Performance test control.This test control by autotest'''

class Run_perftest():

    def run_once(self,testitem_control='pts_grahics-control',testitem_result='pts.graphics'):
        cmd_main='python /var/cache/Isoft-desktop-autotest/autotest-Idat/client/autotest-local'
        cmd_control='/var/cache/Isoft-desktop-autotest/autotest-Idat/client/client-test-control/%s' %testitem_control
        cmd_out='--out=/var/cache/Isoft-desktop-autotest/Performance-result/%s' %testitem_result
        cmd_log='>>/var/cache/Isoft-desktop-autotest/testlog 2>&1'
        cmd=cmd_main + ' ' + cmd_control + ' ' + cmd_out + ' ' + cmd_log
        os.system(cmd)
     
    def mvresult(self,testitem_result='Perf_info',testtool_path='infotest'):
        Targetdir_dict=resultprocess_dir()
        Target_dir=Targetdir_dict['resultdir']
        path_main='/var/cache/Isoft-desktop-autotest/Performance-result/'
        path_testitem='%s' %testitem_result
        path_testtool='/results/default/%s' %testtool_path
        path_all_tmp=os.path.join(path_main,path_testitem)
        path_all=path_all_tmp + path_testtool
        path_target=os.path.join(Target_dir,testtool_path)
        shutil.copytree(path_all,path_target)      

def perf_test(perf_testlist):
    run_test=Run_perftest()
    for perftest in perf_testlist:
        Perf_setup(perftest)
    run_test.run_once(testitem_control='Systeminfo-control',testitem_result='Perf_info')
    run_test.mvresult(testitem_result='Perf_info',testtool_path='infotest')
    for perftest in perf_testlist:
        if perftest == 'Perf_cpu':
            run_test.run_once(testitem_control='sysbench_CPU-control',testitem_result='Perf_cpu')
            run_test.mvresult(testitem_result='Perf_cpu',testtool_path='sysbench.cpu')
        elif perftest == 'Perf_thread':
            run_test.run_once(testitem_control='pingpong-control',testitem_result='Perf_thread')
            run_test.mvresult(testitem_result='Perf_thread',testtool_path='pingpong')
        elif perftest == 'Perf_mem':
            run_test.run_once(testitem_control='sysbench_MEM-control',testitem_result='Perf_mem')
            run_test.mvresult(testitem_result='Perf_mem',testtool_path='sysbench.mem')
        elif perftest == 'Perf_io':
            run_test.run_once(testitem_control='iozone-control',testitem_result='Perf_io')
            run_test.mvresult(testitem_result='Perf_io',testtool_path='iozone')
        elif perftest == 'Perf_net':
            run_test.run_once(testitem_control='netperf-control',testitem_result='Perf_net')
            run_test.mvresult(testitem_result='Perf_net',testtool_path='netperf2')
        elif perftest == 'Perf_os':
            run_test.run_once(testitem_control='unixbench-control',testitem_result='Perf_os')
            run_test.mvresult(testitem_result='Perf_os',testtool_path='unixbench5')
        elif perftest == 'Perf_compression':
            run_test.run_once(testitem_control='pts_compress-control',testitem_result='Perf_compression')
            run_test.mvresult(testitem_result='Perf_compression',testtool_path='pts.compression')
        elif perftest == 'Perf_encoding':
            run_test.run_once(testitem_control='pts_encoding-control',testitem_result='Perf_encoding')
            run_test.mvresult(testitem_result='Perf_encoding',testtool_path='pts.encoding')
        elif perftest == 'Perf_graphics':
            run_test.run_once(testitem_control='pts_graphics_control',testitem_result='Perf_graphics')
            run_test.mvresult(testitem_result='Perf_graphics',testtool_path='pts.graphics')
        elif perftest == 'Perf_compiler':
            run_test.run_once(testitem_control='pts_graphics_control',testitem_result='Perf_compiler')
            run_test.mvresult(testitem_result='Perf_compiler',testtool_path='pts.compiler')
