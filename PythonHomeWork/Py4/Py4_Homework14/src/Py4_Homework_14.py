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
    def __enter__(self):
        cm = object()
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if exc_type == ValueError:
                pass
#            else:
#                return 
                    

def adder(a, b):
    return a + b 

def findKey(string, key):
    return string[key]
    
def contains(string, ch):
    return string.__contains__(ch)
    
def getIndex(string, item):
    return string.index(item)

if __name__ == "__main__":

        with ctx_mgr() as cm:
            adder(3, 4)

        with ctx_mgr() as cm:
            adder("a", "b")

        with ctx_mgr() as cm:
            adder("abc", "d")

        with ctx_mgr() as cm:
            findKey("abcde", 2)

        with ctx_mgr() as cm:
            contains("abcdef", "d")

        with ctx_mgr() as cm:
            getIndex("abcdefg", "e")

        with ctx_mgr() as cm:
            getIndex("abcde", "x") 
