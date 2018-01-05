'''
Demostrates attribute resolution removal
'''
class Small:
    class Smaller:
           x = 20
    smaller = Smaller

small = Small()
    
def attr1():
    ttl = 0
    for i in range(50):
       ttl += small.smaller.x
    return ttl
    
def attr2():
    ttl = 0
    x = small.smaller.x
    for i in range(50):
       ttl += x
    return ttl
    
from timeit import timeit
print("attr1 ", timeit("attr1()", "from __main__ import small, attr1"))
print("attr2 ", timeit("attr2()", "from __main__ import small, attr2"))        

'''
E:\Python\Py4_Git\Py4_Git\Py4_Git\Py4_Lesson_5\src>python removeAttributeResolutionFromLoop.py
attr1  6.594809116948836
attr2  3.150187070921577
'''
