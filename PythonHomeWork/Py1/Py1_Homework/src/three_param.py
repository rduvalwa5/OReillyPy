#!/usr/local/bin/python3
""" three_param.py
    program that processes three parameters """
def my_func(a,b='b was not entered',c='c was not entered'):
       argList = [a,b,c]
       for arg in argList:
         print(arg)

my_func("test")
my_func("test","test")
my_func("test","test","test")
print(my_func)
