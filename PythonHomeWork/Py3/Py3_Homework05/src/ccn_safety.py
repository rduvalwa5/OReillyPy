'''
Created on Jul 1, 2013
Instructions:
1. Create a Python3_Homework05 project
2. assign it to your Python3_Homework working set
3. Python3_Homework05/src folder, create a program named ccn_safety.py
   a. with a function that substitutes X for all but the last four digits of any credit card numbers
      in a string, returning the updated string as its result. 
   b. Use the following text as a sample:
   Text to use in ccn_safety.py
   Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously 
   fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be 
   real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts.
4. Your project should meet the following conditions:
   1. it only needs to convert numbers of the form XXXX-XXXX-XXXX-XXXX.
   2. The program should return this text: 
      "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously 
       fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number that appears to be 
       real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts." 
   3. Note that the phone numbers should not be replaced! 
   4. You should include a test_ccn_safety.py program in a separate file that confirms that your code 
      functions as expected.
@author: rduvalwa2
'''
import re

# text = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts." 

def ccn_safety(text):
    return re.sub("\d{4}-\d{4}-\d{4}-", "XXXX-XXXX-XXXX-", text)

# if __name__ == '__main__':
#    result = ccn_safety(text)
#    print(result)

