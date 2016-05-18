#!/usr/bin/env python
# coding:utf-8
'''
Created on 2016年5月17日

@author: YangYi
'''

import random

print('随机数,验证码')
print(random.random())
print(random.randint(1, 5))
print(random.randrange(1, 3))

temp = random.randint(65, 90)
print(chr(temp))

code = []
for i in range(6):
    if i == random.randint(0, 5):
        code.append(str(random.randint(0, 9)))
    else:
        temp = random.randint(65, 90)
        code.append(chr(temp))
s = ''.join(code);
print(type(s))
print(s)

print('MD5')
import hashlib
hashCode = hashlib.md5()
print(type(hashCode))
hashCode.update('admin');
print(hashCode.hexdigest())
print(hashCode.digest())

print('序列化和JSON')
import pickle
data = {'k1':123, 'k2':'hello'}
print(data)

print('把对象序列化为字符串形式')
dumped = pickle.dumps(data)
print(dumped)
print(type(dumped))

print('把字符串形式反序列化为对象')
loaded = pickle.loads(dumped)
print(loaded)
print(type(loaded))

print('将对象序列化到文件')
pickle.dump(data, open('D://temp.pk', 'wb'))

print('将文件反序列化为对象')
result = pickle.load(open('D://temp.pk', 'rb'))
print(result)

print('转JSON')
import json
jsonResult = json.dumps(data)
print(jsonResult)

dataFromJson = json.loads(jsonResult);
print(dataFromJson)
print(type(dataFromJson))











