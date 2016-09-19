import  xml.dom.minidom
import time

def getupdateid():
    dom=xml.dom.minidom.parse('/etc/update/updates.xml')
    itemlist=dom.getElementsByTagName('updates')
    item=itemlist[0]
    updateid=item.getAttribute("latest")
    return updateid

def setinituid():
    inituid = getupdateid()
    try:
        f = open('uid', 'w')
        f.write(inituid)
        f.closed
    except IOError:
        print "plealse check uid file"

def checkidupdate():
    try:
        f = open('uid', 'r')
        lastuid = f.read().strip()
        newuid = getupdateid()
        while True:
            if newuid > lastuid:
                f.write(newuid)
                f.closed
                break
            else:
                time.sleep(10)
                print "check now"
    except IOError:
        print "plealse check uid file"

setinituid()
checkidupdate()
