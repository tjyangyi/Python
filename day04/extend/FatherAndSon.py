#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月19日

@author: YangYi
'''
'''新式类'''
class Father(object):
    def __init__(self):
        print('在父亲构造方法中打印的')
        self.fatherName = 'father name'
        
    def funcInFather(self):
        print('父亲干的事情')
        
'''继承'''
class Son(Father):
    def __init__(self):
        Father.__init__(self)
        super(Son,self).__init__()
        print('在儿子构造方法中打印的')
        self.sonName = 'son name'
        
    def funcInSon(self):
        print('儿子干的事')
    
    #重写父类方法
    def funcInFather(self):
        Father.funcInFather(self)
        print('儿子在父亲之后又干了点事')
        
s1 = Son()
s1.funcInSon()
s1.funcInFather()
#print(s1.fatherName) 
print(s1.sonName)

        
        
