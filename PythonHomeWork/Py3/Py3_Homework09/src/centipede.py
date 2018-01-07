'''
@author: rduvalwa2
Overall Comments:
You have a fairly complicated design here.  
-
Individual Centipedes do not share stomachs or legs, so those should
be instance level variables:
-
class Centipede:
    def __init__(self):
        self.legs = [ ]
        self.stomach = [ ]
-
except these simple assignments may run afoul of __setattr__.
-
You should have no __getattr__ in any class.  __setattr__ should 
append the attributes that were set, by name i.e. if ralph the 
Centipedes favorite icecream is "vanilla", then ralph.legs should
have the string 'icecream' appended.  A little strange, but designed
to get you protecting against bogus inputs.  
-
Note:  you can get around __setattr__ by calling the parent version
of the method:  super().__setattr__("legs", [ ]) or maybe just use 
__setindex__ syntax instead:  self.__dict__["legs"] = [ ].  This kind
of thing __init__ will let you get self.legs and self.stomach going 
with no worries from __setattr__.
Looking forward to your next draft.  Good work so far.
-Kirby
'''
class AttrMixin:
    "Displays a message when an object's attributes are retrieved, deleted or set."   
    
    def __setattr__(self, key, value):
#        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        if key == 'legs':
            raise AttributeError
        elif key == 'stomach':
            raise AttributeError
        else:
            self.__dict__[key] = value
        self.legs.append(key)

class Centipede(AttrMixin):
    def __init__(self):
            self.__dict__["legs"] = [ ]
            self.__dict__["stomach"] = [ ]
            
    def __call__(self, *args, **kwargs):
#            print("args is: ", args, "kwargs is: ", kwargs)
            self.stomach.append(args[0])

    def __str__(self):
        return ','.join(self.stomach) 
    
    def __repr__(self):        
        return ','.join(sorted(self.legs, reverse=True))
        
if __name__ == "__main__":
    ralph = Centipede()
    ralph('chocolate')
    ralph('bbq')   
    ralph('cookies')         
    ralph('salad') 
    ralph.friends = ['Steve', 'Daniel', 'Guido']        
    ralph.favorite_show = "Monty Python's Flying Circus"        
    ralph.age = '31'
    print("dict :", ralph.__dict__)
    print("ralph.__str__: ", ralph.__str__())
    print(ralph.age)
    print(ralph.__repr__())
    ralph('legs')
    ralph('stomach')
    print(ralph.stomach)
    print(ralph.legs)
    
'''
class Centipede(object):
    def __init__(self):
        self.__dict__['legs'] = []
        self.__dict__['stomach'] = []

    def __call__(self, value):
        self.stomach.append(value)

    def __repr__(self):
        return '<' + ','.join(self.legs) + '>'

    def __setattr__(self, key, value):
        if key in ('legs', 'stomach'):
            raise AttributeError
        else:
            self.__dict__[key] = value
            self.legs.append(key)

    def __str__(self):
        return ','.join(self.stomach)
'''    
