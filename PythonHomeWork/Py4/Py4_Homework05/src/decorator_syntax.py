'''
Created on Feb 17, 2014
 function is a decorator syntax
 decorator_syntax.py
@author: rduvalwa2
'''
def trace(f):
    "TRACE: Decorate a function to print a message before and after execution."
    def traced(*args, **kw):
        print("Entering", f.__name__)
        result = f(*args, **kw)
        print("Leaving", f.__name__)
        return result
    return traced

@trace
def myfunc(x, a=None):
    'My myfunc.................. '
    print("Inside", myfunc)
    print("X:", x, "a", a)

@trace
def myMultiplier(x, y):
    "My Multiplier........."
    return pow(x, y)

@trace
def myAdder(x, y):
    "My myAdder...................."
    return x + y

if __name__ == "__main__":
    myfunc("One", "Two")
    n = myMultiplier(5, 6)
    print("myMultiplier output ", n)
    a = myAdder('a', 'b')
    print('myAdder("a","b")', a)
    a = myAdder(5, 6)
    print('myAdder(5,6)', a)
    print(trace.__name__)
    print(myfunc.__name__)
    print(myMultiplier.__name__)
    print(myAdder.__name__)
    print(trace.__doc__)
    print(myfunc.__doc__)
    print(myMultiplier.__doc__)
    print(myAdder.__doc__)
