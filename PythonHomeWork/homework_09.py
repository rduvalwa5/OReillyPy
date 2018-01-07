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
    def __init__(self,i):
            self.c=i

    def multiply(self,i):
        return self.a * self.b * i
    
    def print_out(self):
        print(self.multiply())

def get_user_attributes(cls):
    boring = dir(type('dummy', (object,), {}))
    return [item
            for item in inspect.getmembers(cls)
            if item[0] not in boring]
            
if __name__ == "__main__":
#    print(inspect.getargspec(A.multiply))
#    t = A(1)
    print("isFunc ",inspect.isfunction(B))
    print("GetArgSpec ",inspect.getargspec(B))
    print("CallArgs ",inspect.getcallargs(B,1,2,3))
    print("GetArgs ",inspect.getcallargs(B,1,2,3))
    print("GetValues ",inspect.ArgInfo(B,"a","b","c"))
    print("GetMembers ", inspect.getmembers(A,inspect.isfunction))
    print(" ", inspect.ArgInfo(B,1,2,3))
    print(inspect.getsourcelines(B))
    print(inspect.getsourcelines(A))    
    print(inspect.getsourcelines(array))
#    print(" ", inspect.CO_VARARGS(B))
    
#    print(inspect.getmembers(A,inspect.isfunction))
#    for ob in inspect.getmembers(A,inspect.isfunction):
#        print(ob[0])
#        print(inspect.getfullargspec(ob[1]))
#    print(inspect.getmembers(array,inspect.isfunction))
#    for ob in inspect.getmembers(array,inspect.isfunction):
#        print(ob[0])
#        print(inspect.getfullargspec(ob[1]))
#        arguments = inspect.getfullargspec(ob[1])
#        print("ARGS ",arguments)
#        for bar in inspect.getfullargspec(ob[1]):
#            print(bar)