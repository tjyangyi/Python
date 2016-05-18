#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月18日

@author: YangYi
'''
str1 = 'Demo'
str2 = 'foo'

modul = __import__(str1)
func = getattr(modul, str2)
func()


