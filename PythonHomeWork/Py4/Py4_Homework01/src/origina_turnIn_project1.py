"""
composable.py: defines a composable function class.
Here are your instructions:
1. Extend the final definition of the composable object to allow it to be raised to positive integer powers. 
   This will require defining the __pow__ method. 
2. For the purposes of this exercise assume that f**2 is the same as f*f, f**3 is the same as f*f*f, and so on. 
   So (f**3)(x) is f(f(f(x))). 
3. If the argument is not an integer, the method should raise a TypeError exception, 
   and a ValueError if its value is non-positive.
"""
import types
class Composable:
    
    def __init__(self, f):
        "Store reference to proxied function"
        self.func = f
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all argumnents through"
        if  isinstance(args[0], int):
            return self.func(*args, **kwargs) ** args[0]
        else:
            return self.func(*args, **kwargs)
    def __mul__(self, other):
        "Return the compostion of proxied ad another function"
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
        
    def __repr__(self):
        return "<Composable function {0} at 0x{1:x}".format(self.func.__name, id(self))
    
if __name__ == '__main__':
    
    @Composable
    def f(x):
        return x * x
    
    print(f(4))
