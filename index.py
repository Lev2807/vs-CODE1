# import json

# with open('j.json') as file:
#     res = json.load(file)

# print(res)


# from icecream import ic

# def foo(i):
#     return i + 333

# ic(foo(123))


# ic(foo(123), 1 + 5)

# d = {'key': {1: 'one'}}
# ic(d['key'][1])

# class klass():
#     attr = 'yep'

# ic(klass.attr)



# import json

# with open('j.json') as f:
#     templates = json.load(f)

# print(templates)


# import platform

# print(platform.platform())

# print(platform.system())


# import csv

# with open('j.csv') as f:
#     reader = scv.reader(f)
#     for row in reader:
#         print(row)


# import yaml
# from yaml.loader import SafeLoader

# yml = """
# ---
#   UserName: Alicia
#   Password: pinga123* 
#   phone: (495) 555-32-56
#   room: 10
#   TablesList:
#         - EmployeeTable
#         - SoftwaresList
#         - HardwareList 
# ...
# """

# data = yaml.load(yml, Loader=SafeLoader)

# print(data)


# import yaml
# from yaml.loader import SafeLoader

# with open('j.yaml') as f:
#     data = yaml.load(f, Loader=SafeLoader)
#     print(data)


# import pandas as pandas
# my_series = pd.Series([5, 6, 7, 8, 9, 10])
# print(my_series)



# try:
#     a = int(input())
#     b = int(input())

#     print(a / b)

# except(ZeroDivisionError, ValueError ):
#     print('Неможливо')

# import random

# try:
#     a = [1, 2, 3, 4, 5]
#     b = random.randint(0, 10)

#     print(a[b])

# except(IndexError):
#     print('Неможливо')


# class A:
#     @staticmethod
#     def printData(name):
#         print(name)

# v = A()
# v.printData('Lev')


# import pandas as pd
# my_series = pd.Series([5, 6, 7, 8, 9, 10])
# print(my_series)


# from collections import deque

# a = deque([1, 2, 3, 4, 5,])
# a.popleft()
# a.pop()
# a.append(20)
# a.appendleft(30)

# print(a)


# from collections import deque

# a = deque([1, 2, 3, 4, 5])
# a.appendleft(1)
# a.appendleft(2)
# a.pop()
# a.pop()

# print(a)


# import uuid

# random_uuid = uuid.uuid1()

# print(random_uuid)


# from collections import namedtuple

# Person = namedtuple('Person', ['a', 'b'])

# res = Person('123', '123')

# print(res.a, res.b)


# from collections import Counter

# a = Counter([1, 2, 3, 4, 5, 6, 7])

# print(a)


# a = (1, 2, 3, 4, 5)
# a = list(a)

# for i in a:
#     print(i)


# from enum import Enum

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

# print(Color)
# print(Color.RED)
# print(Color.RED.value)

# print(len(Color))
# print(list(Color))


# class A:
#     a = 'Lev'
#     b = 'Roman'

# class B(A):
#     def printData(self):
#         print(len(self.a))
#         print(len(self.b))

# v = B()
# v.printData()


# class Person1:
#     def  printName(self):
#         print('Pasha')

# class Person2(Person1):
#     def printName(self):
#         print('Lev')

# m = Person2()
# m.printName()


# class ABC:

#     def __init__(self, name):
#         self.__name = name

#     @property

#     def printData(self):
#         return self.__name

#     @printData.setter
#     def printData(self, newName):
#         self.__name = newName

# a = ABC('Lev')

# print(a.printData)

# a.printData = 'Roma'

# print(a.printData)
        

# class A:
#     a = 'Lev'

# class B:
#     b = 'Lev'

# class C(A, B):
#     def printData(self):
#         if self.a == self.b:
#             print('+')
        
#         else:
#             print('-')

# v = C()
# v.printData()


# class ABC:
#     def __init__(self, a):
#         self.__a = a

#     def printData(self, value):
#         print(self.__a[value])

# v = ABC([1, 2, 3, 4, 5])
# v.printData(3)


# class Person:
#     __name = 'Lev'

#     @property
#     def getName(self):
#         return self.__name

#     @getName.setter
#     def getName(self, newName):
#         self.__name = newName

# a = Person()
# print(a.getName)

# a.getName = 'Roma'
# print(a.getName)


# a = -13
# print(abs(a))


# print(chr(67))


# a = [1, 2, 3, 4]

# print(dir(a))

# b = (1, 2, 3, 4)

# print(dir(b))


# str1 = 'Lev'

# print(list(enumerate(str1)))


# a = [6, 4, 7, 3]
# i = iter(a)

# print(next(i))
# print(next(i))


# a = [-1, -2, -3, -4]

# print(abs(a[0]))
# print(abs(a[1]))
# print(abs(a[2]))
# print(abs(a[3]))


# a = [-1, -2, -3, -4, -1, -2, -3, -4, -1, -2, -3, -4]

# for i in a:
#     print(abs(i))


# a = {1:1, 2:2}

# print(dir(a))


# class Person:
#     def printData(self):
#         print('Hello world')

# class Person2(Person):
#     def printData(self):
#         print('Lev')
#         super().printData()

# v = Person2()
# v.printData()


# class A:
#     def __init__(self, str1):
#         self.str1 = str1

# class B(A):
#     def printData(self):
#         print(self.str1)

# v = B('qwertyu')
# v.printData()


# import re
 
# text = "Карта map и объект bitmap - это разные вещи"
# match = re.findall("\\bmap\\b", text)
# print(match)

