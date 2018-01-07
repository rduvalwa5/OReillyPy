'''
Created on Sep 26, 2013

@author: rduvalwa2
'''
class AttrMixin:
    "Displays a message when an instance's attributes are set."
    items = []    
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value

class Centipede(AttrMixin): 
    def __call__(self, *args, **kwargs):
#        print("Args are:", args)
#        print("Kwargs are:", kwargs)
#    def __init__(self, args):
        self.attrib = args
        self.items.append(args)
        print("items: ", self.items)

#    def __call__(self,*args, **kargs):
#            self.key = args
#            self.value = kargs
#            self.__setattr__(self.key, self.value)
#            self.attribute.append(self.key)
             
        
if __name__ == "__main__":
#    from centipede import Centipede
    ralph = Centipede()
    ralph('chocolate')
    ralph('bbq')    
    print("dict :", ralph.__dict__)
    print("ralph: ", ralph)
    print("ralph.__str__: ", ralph.__str__())
#    print(ralph.items)
