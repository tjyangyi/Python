#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月18日

@author: YangYi
'''

def outer(fun):
    def wrapper(arg):
        print('验证')
        result = fun(arg)
        print('日志')
        return result
    return wrapper

@outer
def func1(arg):
    print('func1')
    print(arg)
    return '原函数返回值'

ret = func1('代入原函数的参数')
print(ret)