#!/usr/bin/env python
# coding:utf-8
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



def myFilter(before_fuc, after_func):
    def outer(main_func):
        def wrapper(request, kargs):
            before_result = before_fuc(request, kargs)
            if(before_result != None):
                return before_result
            main_result = main_func(request, kargs)
            if(main_result != None):
                return main_result
            after_result = after_func(request, kargs)
            if(after_result != None):
                return after_result
        return wrapper
    return outer            
    
def before_fuc(request, kargs):
    print('enter before_fuc')
    print('in before_fuc', request)
    print('in before_fuc', kargs)
    #return 'before_fuc返回值'
    
def after_func(request, kargs):
    print('enter after_func')
    print('in after_func', request)
    print('in after_func', kargs)
    #return 'after_func return value'
            
@myFilter(before_fuc, after_func)
def test(request, kargs):
    print('enter main_func')
    #return 'main_func return value'
    
test(1, 1)


