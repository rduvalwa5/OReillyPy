'''
Created on Apr 21, 2014
Demonstates a simple context manager
@author: rduval
'''
class ctx_mgr:
    def __init__(self, raising=True):
        print("Created new context manager object", id(self))
        self.raising = raising
    def __enter__(self):
        print("__enter__ called")
        cm = object()
        print("__enter__ returning object id:", id(cm))
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called")
        if exc_type:
            print("An exception occurred")
            if self.raising:
                print("Re-raising exception")
            return not self.raising
        
with ctx_mgr(raising=True) as cm:
    print("cm ID:", id(cm))
print("case 1")
with ctx_mgr(raising=False):
       3 / 0
print("case 2")
with ctx_mgr(raising=False) as cm:
     3 / 0
print("case 3")
with ctx_mgr(raising=True) as cm:
        5 / 0
