'''
Created on Jun 1, 2014

@author: rduval
'''
class myPow(object):
    def __init__(self, arg1):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print ("Inside __init__()")
        self.arg1 = arg1
        print("self.arg1", self.arg1)

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        def powers_f(*args): 
                print("In powers_f()")
                print("Decorator Argument", self.arg1)
                x = self.arg1
                print("x is", x)
                if False == isinstance(x, int):
                    raise TypeError
                elif x < 0:
                    raise ValueError     
                else:
                    return pow(f(*args), x)
        return powers_f

if __name__ == "__main__":
    inx = 3
    @myPow(inx)
    def myfunc(x):
        print("Message")
        return x + x    
    
    print(myfunc(4))

    for value in [6, -1, "a", 101, "123"]:
        try:
            inx = value
            @myPow(inx)
            def myfunc(value):
                print("Message")
                return value + value    
            print(value, "is ", myfunc(value))
        except TypeError:
            print(value, "is TypeError")
        except ValueError:
            print(value, "is Value Error")
