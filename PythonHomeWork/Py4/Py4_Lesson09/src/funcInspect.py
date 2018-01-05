'''
Created on Mar 21, 2014

@author: 310122001
'''
import inspect
def f(a, b, c=1, d="one", *args, **kw):
    print('a', a, 'b', b, 'c', c, 'd', d, 'args', args, 'kw', kw)

if __name__ == "__main__": 
    print("Start")
    print(inspect.getfullargspec(f))
# FullArgSpec(args=['a', 'b', 'c', 'd'], varargs='args', varkw='kw', defaults=(1, 'one'), kwonlyargs=[], kwonlydefaults=None, annotations={})
    print(inspect.formatargspec(*inspect.getfullargspec(f)))
# "(a, b, c=1, d='one', *args, **kw)"
