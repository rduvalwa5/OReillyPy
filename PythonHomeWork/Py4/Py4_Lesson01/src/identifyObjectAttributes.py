'''
Created on May 26, 2014

@author: rduvalwa2
'''


from pprint import pprint

def g(x):
    return x * x

print(g)
# <function g at 0x102a5c8c0>
print(type(g))
# <class 'function'>
print(dir(g))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
def f(x):
    return x
""" way to identify attribues in dir that are functions """

function_attrs = set(dir(f))
object_attrs = set(dir(object))
function_attrs -= object_attrs

pprint(sorted(function_attrs))
'''
['__annotations__',
 '__call__',
 '__closure__',
 '__code__',
 '__defaults__',
 '__dict__',
 '__get__',
 '__globals__',
 '__kwdefaults__',
 '__module__',
 '__name__',
 '__qualname__']
''' 
