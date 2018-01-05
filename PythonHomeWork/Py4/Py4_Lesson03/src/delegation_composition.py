'''
1. Ns class uses a list of dicts as its primary data store
   - doesn't call any of their methods directly
   -  It does call their methods indirectly though, 
   -  because the _getitem__() method iterates over the list to access the required element from each dict in turn
2. Each failure raises a KeyError exception
   - is ignored by the pass statement to move on to the next iteration
3. effectively the __getitem__() method searches a list of dicts
   - stopping when it finds something to return
4. That is why ns["one"] returned 1. 
   While 14 is associated with the same key, this association takes place in a dict later 
   in the list and so is never considered; the function has already found the same key in an
   earlier list and returned with that key's value.
'''

class Ns:
    def __init__(self, *args):
        "Initialize a list of namespaces presented as dicts"
        self._dlist = args
    def __getitem__(self, key):
        for d in self._dlist:
            try:
                return d[key]
            except KeyError:
                pass
        raise KeyError("{!r} not present in Ns object".format(key))

if __name__ == "__main__":
#    from delegation_composition import *
    ns = Ns({"One": 1, "Two": 2}, {"One":13, "Three": 3}, {"one": 14, "Four": 4})
    print("One is :", ns["One"])
    print("one is :", ns["one"])
    print("For is :", ns["Four"])
    print(ns)
    print(ns.__dict__)
    for item in ns._dlist:
        print("item" , item)
        lst = list(item)
        print("lst ", lst)
        for it in lst:
            print("it ", it)
            print("GetItem ", ns.__getitem__(it))
    print(ns.__getitem__("Six"))
#    print(ns.keys)
    
