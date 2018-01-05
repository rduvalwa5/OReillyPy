'''
Created on May 28, 2013
@author: rduvalwa2
'''
import unittest
from adder import addIntegers


class Test(unittest.TestCase):
    """
    Test positive result, add integers
    """
    def testAddIntegers(self):
            self.assertEqual(24, addIntegers(3, 21))
    """
    Add long integers
    """            
    def testAddLongIntegers(self):
            self.assertEqual(1000000000021, addIntegers(1000000000000, 21))
    """
    Test char
    """
    def testCharThrowError(self):
                self.assertRaises(TypeError, addIntegers, "A", 3)
    """
    Test float
    """            
    def testFloatThrowError(self):
                self.assertRaises(TypeError, addIntegers, 1.01, 3)  
    """
    Test number as char
    """
    def testNumCharThrowError(self):
                self.assertRaises(TypeError, addIntegers, 100, '3')  
    """
    Test string
    """
    def testStringThrowError(self):
                self.assertRaises(TypeError, addIntegers, 100, "abcdef")  
                
    def testDecimalThrowError(self):
                self.assertRaises(TypeError, addIntegers, 100, 3.5)  

                
if __name__ == "__main__":
    unittest.main()
