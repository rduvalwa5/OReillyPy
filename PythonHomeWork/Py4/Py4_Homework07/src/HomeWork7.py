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
def addarg(arg1):
    def wrap(f):
        def wrapped_f(*args, **kw):
            return f(arg1, *args, **kw)
        return wrapped_f
    return wrap

@addarg(1)
def myfunc(*args, **kwarg):
    return args
    
if __name__ == "__main__":
    print(myfunc("One", "Two"))
    print(myfunc(1, 2, 3))
    print(myfunc(("one", 1), ("two", 2)))
