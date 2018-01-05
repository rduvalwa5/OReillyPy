'''
Created on Mar 29, 2014

@author: rduvalwa2
'''
import inspect
import importMod
from arr import array


def f(a, b, c=1, d="one", *args, **kw):
    print('a', a, 'b', b, 'c', c, 'd', d, 'args', args, 'kw', kw)
 
print(inspect.getfullargspec(importMod))
# FullArgSpec(args=['a', 'b', 'c', 'd'], varargs='args', varkw='kw', defaults=(1, 'one'), kwonlyargs=[], kwonlydefaults=None, annotations={})
print(inspect.formatargspec(*inspect.getfullargspec(importMod)))
# "(a, b, c=1, d='one', *args, **kw)"
