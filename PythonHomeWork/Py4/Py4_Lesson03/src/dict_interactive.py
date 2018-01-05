'''
Created on Dec 18, 2013

@author: rduvalwa2
'''

class Dict(dict):  # how to extend __dict__
    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)
        self.adds = 0
    def __setitem__(self, key, value):
        if key not in self:
            self.adds += 1
            dict.__setitem__(self, key, value)
'''
This class delegates by binding the dict object to a local variable self._d = dict(*args, **kwargs)
'''
class MyDict:
#    d = Dict()
    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)
    def __setitem__(self, key, value):
        return self._d.__setitem__(key, value) 
    def __getitem__(self, key):
        return self._d.__getitem__(key)
    def __delitem__(self, key):
        return self._d.__delitem__(key)
            
if __name__ == "__main__":
    d = Dict(a=1, b=2)
    print("Adds:", d.adds)
    # Adds: 0
    d["newkey"] = "add"
    print("Adds:", d.adds)
    # Adds: 1
    d["newkey"] = "replace"
    print("Adds:", d.adds)
    # Adds: 1
    # d.__dict__()
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: 'dict' object is not callable
    d.__dict__
    # {'adds': 1}
    d["next"] = "replace"
    print("Adds:", d.adds)
    print(d.__dict__)
    # {'adds': 2}
    print(dict(d))
    # {'b': 2, 'a': 1, 'newkey': 'replace', 'next': 'replace'}
    print(d)
    # {'b': 2, 'a': 1, 'next': 'replace', 'newkey': 'replace'}

    dd = MyDict(wynken=1, blynken=2)
    print(dd['blynken'])
    # 2
    print(dd.__dict__)
#    print(dd['nod']) # -->
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "<stdin>", line 7, in __getitem__
# KeyError: 'nod'
    dd['nod'] = 3
    print(dd['nod'])
    # 3
    print(dd.__dict__)
    del dd['nod']
    print(dd)
    print(dd.__dict__)
#    print(dd.keys())
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'MyDict' object has no attribute 'keys'

    
    
