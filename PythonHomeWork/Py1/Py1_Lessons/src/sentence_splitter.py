'''
Created on Jul 22, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""sentence_spitter.py
   Splits sentences into words."""
s = input("Enter a sentence: ")
print("Input: ",s)
while True:  #continue to execute until the end of the sentence
    while s.startswith(" ") or s.startswith("\t"): #remove leading spaces
        s = s[1:] #start string s at position 1 not 0
    pos = 0
    for c in s:
       if c == " " or c == "\t":
          print(s[:pos])  #print s to postion of the space
          s = s[pos+1:]   #set new string that starts at the position of space plus 1
          break
       pos += 1
    else:
      print(s)
      break