'''
http://docs.python.org/2/library/inspect.html
Created on Mar 22, 2014
@author: rduvalwa2
Write a program that imports a module and then goes through the module's namespace to find any functions 
and print the names of the functions and their arguments, in the same way as it might appear in a def statement.
'''

import inspect

def B(a, b, c):
    return a + b + c

def C(x):
    myA = x
    def readA():
        for item in myA:
            print(item)
        return myA

def f(a, b, c, d=3, *, e):
        print("a")

if __name__ == "__main__":
#    from prj9_b import B
#    print(inspect.getmembers(B))
    print(inspect.formatargspec(*inspect.getfullargspec(f)))
#    arg =  inspect.getfullargspec(f)
#    print(arg)
#    for i in arg:
#        print(i)
#        print(inspect.formatargspec(arg[i]))
#        print(func[0],spec)
