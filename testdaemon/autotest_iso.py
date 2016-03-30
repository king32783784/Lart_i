#!/usr/bin/env python
#coding=utf8
'''Name:Linux automated regression testing
   Function:Check the ISO changes
   Author:peng.li@i-soft.com.cn
   Time:20160330
'''
import os,sys,time
from common import parsing_xml 

##解析配置文件，"test_setup_info"是个字典，其中'xml_list'对应配置列表；'xml_dict'是一个以配置项为键，其对应设置内容为值的字典" ##
test_setup=Parsing_XML('setup.xml','configlist')
test_setup_info=testsetup.specific_elements()



