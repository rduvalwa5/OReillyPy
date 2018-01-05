'''
Created on Feb 28, 2014
Using a parameterized decorator
@author: 310122001
'''

counts = {}

def countable(ftype):
    "Returns a decorator that counts each call of a function against ftype."
    def decorator(f):
        "Decorates a function and to count each call."
        def wrapper(*args, **kw):
            "Counts every call as being of the given type."
            try:
                counts[ftype] += 1
            except KeyError:
                counts[ftype] = 1
            print("f ", f)
            return f(*args, **kw)
        print ("Wrapper ", wrapper)
        return wrapper
    print("decorator ", decorator)
    return decorator

@countable("short")
def f1(a, b=None):
    print("f1 called with", a, b)

@countable("f2")
def f2():
    print("f2 called")

@countable("short")
def f3(*args, **kw):
    print("f3 called:", args, kw)
    return args, kw

if __name__ == "__main__":
    for i in range(10):
        f1(1)
        f2()
        f3(i, i * i, a=i)
result = f3(i, i * i, a=i)
print("result ", result)
    
