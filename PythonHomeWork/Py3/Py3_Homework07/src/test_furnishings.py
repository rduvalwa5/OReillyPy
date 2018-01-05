'''
Created on Jul 5, 2013

@author: rduvalwa2
'''
import unittest

from furnishings import *

class TestFunishings(unittest.TestCase):

    def test_counter(self):
            HOME = []
            HOME.append(Bed('Bedroom_Master'))
            HOME.append(Bed('Bedroom_Master'))
            HOME.append(Table('Bedroom_Master'))
            HOME.append(Bookshelf('Bedroom_Master'))
            HOME.append(Table('Kitchen'))
            HOME.append(Sofa('Living Room')) 
            HOME.append(Bed('Bedroom_Blue')) 
            myCounts = counter(HOME)
            self.assertEqual(myCounts['Items'], 7, "Total furnishings is incorrect")
            self.assertEqual(myCounts['Beds'], 3, "Total beds is incorrect")
            self.assertEqual(myCounts['Tables'], 2, "Total tables is incorrect")
            self.assertEqual(myCounts['Sofas'], 1, "Total sofas is incorrect")            
            self.assertEqual(myCounts['Bookshelves'], 1, "Total bookshelves is incorrect")    
            
    def test_map(self):
            HOME = []
            HOME.append(Bed('Bedroom_Master'))
            HOME.append(Bed('Bedroom_Master'))
            HOME.append(Table('Kitchen'))
            HOME.append(Sofa('Living Room')) 
            HOME.append(Bookshelf('Den')) 
            
            myMap = map_the_home(HOME)
            print(myMap)
            self.assertTrue(isinstance(myMap['Kitchen'][0], Table), 'Furnishing object is not correct')
            self.assertTrue(isinstance(myMap['Bedroom_Master'][0], Bed), 'Furnishing object is not correct')            
            self.assertTrue(isinstance(myMap['Bedroom_Master'][1], Bed), 'Furnishing object is not correct')
            self.assertTrue(isinstance(myMap['Living Room'][0], Sofa), 'Furnishing object is not correct')
            self.assertTrue(isinstance(myMap['Den'][0], Bookshelf), 'Furnishing object is not correct')
            self.assertFalse(isinstance(myMap['Kitchen'][0], Bookshelf), 'Furnishing object is not correct')
            

if __name__ == "__main__":
    unittest.main()                
