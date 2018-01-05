'''
Created on Jun 17, 2013
Complex inheritance program
'''
"""
Inheritance test program
"""

import unittest
from inhairitance import Child
from inhairitance import Child2

class TestHair(unittest.TestCase):

    def test_father_hair(self):
        child = Child()
        hair = child.hair()
        print("Child hair is " + hair)
        self.assertNotEqual(hair, "red")
        self.assertNotEqual(hair, "brown")
        self.assertNotEqual(hair, "gray")            
        self.assertEqual(hair, "bald")

    def test_mother_hair(self):
        child = Child2()
        hair = child.hair()
        print("Child hair is " + hair)
        self.assertEqual(hair, "red")
        self.assertNotEqual(hair, "brown")
        self.assertNotEqual(hair, "gray")            
        self.assertNotEqual(hair, "bald")



if __name__ == "__main__":
    unittest.main()    

