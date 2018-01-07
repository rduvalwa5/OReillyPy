"""
Python classes with magic methods
use __new__ when extending immutable built-in types
like numbers and string
since it would not be possible to change them in the __init__() method
an extension of the basic str type that returns a string object that always has upper-case
versions of any letters it may contain.
Create the Python3_Lesson09 project and assign it to the Python3_Lessons working set. 
Then, in the Python3_Lesson09/src folder, create newmagic.py as shown:
"""
 
class ustr(str):
    "An upper case string object."
    def __new__(cls, arg):
        arg = str(arg)
#        print(arg)
        return str.__new__(cls, arg.upper())
    
if __name__ == "__main__":
    theString = "changed to upper case"
    rtn = ustr(theString)
    print (type(rtn))
    print(rtn)
    print(len(rtn))
    print(rtn.lower())
    rtn.size = 12
    rtn.bold = 34
    print(rtn.size)
    print(rtn.__dict__)
    ss = "A regular string"
    try:
        ss.size = 16
    except AttributeError:
        print("AttributeError")
    
    
