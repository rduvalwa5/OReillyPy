'''
Created on Dec 13, 2013
test_array.py
Test list-of-list based array implementations.
 using tuple subscripting.
@author: rduvalwa2
'''
import unittest
import arr
class TestArray(unittest.TestCase):

    def test_zeroes(self):
        print("Test array")
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                for j in range(N):
#  using double subscripting    
#                    self.assertEqual(a[i][j], 0)
# using the "tuple of subscripts" notation
                    self.assertEqual(a[i, j], 0)
    def test_identity(self):
        print("Test identity")
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
#               a[i][i] = 1 
                a[i, i] = 1
            for i in range(N):
                for j in range(N):
#                   self.assertEqual(a[i][j], i==j)
                    self.assertEqual(a[i, j], i == j)

    def _index(self, a, r, c):
        return a[r, c]
    
    def test_key_validity(self):
        a = arr.array(10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1)
        self.assertRaises(KeyError, self._index, a, 1, 10)


if __name__ == "__main__":
    unittest.main()
