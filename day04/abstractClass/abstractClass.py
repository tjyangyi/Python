#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月19日

@author: YangYi
'''
from abc import ABCMeta,abstractmethod

class Bar:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Fun(self):
        pass
    
class Foo(Bar):
    def __init__(self):
        print('__init__')
        
    def Fun(self):
        Bar.Fun(self)
        
Foo()

