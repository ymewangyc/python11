#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print ('''line1
line2
line3''')

print(r'''hello,\n
world''')

print('包含中文的str')

print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

# -- coding: utf-8 --
n1 = 255
n2 = 1000

print(hex(n1),hex(n2))

def f(x):
    return str(hex(x))
n1=255
n2=1000
print(f(n1))
print(f(n2))
