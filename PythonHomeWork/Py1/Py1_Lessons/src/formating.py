'''
Created on Jul 30, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""formatting.py
   accept format strings from the user and format fixed data"""
i = 42
r = 31.97
c = 2.2 + 3.3j
s = "String"
lst = ["zero","one","two","three","four","five"]
dct = {"Jim":"Dandy",
       "Stella": "du Boius",
       1:"integer"}
#print("Format:", s, "output:", s.format(i, r, c, s, e=lst, f=dct))       
while True:
    fmt = input("Format strings: ")
    if not fmt:
        break
    fms = "{"+fmt+"}"
#    print(fms)
#    print("Format:", s, "output:", s.format(i, r, c, s, e=lst, f=dct))
    print("Format:", fms, "output:", fms.format(i, r, c, s, e=lst, f=dct))