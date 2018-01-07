'''
Created on Jun 1, 2013
Simple bunch class
@author: rduvalwa2
'''
#import unittest

class Bunch(object):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of the '%s' API" % (key, self.__class__.__name__))
            else:
                setattr(self, key, value)
    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text
    
#    def __init__(self,**kwargs):
#        self.__dict__.update(kwargs)

#class TestBunch(unittest.TestCase):
#    def test_attributes(self):
#        b = Bunch(name="Python 3", language="Python 3.0.1")
#        self.assertEqual("Python 3", b.name)
#        self.assertEqual("Python 3.0.1", b.language)

        
if __name__ == "__main__":
#    b = Bunch(name="Python 3", language="Python 3.0.1")
#    print(b.name)
#    print(b.language)
#    print(b.__dict__)
    import unittest
    class TestBunch(unittest.TestCase):
        def test_attributes(self):
            b = Bunch(name="Python 3", language="Python 3.0.1")
            self.assertEqual("Python 3", b.name)
            self.assertEqual("Python 3.0.1", b.language)

    unittest.main()

