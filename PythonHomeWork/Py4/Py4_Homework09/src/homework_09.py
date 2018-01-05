'''
Created on Mar 25, 2014
Write a program that imports a module and then goes through the module's namespace to find any functions 
and print the names of the functions and their arguments, in the same way as it might appear in a def statement.
--
 Almost.
 --
 Your program's output for the json module:
 --
 dump ('obj', 'fp', 'skipkeys', 'ensure_ascii', 'check_circular', 'allow_nan', 'cls', 'indent', 'separators', 'default')
 dumps ('obj', 'skipkeys', 'ensure_ascii', 'check_circular', 'allow_nan', 'cls', 'indent', 'separators', 'default')
 load ('fp', 'cls', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'object_pairs_hook')
 loads ('s', 'encoding', 'cls', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'object_pairs_hook')
 --
 but what's expected would be:
 --
 dump (obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, **kw)
 dumps (obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, **kw)
 load (fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
 loads (s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
 i.e. default arguments are show with defaults and there's no quoting of argument names.
 Hint:  inspect.formatargspec is your friend.
 Good work so far.
 -Kirby
@author: rduvalwa2

'''

import inspect
import importMod
from arr import array
import json 


def get_functions(mod):
    for ob in inspect.getmembers(mod, inspect.isfunction):
        yield ob    
            
if __name__ == "__main__":
    mod = json
    for func in get_functions(mod):
        print(func[0], inspect.formatargspec(*inspect.getfullargspec(func[1])))
        
    mod = importMod
    for func in get_functions(mod):
        print(func[0], inspect.formatargspec(*inspect.getfullargspec(func[1])))
            
    mod = array
    for func in get_functions(mod):
        print(func[0], inspect.formatargspec(*inspect.getfullargspec(func[1])))
