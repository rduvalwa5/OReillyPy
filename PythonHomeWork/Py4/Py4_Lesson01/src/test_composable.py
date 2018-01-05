"""
test_composable.py" performs simple tests of composable functions.
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
#    print("Reverse ", s[::-1])
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x * x

class ComposableTestCase(unittest.TestCase):


    def test_inverse(self):
        print("\n ***** Test Inverse String attributes******")
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            print(nulltran(s))
            self.assertEqual(nulltran(s), s)
       
    def test_square(self):
        print("\n ***** Test Square numbers******")
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1, 1), (2, 16), (3, 81), (-1, 1), (-2, 16)):
            print(po4(v))
            self.assertEqual(po4(v), r)
            
    def test_exceptions(self):
        print("\n ***** Test Exceptions Type Errors******")
        fc = Composable(square)
        print("Type is ", type(fc))
        with self.assertRaises(TypeError):    
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc

if __name__ == "__main__":
    unittest.main()
