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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    # pass
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
