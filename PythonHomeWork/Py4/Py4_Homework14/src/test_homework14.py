'''
Created on Apr 23, 2014
@author: rduvalwa2
Here are your instructions:
Write a context manager class that suppresses any ValueError exceptions that occur 
in the controlled suite, but allows any other exception to be raised in the surrounding context.
'''

import unittest
# from contextlib import contextmanager

class ctx_mgr:
    def __enter__(self):
        cm = object()
#        print("Enter ",cm)
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
#        print("Exit ")
        if exc_type:
            if exc_type != ValueError:
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

class TestContextMgr(unittest.TestCase):

    """ Demonstrate the context manager does not interfere with a with no error""" 
    def test_noError(self):
        try:
            with ctx_mgr() as cm: 
                result = adder(3, 4)
        except Exception as e:
            print(e)
        self.assertEqual(result, 7)

        try:
            with ctx_mgr() as cm: 
                result = adder("abc", "d")
        except Exception as e:
            print(e)
        self.assertEqual(result, 'abcd')
 
        try:
            with ctx_mgr() as cm: 
                result = getIndex("abcdefg", "e")
        except Exception as e:
            print(e)
        self.assertEqual(result, 4)

        try:
            with ctx_mgr() as cm: 
                result = findKey("abcde", 2)
        except Exception as e:
            print(e)
        self.assertEqual(result, 'c')

    """ Demonstrate the context manager SUPPRESSES ValueError"""         
    def test_ValueError(self):
            result = "x"
            with ctx_mgr() as cm: 
                print("Test ValueError", cm)
                result = "no error"
                getIndex("abcde", "x")
            self.assertEqual(result, "no error")

    """ Demonstrate the context manager DOES ALLOW KeyError to be thrown"""         
    def test_KeyError(self):
        try:
            with ctx_mgr() as cm: 
                print("Test KeyError", cm)
                getIndex("abcde", "x")
        except KeyError:
            self.assertTrue(KeyError, "string index out of range")   
 
    """ Demonstrate the context manager DOES ALLOW TypeError to be thrown"""            
    def test_TypeError(self):
        try:
            with ctx_mgr() as cm: 
                print("Test TypeError", cm)
                adder(3, "a")
        except TypeError:
            self.assertTrue(TypeError, "unsupported operand type(s) for +: 'int' and 'str'")   
           
if __name__ == "__main__":
    unittest.main()
