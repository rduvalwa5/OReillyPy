'''
Created on Apr 15, 2014

@author: rduvalwa2
'''
def f(i: int, x:float=1.2) -> str:
        return str(i + x)
def g(i):
    return i + i

print(f.__annotations__)
# {'i': <class 'int'>, 'x': <class 'float'>, 'return': <class 'str'>}
print(f(4))
try: print(f('a'))
except TypeError:
    print("TypeError: Can't convert 'float' object to str implicitly")
print(g(4))
print(g('a'))

'''
{'return': <class 'str'>, 'x': <class 'float'>, 'i': <class 'int'>}
5.2
TypeError: Can't convert 'float' object to str implicitly
8
aa
'''
