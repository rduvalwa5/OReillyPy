'''
Created on Jun 2, 2013
The tests are small here, so it is OK to add them to the basic module rather 
than making a separate test module. The current code always imports the unittest module 
even when it is not going to be used (when the module is imported rather than running as a main program).
@author: rduvalwa2

Simple bunch class
'''
import unittest

class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
      
class TestBunch(unittest.TestCase):
    def test_attributes(self):
        b = Bunch(name="Python 3", language="Python 3.0.1")
        self.assertEqual("Python 3", b.name)
        self.assertEqual("Python 3.0.1", b.language)

if __name__ == "__main__":
#    b = Bunch(name="Python 3", language="Python 3.0.1")
#    print(b.name)
#    print(b.language)
#    print(b.__dict__)
    unittest.main()


