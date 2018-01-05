'''
http://www.artima.com/weblogs/viewpost.jsp?thread=240845
Created on Mar 5, 2014
Here are your instructions:
Write a decorator function addarg() that takes an argument and adds that argument as the first argument to all calls to decorated functions.
 So if you wrote:
--------------------
@addarg(1)
def prargs(*args):
 return args
prargs(2, 3)
prargs("child") 
--------------------
the output would be: 
-
(1, 2, 3)
(1, 'child')
Write a test program to verify the decorator's operation.
-
Note: it's possible the wrapped function will have keyword arguments and these should 
be respected.
@author: 310122001
'''

def addarg(f):
    def deco(*args, **kw):
        print("Entering", f.__name__)
        result = f(*args, **kw)
        print("Leaving", f.__name__)
        return result
    return deco

@addarg("Xx")
def myfunc(x, a):
    'My myfunc.................. '
    print("Inside", myfunc)
    print("X:", x, "a", a)
    
if __name__ == "__main__":
    myfunc("One", "Two")
