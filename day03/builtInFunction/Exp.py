#!/usr/bin/env python
# coding:utf-8

'''
内置函数
'''


a = []
a1 = list()

b = ()
b1 = tuple()

d = {}

print(dir(a))
print(vars())
print(type(a))
print(type(a1))
print(type(b))
print(type(b1))
print(type(d))

t1 = 1
t2 = 2
print(id(t1))
print(id(t2))


print(cmp(2, 1))
print(abs(-1))
print(bool(2))
print(divmod(7, 4))
print(type(divmod(7, 4)))
dm = divmod(7, 4)
print(dm[0])

print('最大值：')
print(max(1, 2, 3, 4))
print('最小值：')
print(min(1, 2, 3, 4))
print('幂：')
print(pow(2, 5))
print('长度：')
print(len('我的天呐'))
print(len(dm))

print('判断是否所有都为真')
print(all([1, 2, 3, 0]))
print('判断是否有任何一个为真')
print(any([1, 2, 3, 0]))

print('空字符串的布尔值')
print(bool(None))

print('数字转字母')
print(chr(66))
print('字母转数字')
print(ord('a'))
print('十六进制')
print(hex(20))
print('二进制')
print(bin(20))
print('八进制')
print(oct(20))

print(range(3))
print(xrange(3))

li = ['手表', '汽车', '房子']
for item in enumerate(li):
    print(item[0], item[1])
    
    
s = '占位符展示{0},{1}'
print(s.format('alex', 'ds'))

def func(arg):
    print(arg)
    
def add100(arg):
    return arg + 100

li = [11, 22, 33]
print('map的使用:')
print(map(add100, li))
print(map(lambda arg:arg + 100, li))









