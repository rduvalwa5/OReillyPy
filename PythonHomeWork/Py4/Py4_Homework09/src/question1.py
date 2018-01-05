'''
Created on Mar 31, 2014

@author: 310122001
'''
import inspect
class A():
    zz = []
    yy = "12334"
    vv = 123
    def __init__(self):
        pass
    def __call__(self):
        pass
    def a(self):
        print("A")
    def b(self):
        print("A")
    def c(self):
        print("C")
    def d(self):
        print("D")       
if __name__ == "__main__":
    cls = A()
    for item in inspect.getmembers(cls):
        if hasattr(cls, item[0]) == True:
            print(item , inspect.ismethod(getattr(cls, item[0])))
        else:
            print(item, " Not in " , cls)
            
    if hasattr(cls, 'm') == True:
        print(item , inspect.ismethod(getattr(cls, item[0])))
    else:
        print(item[0], "returns" , hasattr(cls, item[0]))
