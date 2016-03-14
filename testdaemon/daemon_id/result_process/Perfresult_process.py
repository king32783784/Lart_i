import os, time
from Public import resultprocess_dir 
from Auto_mail import automail_result

def Perf_result_process():
    time_stamp=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    resultprocess=resultprocess_dir()
    result_dirname=resultprocess['resultdirname']
    result_toolpath=resultprocess['processtooldir']
    result_dirpath=resultprocess['processsource']
    result_finaltardir=resultprocess['processresultpath']
    result_dir=resultprocess['resultdir']
    Perf_resultlist=os.popen('ls %s' %result_dir).read()
    Perf_resultlist=Perf_resultlist.replace('\n',' ')
    process_cmd='sh mkresult' + ' ' + '-d' + ' ' + result_dirpath + ' ' + '-i' + ' ' + '"' + Perf_resultlist + '"' + ' ' + '-s' + ' ' + '"' + result_dirname + '"'
    Homedir=os.popen('pwd').read()
    Homedir=Homedir.replace('\n','/')
    os.chdir(result_toolpath)
    os.system('%s' %process_cmd)
    os.chdir('Source_data')
    result_tar=result_dirname + '_' + time_stamp + '.tar.bz2'
    tar_cmd='tar jcf' + ' ' + result_tar + ' ' + result_dirname 
    os.system(tar_cmd)
    os.chdir(Homedir)
    result_finaltarpath=result_finaltardir+result_tar
    automail_result(result_finaltarpath,result_dirname,result_tar)
       
    
