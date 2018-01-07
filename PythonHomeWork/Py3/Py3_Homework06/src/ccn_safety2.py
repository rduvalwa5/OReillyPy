'''
Created on Jul 2, 2013
@author: rduvalwa2
Instructions:
1. Create a Python3_Homework06 project and assign it to your Python3_Homework working set
2. In the Python3_Homework06/src folder, create a program named ccn_safety2.py 
   that duplicates the ccn_safety.py program's functionality, but uses a compiled regular expression to replace 
   the credit card numbers in the paragraph with "CCN REMOVED FOR YOUR SAFETY". 
3. Text to use in ccn_safety2.py
   "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
4. Your project should meet the following conditions:
   The program should return this text: 
   "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts." 
5. Note that phone numbers should not be replaced! 
6. You should include a test_ccn_safety2.py program in a separate file that confirms that your code functions as expected. 
7. You must use the re.VERBOSE flag to properly document each element of the pattern used to identify credit card numbers.
8. Submit ccn_safety2.py and test_ccn_safety2.py when they are working to your satisfaction.
'''
import re

text = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
extd = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts." 
def ccn_safety2(text):
        regex = re.compile(r"\d{4}-\d{4}-\d{4}-\d{4}")  # ,"CCN REMOVED FOR YOUR SAFETY")
        return re.sub(regex, "CCN REMOVED FOR YOUR SAFETY", text)

if __name__ == '__main__':
#    ccn_safety(text)
#    print(result)
    import unittest
    class Test_Ccn_Safety(unittest.TestCase):
        def test_attributes(self):
            result = ccn_safety2(text)
            self.assertEqual(extd, result)
    unittest.main()
