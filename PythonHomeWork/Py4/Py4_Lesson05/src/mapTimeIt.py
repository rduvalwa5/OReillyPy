'''
Created on Jan 5, 2014
@author: rduvalwa2
'''
from timeit import timeit
oldlist = "the quick brown fox jumps over the lazy dog.".split()

def lf1(lst):
    newlist = []
    for w in lst:
        newlist.append(w.upper())
    return newlist
    
def lf2(lst):
    return [w.upper() for w in lst] 
    
def lf3(lst):
    return list(w.upper() for w in lst)
    
def lf4(lst):
    return map(str.upper, lst)  # map() buit-in

print("lf1 ", timeit("lf1(oldlist)", "from __main__ import lf1, oldlist"))
print("lf2 ", timeit("lf2(oldlist)", "from __main__ import lf2, oldlist"))
print("lf3 ", timeit("lf3(oldlist)", "from __main__ import lf3, oldlist"))
print("lf4 ", timeit("lf4(oldlist)", "from __main__ import lf4, oldlist"))
