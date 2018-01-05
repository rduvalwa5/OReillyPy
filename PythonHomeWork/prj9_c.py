'''
Created on Mar 24, 2014
http://docs.python.org/2/library/inspect.html
inspect.formatargvalues(args[, varargs, varkw, locals, formatarg, formatvarargs, formatvarkw, formatvalue, join])
 Format a pretty argument spec from the four values returned by getargvalues(). The format* arguments are the corresponding optional formatting functions that are called to turn names and values into strings.

@author: 310122001
'''
import inspect
import importMod


def get_functions(mod):
#    print(inspect.getmembers(mod,inspect.isfunction))
    for ob in inspect.getmembers(mod,inspect.isfunction):
#        print(ob[0])
#        fun = mod.__name__ + "." + ob[0]
#        print("fun ", fun)        
        yield ob
#        arguments = inspect.formatargspec(inspect.getfullargspec(ob[0]))
#        print(arguments)
#        print(mod.__name__ + "." + ob[0] + arguments)
    
def get_arguments(mod):
    for func in inspect.getmembers(mod,inspect.isfunction):    
        print(inspect.getargspec(func[1]))
        print("Format ",inspect.formatargspec(func[0]))
        arguments = []
        for arg in inspect.getargspec(func[1]):
            if  arg != None:
#                print(arg)
                yield arg
                
def get_formatArgSpec(mod):
        print(inspect.formatargspec(mod))


def get_module(mod,path):
    print("Is Module ",inspect.ismodule(mod))
    print("Memebers ",inspect.getmembers(mod)) #predicate is options
    print("Module Info ", inspect.getmoduleinfo(path))
    print("Module Name ",inspect.getmodulename(path))
            
if __name__ == "__main__":
    
    for func in get_functions(importMod):
        print(func)
        print()
        print("Full",inspect.getfullargspec(func[1]))
        print("Get", inspect.getargspec(func[1]))
        aaa = inspect.getfullargspec(func[1])
        print("AAA ", aaa)
        x = []
#        print(inspect.formatargvalues(inspect.getfullargspec(func[1]("args"))) # inspect.getargspec(func)))
        for val in inspect.getfullargspec(func[1]):
            x.append(val)
        print(x)

        
        
#    get_module(importMod,"./")
    
#    for argument in get_arguments(importMod):
#            print(argument)
#            print(tuple(argument))
    

#    print(inspect.formatargvalues(inspect.getargspec(get_module)))