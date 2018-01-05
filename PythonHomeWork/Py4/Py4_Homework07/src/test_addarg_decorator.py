import unittest
from HomeWork7 import myfunc

class project7_TestCase(unittest.TestCase):

        def test_strings(self):
                expected = (1, 'One', 'Two')
                print(myfunc("One", "Two"))
                self.assertEqual(myfunc("One", "Two"), expected)
    
        def test_numbers(self):
                expected = (1, 2, 3, 4, 5)
                print(myfunc(2, 3, 4, 5))
                self.assertEqual(myfunc(2, 3, 4, 5), expected)
                
        def test_tuples(self):
                expected = (1, ("One", 1), ('Two', 2))
                print(myfunc(("One", 1), ('Two', 2)))
                self.assertEqual(myfunc(("One", 1), ('Two', 2)), expected)


if __name__ == "__main__":
    unittest.main()
        
