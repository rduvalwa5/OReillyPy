"""
Test list-of-list array implementations using tuple subscripting.
"""
import unittest
import arr_dict3D

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr_dict3D.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for d in range(N):
                        self.assertEqual(a[i, j, d], 0)

    def test_identity(self):
        for N in range(4):
            a = arr_dict3D.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for d in range(N):
                        print("d is ", d)
                        print("i is", i)
                        print("j is ", j)
                        print(a[i, j, d])
                        print("i==j==d", i == j == d)
                        self.assertEqual(a[i, j, d], i == j == d)
                    
    def _index(self, a, r, c, d):
        return a[r, c, d]

    def test_key_validity(self):
        a = arr_dict3D.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a , -1, 1, 1)
        self.assertRaises(KeyError, self._index, a , 10, 1, 1)
        self.assertRaises(KeyError, self._index, a , 1, -1, 1)
        self.assertRaises(KeyError, self._index, a , 1, 10, 1)

if __name__ == "__main__":
    unittest.main()
