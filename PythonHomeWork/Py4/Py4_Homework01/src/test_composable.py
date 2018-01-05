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
        reverser = Composable(reverse)
        nulltran = reverser ** 2  #  reverser -- commenting out what was a mulitplicand
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)
    
    def test_square(self):
            squarer = Composable(square)
            po4 = squarer ** 2  #  square
            for v, r in ((1, 1), (2, 16), (3, 81)):
                self.assertEqual(po4(v), r)
                
    def test_exceptions(self):
            fc = Composable(square)
            with self.assertRaises(TypeError):    
                fc = fc * 3
            with self.assertRaises(TypeError):
                fc = square * fc
            
            
    def test_Powers_ValueError(self):
            with self.assertRaises(ValueError):
                    squarer = Composable(square)
                    po4 = squarer ** -1
                    
    def test_Powers_TypeError(self):
            with self.assertRaises(TypeError):
                    squarer = Composable(square)
                    po4 = squarer ** "a"
    
if __name__ == "__main__":
    unittest.main()
