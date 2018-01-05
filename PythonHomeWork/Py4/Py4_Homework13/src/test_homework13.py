'''
Created on Apr 17, 2014

@author: rduvalwa2
'''
import unittest
from Py4_Homework13 import sstr, NumberSize


class TestSstr(unittest.TestCase):

    def test_sstr(self):
        s1 = sstr("abcde")
        self.assertEqual(s1 << 0, 'abcde')
        self.assertEqual(s1 >> 0, 'abcde')
        self.assertEqual(s1 >> 2, 'deabc')
        self.assertEqual(s1 << 2, 'cdeab')
        self.assertEqual(s1 >> 5, 'abcde')
        self.assertEqual(s1 << 5, 'abcde')
        self.assertEqual((s1 >> 5) << 5, 'abcde')
        
    def test_errorRightShift(self):
        s1 = sstr("abcde")
        try:
            s1 >> 6
        except NumberSize: 
            self.assertTrue(NumberSize, "Number too big")
            
    def test_errorLeftShift(self):
        s1 = sstr("abcde")
        try:
            s1 << 6
        except NumberSize: 
            self.assertTrue(NumberSize, "Number too big")            

if __name__ == "__main__":
    unittest.main()
