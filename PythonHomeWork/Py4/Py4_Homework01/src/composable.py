"""
composable.py: defines a composable function class.
"""
import types
class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
    def __call__(self, *args, **kwargs):        
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    def __mul__(self, other):
        "Return the composition of proxied and another function."
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
        return "<Composable function {0} at 0x{1:X}>".format(
                            self.func.__name__, id(self))
        
    def __pow__(self, i):
        if False == isinstance(i, int):
            raise TypeError
        elif i < 1:
            raise ValueError   
        else:  
            result = self
            for z in range(i - 1):
                result *= self
            return  result         
        
                

if __name__ == '__main__':

    def reverse(s):
        "Reverses a string using negative-stride sequencing."
#    print("Reverse ", s[::-1])
        return s[::-1]

    reverser = Composable(reverse)
    
    nulltran = reverser ** 1 
    print(nulltran("abcd"))

    nulltran = reverser ** 2 
    print(nulltran("abcd"))
    
    nulltran = reverser ** 3 
    print(nulltran("abcd"))
    

    def square(x):
        return x * x

    squarer = Composable(square)
    po4 = squarer ** 1  
    print(po4(2))

    po4 = squarer ** 2  
    print(po4(2))
    po4 = squarer ** 3    
    print(po4(2))
    po4 = squarer ** 4    
    print(po4(2))

    '''
    print(f(f(2)))
    print(f(2)**2)
    print(f(f(f(2))))
    print(f(2)**3)    
    print(f(f(f(f(2)))))
    print(f(2)**4)    
    '''
