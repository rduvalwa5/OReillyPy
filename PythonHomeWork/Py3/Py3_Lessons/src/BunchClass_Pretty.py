'''
Created on Jun 4, 2013
pretty printing
@author: rduval
'''
import unittest

class Bunch(object):
    def __init__(self,*args, **kwargs):
        self.__dict__.update(kwargs)
    
    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key,value)
        return text
    
class TestBunch(unittest.TestCase):
    def test_attributes(self):
        b = Bunch(name="Python 3", language="Python 3.0.1")
        self.assertEqual("Python 3", b.name)
        self.assertEqual("Python 3.0.1", b.language)
    def test_pretty(self):
        b = Bunch(name = "Steve Holden", profession="Pythonista")
        p = b.pretty()
        self.assertTrue("name: Steve Holden" in p)
        self.assertTrue("profession: Pythonista" in p)
        self.assertEqual(len(p.splitlines()), 2, "Too many lines")

if __name__ == "__main__":
    unittest.main()
    