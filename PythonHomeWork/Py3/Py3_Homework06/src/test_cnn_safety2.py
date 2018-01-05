'''
Created on Jul 1, 2013
@author: rduvalwa2
'''
import unittest
import re
from ccn_safety2 import ccn_safety2

text = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
expd = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts." 
result = ccn_safety2(text)

class TestCcnSafetyRegex(unittest.TestCase):
    """
    Brute force expected string compare
    Not very efficient
    """
    def test_expect_string(self):
        self.assertEqual(expd, result, "Strings don not match")
        
    """
    Search for an expected phone number format and expect to find it
    """
    def test_tel_num_not_changed(self):
        self.assertIsNotNone(re.search("\d{3}-\d{3}-\d{4}", result), "Phone number format was changed")
    """
    Search for an expected credit card altered format and expect to find it
    """        
    def test_altered_ccn(self):
        self.assertIsNotNone(re.search("CCN REMOVED FOR YOUR SAFETY", result), "Credit Card Number not changed")    
    """
    Search for an unexpected credit card format and expect not to find it
    """        
    def test_ccn_format_not_found(self):
        self.assertIsNone(re.search("\d{4}-\d{4}-\d{4}-\d{4}", result), "Unaltered credit card number was found")
                        
if __name__ == "__main__":
    unittest.main()

