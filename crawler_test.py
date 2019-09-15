# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:14:40 2019

@author: zsh
"""

import urllib.request
import urllib.parse

#打开python官网
response = urllib.request.urlopen('https://www.python.org')

#得到python官网源代码
#print(response.read().decode('utf-8'))

#查看response类型，为HTTPResponse类型的对象，该对象含有许多方法
#print(type(response))

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())