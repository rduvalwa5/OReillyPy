'''
Created on Dec 18, 2013
Demonstrates extension of dict MyDict(dict)
has access to all methods of a dict
@author: rduvalwa2
'''

class MyDict(dict):
    pass
            
if __name__ == "__main__":
    print("Demonstarttion of dict methods: http://docs.python.org/2/library/stdtypes.html?highlight=dict#dict")
    dd = MyDict(wynken=1, blynken=2)
    print(dd['blynken'])
    # 2
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
    dd['nod2'] = 3
    dd.__delitem__('nod2')
    print(dd.__dict__)
    print(dd.items())
    aa = dd.copy
    print(dir(aa))
    n = 0
#    keys = dd.viewkeys()
#    values = dd.viewvalues()
    DD = {}
    print(type(DD))
    for key in range(5):
        DD[key] = "a" + str(key)
    print(DD)
    print(DD.items())
    print(DD.keys())
    print(DD.values())
    print(DD)
    DD.pop(0)
    print("a0 is gone: ", DD)
    print("Set default key:", DD.setdefault(3))    
    print("Get default key", DD.get(6))
