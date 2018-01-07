"""
Demonstrate magic methods for attribute access.
"""
class AttrMixin:
    "Displays a message when an instance's attributes are set."    
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value
 
class Person(AttrMixin):
    "Represents a person"
    def __init__(self, name):
        self.name = name
        
if __name__ == "__main__":
    from newmagic import *
    s = ustr("Stevie Wonder")
    print(s)
    print(type(s))
    print(s.lower())
    print(len(s))
    ss = "Stevie Wonder"
    try:
        ss.size = 5
    except AttributeError:
        print("AttributeError: str object has no attribute size")
        
    
