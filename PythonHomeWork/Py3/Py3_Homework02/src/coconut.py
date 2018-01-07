'''
Created on Jun 18, 2013
@author: rduvalwa2
'''

class Coconut():
    pass
        
class American(Coconut):
        weight = 3.5
            
class MiddleEastern(Coconut):
        weight = 2.5
 
class SouthAsian(Coconut):
        weight = 3
       
        
if __name__ == "__main__":
    import unittest
    class TestCoconut(unittest.TestCase):
 
        def test_AmericanClassWeight(self):
            self.assertEqual(3.5, American.weight)

        def test_AmericanInstanceWeight(self):
            american = American()
            american.weight = 4
            self.assertEqual(4, american.weight)

        def testObjectInstance(self):
            self.assertTrue(isinstance(American(), Coconut), "American  is not an instance of Coconut")
                
    unittest.main()
