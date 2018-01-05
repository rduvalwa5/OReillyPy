'''
Created on Apr 22, 2014
Here are your instructions:
Write a context manager class that suppresses any ValueError exceptions that occur in the controlled suite,
but allows any other exception to be raised in the surrounding context.
----
exception ValueError
Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value,
and the situation is not described by a more precise exception such as IndexError.
@author: rduvalwa2
'''
from contextlib import contextmanager

class ctx_mgr:
#    def __init__(self):
#        print("Created new context manager object", id(self))
#        self.raising = raising
    def __enter__(self):
#        print("__enter__ called")
        cm = object()
#        print("__enter__ returning object id:", id(cm))
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
#        print("__exit__ called")
        if exc_type:
#            print(exc_type)
            if exc_type == ValueError:
#                print(exc_type)
#                print("An exception occurred")
#                print("Re-raising exception")
#                raise ValueError
                pass
            else:
                return "Nothing"
                    

def adder(a, b):
    return a + b 

def findKey(string, key):
    return string[key]
    
def contains(string, ch):
    return string.__contains__(ch)
    
def getIndex(string, item):
    return string.index(item)

if __name__ == "__main__":
        """Index Error"""
        try:
            findKey("abcde", 7)
        except IndexError as e:
            print(IndexError.__repr__(e))
        """ TypeError"""
        try:
            print("Adder", adder(3, "a"))
        except TypeError as e:
            print("e is ", TypeError.__repr__(e))
            print(TypeError.__str__(e))
            
        with ctx_mgr() as cm:
            print(adder(3, 4))

        with ctx_mgr() as cm:
            print(adder("a", "b"))

        with ctx_mgr() as cm:
            print(adder("abc", "d"))

        with ctx_mgr() as cm:
            print(findKey("abcde", 2))

        with ctx_mgr() as cm:
            print(contains("abcdef", "d"))

        with ctx_mgr() as cm:
            print(getIndex("abcdefg", "e"))

        with ctx_mgr() as cm:
#            getIndex("abcde","x")
            print(getIndex("abcde", "x")) 
       


'''
        """Value Error """
        try:
            getIndex("abcde","x")
        except ValueError as e:
            print(ValueError.__repr__(e))

        with ctx_mgr() as cm:    
            print(adder(3,"a"))    

        with ctx_mgr() as cm:
            print(findKey("abcde",7))
             
        with ctx_mgr() as cm:
            print(getIndex("abcde","x"))    
'''
