import  xml.dom.minidom

def checkupdateID():
    dom=xml.dom.minidom.parse('/etc/update/updates.xml')
    itemlist=dom.getElementsByTagName('updates')
    item=itemlist[0]
    updateid=item.getAttribute("latest")
    return updateid

