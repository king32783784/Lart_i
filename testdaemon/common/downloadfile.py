import os,urllib2,urllib

def downLoadTestFile(local_dir,url):
    try:
        response = urllib2.urlopen(url)
        urllib.urlretrieve(url, local_dir)
    except :
        print '\tError download the file:',local_dir
        exit(1)
