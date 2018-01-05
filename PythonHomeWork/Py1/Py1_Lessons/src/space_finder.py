'''
Created on Jul 22, 2012

@author: rduvalwa2
'''
#!/usr/bin/python3
""" space_finder.py
   Program finds the first space and ends before iterating thru the complete str
ing. """

s = input("Input a string with a space: ")
pos = 0
for c in s:
  if c == " ":
     pos += 1
     print("First space occurred at position", pos)
     break
  pos += 1
else:
  print("Final character was ", c,"and no spaces were found." )
