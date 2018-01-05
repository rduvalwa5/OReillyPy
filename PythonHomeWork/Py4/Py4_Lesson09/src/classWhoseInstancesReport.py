'''
Created on Mar 19, 2014
@author: 310122001
'''
"Before Class Doc"
class X:
    "Class x document!"
    def __getattr__(self, name):
        print("getattr", name)
        return 0
    "End of class"
      
x = X()
print(hasattr(x, "thing"))
    
print(x.__doc__)  
print(help(x))  

'''
getattr thing
True
Class x document!
getattr __name__
Help on X in module __main__ object:

class X(builtins.object)
 |  Class x document!
 |  
 |  Methods defined here:
 |  
 |  __getattr__(self, name)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
'''
