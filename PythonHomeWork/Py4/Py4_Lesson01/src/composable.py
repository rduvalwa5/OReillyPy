"""
composable.py: defines a composable function class.
"""

import types
class Composable:

    def __init__(self, f):
        print("__init__", f.__name__, type(f))
        "Store reference to proxied function."
        self.func = f
    def __call__(self, *args, **kwargs):
        print("__call__", self.func.__name__)
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    def __mul__(self, other):
        print("__mul__", other)
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            print("MUL if")
            def anon(x):
                print("Returning if anon", self.func(other.func(x)))
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            print("MUL elif")
            def anon(x):
                print("Returning elif anon", self.func(other(x)))
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(
                            self.func.__name__, id(self))

if __name__ == '__main__':
    def f(x):
        return x * x
    
    for x in (1, 2, 3, 4, 0, -1):  # ,"a"):
            f2 = Composable(f)
            a = f2 * f2
            print("a result is ", a(x))

    
