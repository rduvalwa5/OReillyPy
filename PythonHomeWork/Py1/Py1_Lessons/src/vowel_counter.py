'''
Created on Jul 22, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""Counts vowels in a user input string.
   vowel_counter.py
"""

s = input("Enter string: ")
vcount = 0
for c in s:
  if c in "aeiouAEIOU":
    vcount += 1
#    print("C is ", c, "; Vowel Count:", vcount)
#To make this code print only the final count remove the print from the for loop indention
#Remeber that indention is important to Python
print("Vowel Count:", vcount)