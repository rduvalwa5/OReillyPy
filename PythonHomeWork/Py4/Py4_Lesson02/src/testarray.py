"""
Test list-of-list array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    print("Array")
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                for j in range(N):
                    self.assertEqual(a[i, j], 0)
       
    def test_identity(self):
        print("Identity")
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                a[i, i] = 1
            for i in range(N):
                for j in range(N):
                    self.assertEqual(a[i, j], i == j)
                    
    def _index(self, a, r, c):
        print("Index Called")
        return a[r, c]

    def test_key_validity(self):
        print("Key")
        a = arr.array(10, 10)
        print()
        self.assertRaises(KeyError, self._index, a, 10, 10)
        self.assertRaises(KeyError, self._index, a , -1, 1)
        self.assertRaises(KeyError, self._index, a , 10, 1)
        self.assertRaises(KeyError, self._index, a , 1, -1)
        self.assertRaises(KeyError, self._index, a , 1, 10)

    
if __name__ == "__main__":
    unittest.main()


