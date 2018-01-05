'''
Created on Jun 17, 2013
Instructions:
1. Create a Python3_Homework02 project
   - assign it to your Python3_Homework working set
     the Python3_Homework02/src folder create a file named coconuts.py
2. Create an inventory class that tracks different types of coconuts from around the world
   - different types of coconuts must have these weight attribute weights:
     Type             Weight 
     South Asian        3 
     Middle Eastern    2.5 
     American          3.5 
3. inventory class must have the following methods:
   - add_coconut() accepts a coconut as an argument
       - Other types throw an AttributeError. 
   - total_weight() provides the total weight of coconuts
4. For this project, you may find the isinstance built-in useful
5. test_coconuts.py program to confirm all the Inventory class methods
   The tests must check:
   - That different coconut types each have a different weight. 
   - if a string object is passed to the Inventory.add_coconut method
     -  an AttributeError is thrown 
6. if 2 South Asian, 1 Middle Eastern, and 3 American coconuts are added to the inventory
   - the Inventory.total_weight() method returns 19
7  When they are working, submit coconuts.py and test_coconuts.py
@author: rduvalwa2
'''
import unittest
from coconut import American
from coconut import MiddleEastern
from coconut import SouthAsian
from coconuts import Inventory

class Test_Coconuts(unittest.TestCase):
        """
        Test that each CLASS of coconut has a different weight
        """
        def testCoconutTypeWeights(self):
            self.assertNotEqual(American().weight, SouthAsian().weight, "American and South Asian weigh the same.") 
            self.assertNotEqual(American().weight, MiddleEastern().weight, "American and MiddleEastern weigh the same.") 
            self.assertNotEqual(MiddleEastern().weight, SouthAsian().weight, "MiddleEastern and South Asian weight the same.") 

        """
        Test Add Coconuts to an inventory
        """
        def testAddToInventory(self):
                self.AmercanInv = Inventory
                """
                Clear out list to assure empty list
                """
                del self.AmercanInv.coconuts[:]
                for i in range(3):
                    self.AmercanInv.add_coconut(self.AmercanInv, American())
                self.assertEqual(3, len(self.AmercanInv.coconuts))

        """
        Test Attribute Error
        """            
        def testAttributeError(self):
                self.AmercanInv = Inventory
                self.assertRaises(AttributeError, self.AmercanInv.add_coconut, self.AmercanInv, "American") 

        """
        Test weight total
        """
        def testTotalInventoryWeight(self):
                self.mixedInv = Inventory
                """
                Clear out list to assure empty list
                """
                del self.mixedInv.coconuts[:]
                for i in range(3):
                    self.mixedInv.add_coconut(self.mixedInv, American())
                for i in range(2):
                    self.mixedInv.add_coconut(self.mixedInv, SouthAsian())
                self.mixedInv.add_coconut(self.mixedInv, MiddleEastern())
                self.assertEqual(19, self.mixedInv.total_weight(self.mixedInv))
            
if __name__ == "__main__":
    unittest.main()
