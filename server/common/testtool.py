import tarfile
import logging

lartlogger = logging.getLogger('Lart_i_server')

def testtool_extrac(testtool_tarfile, testtool_path):
    try:
        testtool_tar = tarfile.open(testtool_tarfile)
        testtool_tar.extractall(path=testtool_path)
        testtool_tar.close()
    except:
        lartlogger.error('\tError extract the testfile:', testtool_tarfile)
        exit(1)
