#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月18日

@author: YangYi
'''
print('Time模块')

import time
print(time.time())
print(time.localtime())
print(time.ctime(time.time()))
print(time.gmtime())

'''输出时间字符串'''
print(time.strftime('%Y-%m-%d %H:%M:%S'))

'''字符串转结构化时间'''
print(time.strptime('2014-11-11', '%Y-%m-%d'))

'''结构化时间转时间戳'''
print(time.mktime(time.localtime()))

