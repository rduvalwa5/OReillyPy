'''
Created on Jul 30, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
""" personlist.py 
    Produce a listing of people's names, ages and weights."""
data = [
        ("Steve", 59, 202),
        ("Dorthy", 49, 156),
        ("Simom",39, 155),
        ("David", 61, 135)]
print("Print formated data row")
for row in data:
   print("{0[0]:<12s} {0[1]:4d} {0[2]:4d}".format(row))
print("Better code look")
for name, age, weight in data:
   print("{0:<12s} {1:4d} {2:4d}".format(name, age, weight))
print("Version 3 Better code look")
for name, age, weight in data:
    print("{0:.<30s} {1:4d} {2:4d}".format(name, age, weight))   # pad with periods for a width of 30
print("My Reverse look")
for weight, age, name in data:
   print("{2:4d} {1:4d} {0:<12s}".format(weight, age, name))