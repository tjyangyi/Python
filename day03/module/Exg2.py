#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月18日

@author: YangYi
'''

print('正则表达式')
import re

result1 = re.match('\d+', 'sadaseqw232323')
print(result1)
if result1:
    print(result1.group())

result2 = re.search('(\d+)\w*(\d+)', 'sa23daseqw232323')
print(result2)
if result2:
    print(result2.group())
    print(result2.groups())

result3 = re.findall('\d+', '2323sada2323seqw232323')
print(result3)


comp = re.compile('\d+')
print(type(comp))
print(comp.findall('2323sada2323seqw232323'))


