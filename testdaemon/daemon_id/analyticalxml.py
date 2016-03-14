#coding=utf8
import os,sys
import xml.dom.minidom
from downloadfile import downLoadTestFile
'''Analytical Test xml'''
def Analyticaltestlist(Testxml):
    xml_dom = xml.dom.minidom.parse(Testxml)
    xml_document=xml_dom.documentElement
    xml_testtype=xml_dom.getElementsByTagName('Selecttype')
    xml_testtypelist=[]
    for i in xml_testtype:
        xml_testtypelist.append(i.firstChild.data)
    xml_testitemdict={}
    for xml_selecttype in xml_testtypelist:
        xml_testitem=xml_dom.getElementsByTagName(xml_selecttype)        
        xml_testitemlist=[]
        for i in xml_testitem:
            xml_testitemlist.append(i.firstChild.data)
        xml_testitemdict[xml_selecttype]=xml_testitemlist
    xml_test={'xml_type':xml_testtypelist, 'xml_item':xml_testitemdict}     
    return xml_test
