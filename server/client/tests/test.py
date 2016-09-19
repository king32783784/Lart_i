#!/usr/local/bin/python
#coding:utf-8
import re
fopen=open(r'result.out','r')
f=fopen.read().strip()

print "输出1.txt文件内容"
print f
print "---------------------------------------"

print "贪婪匹配,re.S('.'匹配字符,包括换行符)"

array=[]
re_list=re.findall(r"execution time \(avg\/stddev\):(.*?)\/",f,re.S)
for i in re_list:
    array.append(i)
for i in array:
    print i
