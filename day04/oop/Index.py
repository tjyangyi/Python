#!/usr/bin/env python
# coding:utf-8
'''
Created on 2016年5月19日

@author: YangYi
'''

class Person(object):
    bloodType = 'o'  # 静态字段
    
    #构造函数
    def __init__(self, name, privateValue):
        self.name = name  # 动态字段
        self.__privateValue = privateValue  # 私有字段
        
    #析构函数
    def __del__(self):
        print('解释器要销毁我了')
    
    def __call__(self):
        print('执行了call方法')
    
    # 只读
    @property
    def getPrivateValue(self):
        return self.__privateValue
    
    # 可写
    @getPrivateValue.setter
    def setPrivateValue(self, value):
        self.__privateValue = value
    
    # 静态方法
    @staticmethod
    def doStatic():
        print('this is static method')
        
    # 动态方法
    def do_something(self):
        print(self.name + ' is doing something')
    
    # 把方法的访问形式转化为字段的访问形式
    @property 
    def bar(self): 
        print(self.name)
        return 'bar_return'
    
    # 私有方法
    def __private_method(self):
        print('这是私有方法')
        
    


p1 = Person('YangYi', 'GouZi')
p1.name = 'yy'
print(p1.name)
print(Person.bloodType)
p1.do_something()
Person.doStatic()
print(p1.bar)    
p1.setPrivateValue = 'Cat'
print(p1.getPrivateValue)
'''执行对象的CALL方法'''
p1()
