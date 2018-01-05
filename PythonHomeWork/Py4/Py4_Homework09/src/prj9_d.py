'''
Created on Mar 25, 2014

@author: rduvalwa2
'''
'''
Created on Mar 24, 2014
http://docs.python.org/2/library/inspect.html
inspect.formatargvalues(args[, varargs, varkw, locals, formatarg, formatvarargs, formatvarkw, formatvalue, join])
 Format a pretty argument spec from the four values returned by getargvalues(). The format* arguments are the corresponding optional formatting functions that are called to turn names and values into strings.

@author: 310122001
'''
import inspect
import importMod
from arr import array


def get_functions(mod):
    for ob in inspect.getmembers(mod, inspect.isfunction):
        yield ob    

            
if __name__ == "__main__":
    mod = importMod
    for func in get_functions(mod):
        function = func[0]
        x = []
        for val in inspect.getfullargspec(func[1]):
            x.append(val)
        print(function, tuple(x[0]))

    mod = array
    for func in get_functions(mod):
        function = func[0]
        x = []
        for val in inspect.getfullargspec(func[1]):
            x.append(val)
        print(function, tuple(x[0]))
