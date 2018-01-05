'''
Here are your instructions:
Write a subclass of the standard dict class. 
Its __init__() method should take one argument, which will be used as a default value 
when a non-existent key is accessed (it should also call the standard dict's __init__() with no arguments).
Its __getitem__() method should attempt to use the standard dict.__getitem__(), 
but any KeyError exceptions should be handled by returning the default value passed to __init__() on creation. 
Write a small test program for your object.
i.e. a default value is returned any time a key is not
present -- not the usual behavior for a dict, but in 
every other respect behavior should be the same.
-
The goal is to subclass dict so that it works like this:
-
d = DefaultDict("no such animal")
d['A'] = 123
d['A']  # behaves like an ordinary dict
123
d['B']  # would normally raise a KeyError
'no such animal'
-
i.e. a default value is returned any time a key is not
present -- not the usual behavior for a dict, but in 
every other respect behavior should be the same.
-
When subclassing a dict, you need an __init__ that
takes the default value (as shown above) and that 
extends the parent __init__ (typical for subclassing
a built-in; call the parent __init__).  Then you 
would want to override __getitem__ so that you 
don't automatically get a KeyError raised when 
a lookup fails, but instead return the default value.
-
Kirby

'''

class myDict(dict):
        
        def __init__(self, default):
                self.default = default
                self.placeValue = "Default Value"
                             
        def __getitem__(self, key):
                try:
                    return super(myDict, self).__getitem__(key)
                except KeyError:
#                    print(self.default)
                    self.__setitem__(key, self.placeValue)
                    return self.default

if __name__ == "__main__": 
    mydict = myDict("Bad Value")
    mydict['a'] = "good"
    print(mydict['a'])
    mydict['b']
    print(mydict)
 
'''
E:\Python04_Homework_06\src>python
Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from w6b import myDict
>>> wb = myDict("No me")
>>> wb['a']=11
>>> wb['a']
11
>>> wb['b']
'No me'
>>> wb['b']
'Default Value'
>>> print(wb)
{'a': 11, 'b': 'Default Value'}
>>>
'''
