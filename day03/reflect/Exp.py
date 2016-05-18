#!/usr/bin/env python
#coding:utf-8

import day03.reflect.mysqlhelper as mysqlhelper
import day03.reflect.sqlserverhelper as sqlserverhelper

a = '8*8'
print(eval(a))

print(sqlserverhelper.count())
print(mysqlhelper.count())

Function = getattr(sqlserverhelper, 'count');
print(Function())






#反射

