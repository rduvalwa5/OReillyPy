'''
Created on Sep 24, 2013

@author: rduvalwa2
'''
"""
Demonstrate magic methods for attribute access.
"""
class AttrMixin:
    "Displays a message when an object's attributes are retrieved or set."    
 
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value
 
    def __getattr__(self, key):
        print("ATTR: getting attribute {0!r}".format(key))
        self.__setattr__(key, "No value")
        return "No value"
 
class Person(AttrMixin):
    "Represents a person"
    def __init__(self, name):
        self.name = name
      
if __name__ == "__main__":
#    from attrmagic_edit import *
    steve = Person("Steve Holden")
    steve.newattr
    print(steve.newattr)
    print(steve.name)
    print(steve.__dict__)
    
# >>> from attrmagic_edit import *
# >>> steve = Person("Steve Holden")
# ATTR: setting attribute 'name' to 'Steve Holden'
# >>> steve.newattr
# ATTR: getting attribute 'newattr'
# ATTR: setting attribute 'newattr' to 'No value'
# 'No value'
# >>> steve.newattr
# 'No value'
# >>> steve.name
# 'Steve Holden'
# >>> 

