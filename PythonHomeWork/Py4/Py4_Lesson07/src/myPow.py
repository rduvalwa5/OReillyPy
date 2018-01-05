'''
Created on May 26, 2014

@author: rduvalwa2
'''

import math

def myPow(f):
    def powers(*args):  
        print("In Decorator") 
        x = f(*args)
        if False == isinstance(x, int):
            raise TypeError
        elif x < 0:
            raise ValueError     
        else:
            return pow(x, x)
    return powers

@myPow
def myfunc(x):
    print("Message")
    return x + x     
     
     
if __name__ == "__main__":
    print(myfunc(4))

    
    for value in [6, -1, "a", 101, "123"]:
        try:
            print(value, "is ", myfunc(value))
        except TypeError:
            print(value, "is TypeError")
        except ValueError:
            print(value, "is Value Error")

