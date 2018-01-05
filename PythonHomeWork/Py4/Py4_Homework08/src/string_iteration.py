'''
Created on Mar 16, 2014
this exercise it to prove my point that list can be iterated
@author: rduval
'''
strg = "abcssdfrtbyhf"
inLst = list(strg)
print(inLst)
lst = []
for ch in strg:
    if ch in lst:
        print("Did not add ", ch, " to list")
    if ch not in lst:
        lst.append(ch)       
        
print(lst)
    
