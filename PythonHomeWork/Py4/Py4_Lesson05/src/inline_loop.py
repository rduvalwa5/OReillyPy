'''
Created on Jan 5, 2014
@author: rduvalwa2
Demonstartes that Inline is much faster that loop function
'''
from timeit import timeit

def f1():
    pass
#    print("function f1!") 

def loopfunc():
    for i in range(8):
        f1()    
        
def inline():
    f1(); f1();f1();f1();f1(); f1();f1();f1();

print("loopfunc()  ", timeit("loopfunc()", "from __main__ import loopfunc"))
print("inline()  ", timeit("inline()", "from __main__ import inline"))

'''
E:\Python\Py4_Git\Py4_Git\Py4_Git\Py4_Lesson_5\src>python inline_loop.py
loopfunc()   1.2037171257284247
inline()   0.6685058219801063
'''
