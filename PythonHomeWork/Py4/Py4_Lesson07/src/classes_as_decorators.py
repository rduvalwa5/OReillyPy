'''
Classes can be decorators too!
'''
class ctrace:
    def __init__(self, f):
        "__init__ records the passed function for later use in __call__()."
        self.__doc__ = f.__doc__
        self.__name__ = f.__name__
        self.f = f
    def __call__(self, *args, **kw):
        "Prints a trace line before calling the wrapped function."
        print("Called", self.f.__name__)
        return self.f(*args, **kw)  
 
@ctrace
def simple(x):
    "Just prints arg and returns it."
    print("simple called with", x)
    return x
    
 
if __name__ == "__main__":    
    simple("walking")
    print(simple.__name__)
    print(simple.__doc__)
    print(dir(simple))
    print(simple.__dict__)
    
    
