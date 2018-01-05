'''
Created on Mar 31, 2014
A Method is only associated with a CLASS
@author: red
'''
import inspect

class o():
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
    findItems = ['a', 'b', 'm', 'd', 'zz', 'yy']  
    def determineMethod(cls, item): 
            if hasattr(cls, item):
                print(item, type(getattr(cls, item)))
                if inspect.ismethod(getattr(cls, item)):
                    return inspect.ismethod(getattr(cls, item))
                else:
                    return inspect.ismethod(getattr(cls, item))                                
            else:
                print(item)
                return hasattr(cls, item)
            
    cls = o()
    for item in findItems:        
        print(determineMethod(cls, item))
