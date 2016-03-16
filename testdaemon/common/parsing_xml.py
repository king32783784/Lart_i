#coding=utf8
import os,sys
import xml.dom.minidom
#from downloadfile import downLoadTestFile

class Parsing_XML():
    '''Parsing XML-formatted files for Lart_i'''
    def __init__(self,xml_file_name,Tagname='labelname'):
        self.xmlfile=xml_file_name
        self.Tagname=Tagname

    def parsing_label_list(self,labelname):
        '''Parsing Gets the list labels'''
        xml_dom=xml.dom.minidom.parse(self.xmlfile)
        xml_label=xml_dom.getElementsByTagName(labelname)
        xml_label_list=[]
        for single_label in xml_label:
            xml_label_list.append(single_label.firstChild.data)
        return xml_label_list       

    def specific_elements(self):
        '''Read the specific elements,call the class may need to override this function
By default returns a "xml_list" and "xml_dict" a dictionary of xml_list specify a label for the list xml_dict key for the XML element, the corresponding value for a list of corresponding element tag content
        '''
        xml_labels=self.parsing_label_list(self.Tagname)
        xml_elements_dict={}
        for per_label in xml_labels:
            per_xml_label_list=self.parsing_label_list(per_label)
            xml_elements_dict[per_label]=per_xml_label_list
        xml_dict={'xml_list':xml_labels,'xml_dict':xml_elements_dict}
        return xml_dict

'''
sample:
setupxml=Parsing_XML('TestList.xml','Selecttype')
print setupxml.specific_elements()
'''
