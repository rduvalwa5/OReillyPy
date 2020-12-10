'''
Created on May 25, 2014

@author: rduvalwa2
'''
from timeit import timeit
from pprint import pprint

"""Callable Example 
    Function and Method Callls
    The __call__() method is interesting—its name implies that it has something to do with function calling, and this is correct. 
    The interpreter calls any callable object by making use of its __call__() method. You can actually call this method directly if you want to; it's exactly 
    the same as calling the function directly.
"""
def f(x):
    x = x ** 2
    print("f1({}) called".format(x))

print(f.__call__(23))  # should be equivalent to f1(23)
# f1(23) called
f(23)

if __name__ == "__main__":
    """ Time it example of callable function"""
    print(timeit("for x in range(3): f(x)", "from __main__ import f", number=1))

'''
number = 2
f1(529) called
None
f1(529) called
f1(0) called
f1(1) called
f1(4) called
f1(0) called
f1(1) called
f1(4) called
7.986299999999946e-05

number =1
f1(529) called
None
f1(529) called
f1(0) called
f1(1) called
f1(4) called
6.843699999999758e-05
'''

