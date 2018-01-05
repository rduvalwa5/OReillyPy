'''
http://docs.python.org/2/library/inspect.html
Created on Mar 22, 2014
@author: rduvalwa2
Write a program that imports a module and then goes through the module's namespace to find any functions 
and print the names of the functions and their arguments, in the same way as it might appear in a def statement.
'''

import inspect
from arr import array

def B(a,b,c):
    return a + b + c

def C(x):
    myA = x
    def readA():
        for item in myA:
            print(item)
        return myA

class A:
    a=10
    b=20
    def __init__(self,input):
            self.c=input

    def multiply(self,number):
        return self.a * self.b * number
    
    def divide(self, i):
        return a*b/i

    def cube(self,multiplier):
        return (a*b)**multiplier
    
    def print_out(self):
        print(self.multiply())

def get_user_attributes(cls):
    boring = dir(type('dummy', (object,), {}))
    return [item
            for item in inspect.getmembers(cls)
            if item[0] not in boring]
            
if __name__ == "__main__":
    inspectItem = A
    print(inspect.getmembers(inspectItem,inspect.isfunction))
#    print("Name  ",A.__name__)
#    print("Func", inspect.formatargspec(*inspect.getfullargspec(A.__init__)))
    print(inspect.getmembers(inspectItem,inspect.isfunction))
    for ob in inspect.getmembers(inspectItem,inspect.isfunction):
        print(ob[0])
        fun = inspectItem.__name__ + "." + ob[0]
        print("fun ", fun)
        arguments = inspect.formatargspec(inspect.getfullargspec(ob[1]))
        print(arguments)
        print(inspectItem.__name__ + "." + ob[0] + arguments)
#        print(inspect.formatargspec(*inspect.getfullargspec(A.__init__)))
#        print(inspect.getfullargspec(ob[1]))
#    print(inspect.formatargspec(*inspect.getfullargspec(B)))
#    BBB = inspect.formatargspec(*inspect.getfullargspec(B))
#    print("BBB ", BBB)

#    print(inspect.getmembers(array,inspect.isfunction))
#    for ob in inspect.getmembers(array,inspect.isfunction):
#        print(ob[0])
#        print(inspect.getfullargspec(ob[1]))
#        arguments = inspect.getfullargspec(ob[1])
#        print("ARGS ",arguments)
#        for bar in inspect.getfullargspec(ob[1]):
#            print(bar)