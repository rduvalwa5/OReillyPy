import unittest
from property_address import *

class TestAddresses(unittest.TestCase): 

        def setUp(self): 
            self.home = Address(name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VAA', zip_code='12345-1234')
        
        def test_name(self): 
            self.assertEqual(self.home.name, 'Steve Holden') 
            self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')  
         
        def test_state(self): 
            self.assertEqual(self.home.state, 'VAA') 
            self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state') 
            self.assertRaises(StateError, setattr, self.home, 'state', 'Wa') 
            self.assertRaises(StateError, setattr, self.home, 'state', 'coo') 
            self.assertRaises(StateError, setattr, self.home, 'state', 'BB1')        
            self.home.state = 'COO' 
            self.assertEqual(self.home.state, 'COO') 
     
     
        def test_zip_code(self): 
            self.assertEqual(self.home.zip_code, '12345-1234') 
            self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '12345-654')
            self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '12345A-1234')   
            self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', 'A1234-5555')   
            self.home.zip_code = '54321-1234' 
            self.assertEqual(self.home.zip_code, '54321-1234') 
            
     
if __name__ == "__main__":
    CONFIG_FILE = "/Users/rduvalwa2/DevTools/eclipse-indigo/workspace/Python3_Git/Py3_Git/Python3_Homework12/src/propertyaddress.cfg"
    config = configparser.RawConfigParser()
    config.read(CONFIG_FILE)
    LOG_FORMAT = config.get('log', 'format')
    LOG_FILENAME = config.get('log', 'output')
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format=LOG_FORMAT) 
    unittest.main()
