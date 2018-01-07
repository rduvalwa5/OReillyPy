"""
Demonstrate magic methods for attribute access.
"""
class AttrMixin:
    "Displays a message when an object's attributes are retrieved, deleted or set."    
 
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value
 
    def __getattr__(self, key):
        print("ATTR: getting attribute {0!r}".format(key))
        self.__setattr__(key, "No value")
        return "No value"
 
    def __delattr__(self, key):
        print("ATTR: Deleting key {0!r}".format(key))
        object.__delattr__(self, key)
        
class Person(AttrMixin):
    "Represents a person"
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    import unittest
    class Testattrmagic(unittest.TestCase):
            def test_Class(self):
                student = Person("Red Dog")
                self.assertEqual("Red Dog", student.name, "Student name should be No Value")
                self.assertEqual('No value', student.age, "Student Age is wrong")
                student.age = 30
                self.assertEqual(30, student.age, "Student Age should be 30")
                del student.age
                self.assertEqual('No value', student.age, "Student Age should be No Value")
                
unittest.main()
	
"""
>>> from attrmagic3 import *
>>> student = Person("Red Dog")
ATTR: setting attribute 'name' to 'Red Dog'
>>> student.age
ATTR: getting attribute 'age'
ATTR: setting attribute 'age' to 'No value'
'No value'
>>> student.age = 30
ATTR: setting attribute 'age' to 30
>>> student.age
30
>>> del student.age
ATTR: Deleting key 'age'
>>> student.age
ATTR: getting attribute 'age'
ATTR: setting attribute 'age' to 'No value'
'No value'
>>> del student.__delattr__
ATTR: Deleting key '__delattr__'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".\attrmagic3.py", line 18, in __delattr__
    object.__delattr__(self, key)
AttributeError: __delattr__
>>> student
<attrmagic3.Person object at 0x00000000029B9E48>
>>> student.name
'Red Dog'
>>> student.__dict__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> student.__dict__
{'name': 'Red Dog', 'age': 'No value'}
>>>
"""
