'''
Created on Feb 27, 2014
Using a class decorator to wrap each method
@author: 310122001
'''

from decorator_syntax import trace

def callable(o):
    return hasattr(o, "__call__")

def mtrace(cls):
    for key, val in cls.__dict__.items():
        if key.startswith("_") and key.endswith("_") or not callable(val):
            continue
        setattr(cls, key, trace(val))
        print(cls, key, trace(val))
        print("Wrapped", key)
    return cls

@mtrace
class dull:
    def method1(self, arg):
        print("Method 1 called with arg", arg)
    def method2(self, arg):    
        print("Method 2 called with arg", arg)

d = dull()
d.method1("Hello")
d.method2("Goodbye")

'''
Wrapped method2
Wrapped method1
Entering method1
Method 1 called with arg Hello
Leaving method1
Entering method2
Method 2 called with arg Goodbye
Leaving method2
'''
