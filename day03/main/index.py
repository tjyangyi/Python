#!/usr/bin/env python
#coding:utf-8
'''
create
@author: YangYi
'''

print(__name__)
print(__file__)
print(__doc__)

def foo(name):
    print(name,'去砍柴')
    print(login('alex'))
    
    
def login(username):
    if username == 'alex':
        return True
    else:
        return False
    
foo('alex')