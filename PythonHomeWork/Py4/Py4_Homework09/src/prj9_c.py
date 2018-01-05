'''
Created on Mar 24, 2014
Write a program that imports a module and then goes through the module's namespace to find any functions 
and print the names of the functions and their arguments, in the same way as it might appear in a def statement.

'''
import inspect
import importMod
from arr import array


def get_functions(mod):
    for ob in inspect.getmembers(mod, inspect.isfunction):
        yield ob
    
def get_arguments(mod):
    for func in inspect.getmembers(mod, inspect.isfunction):    
        print(inspect.getargspec(func[1]))
        print("Format ", inspect.formatargspec(func[0]))
        arguments = []
        for arg in inspect.getargspec(func[1]):
            if  arg != None:
                yield arg
                
def get_formatArgSpec(mod):
        print(inspect.formatargspec(mod))



            
if __name__ == "__main__":
    mod = array
    for func in get_functions(mod):
        function = func[0]
        x = []
        for val in inspect.getfullargspec(func[1]):
            x.append(val)
        print(function, tuple(x[0]))

    for ag in get_arguments(mod):
        print("ag", tuple(ag))
        
