'''
Created on Oct 24, 2013

@author: rduvalwa2
'''

import unittest

from Py4Lesson6HomeWork import myDict

class TestKeyErrorExtend(unittest.TestCase):

    def setup(self):
        self.mydict = myDict("Bad Value")
        
    def test_SetItemSuccess(self):
        self.mydict = myDict("Bad Value")
        expected = 11
        self.mydict['a'] = expected
        actual = self.mydict['a']
        self.assertEqual(actual, expected) 
    
    def test_ErrorKey(self):
        self.ErrorMsg = "Bad Value"
        self.mydict = myDict(self.ErrorMsg)
#        print("test 2 ",self.mydict['x'])
        self.actualMessage = self.mydict['x']
        self.assertEqual(self.actualMessage, self.ErrorMsg, "Not correct error message")
        
    def test_DefaultValue(self):
        self.ErrorMsg = "Bad Value"
        self.mydict = myDict(self.ErrorMsg)
        self.mydict['b']
#        print("Test 3 ", self.mydict['b'])
        self.assertEqual(self.mydict['b'], self.mydict.placeValue, "Not correct value")
        


if __name__ == "__main__":
    unittest.main()
