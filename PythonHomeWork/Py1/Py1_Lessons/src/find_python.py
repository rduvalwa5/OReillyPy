'''
Created on Jul 4, 2014

@author: rduvalwa2
'''

#!/usr/local/bin/python3
"""Detect any mention of Python in the user input"""

uin = input("Please enter a sentence: ")
if "python" in uin.lower():
   print("You mentioned Python.")
elif "perl" in uin.lower():
   print("You mentioned Perl")
elif "ruby" in uin.lower():
   print("You mentioned Ruby")
else:
   print("Not mentioned any language....")
