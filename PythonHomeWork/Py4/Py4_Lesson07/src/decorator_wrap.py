'''
Created on Feb 21, 2014

@author: 310122001
'''
from functools import wraps

def simpledec(f):
    "A really simple decorator to demonstrate functools.wraps"
    @wraps(f)
    def wrapper(arg):
        print("Calling f with arg", arg)
        return f(arg)
    return wrapper    

@simpledec
def f(x):
    'My f function.................. '
    "Simply prints its argument."
    print("Inside f, arg is", x)

if __name__ == "__main__":
    f("Hello")
    print(f.__name__)
    print(f.__doc__)
