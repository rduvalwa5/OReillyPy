'''
Created on Jun 17, 2013
Instructions:
1. Create a Python3_Homework02 project
   - assign it to your Python3_Homework working set
     the Python3_Homework02/src folder create a file named coconuts.py
2. Create an inventory class that tracks different types of coconuts from around the world
   - different types of coconuts must have these weight attribute values:
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

from coconut import Coconut

class Inventory(object):
    coconuts = []
    def add_coconut(self, nut):
        """
        add coconut
        """
        coco = nut
        if isinstance(coco, Coconut):
            self.coconuts.append(coco)
        else:
            raise AttributeError   
            
    def total_weight(self):
        """
        Total weight of coconuts
        """
        total = 0
        for item in self.coconuts:
            total += item.weight
        return total

            
if __name__ == "__main__":
    
    from coconut import American

    print(isinstance(American(), Coconut))
    AmericanInv = Inventory
    print(isinstance(AmericanInv(), Inventory))
    for i in range(4):
        AmericanInv.add_coconut(AmericanInv, American())
    print(AmericanInv())
    for item in AmericanInv.coconuts:
        print(type(item), item.weight)
    print(AmericanInv.total_weight(AmericanInv))
    print(AmericanInv.add_coconut(AmericanInv, "abcd"))

