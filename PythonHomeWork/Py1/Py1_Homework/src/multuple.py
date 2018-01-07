#!/usr/local/bin/python3
""" multuple.py 
    formating problem """

myTuple = [(1,1),(2,2),(3,3),(5,5),(7,7),(11,11),(3,101),(101,33)]

for element in myTuple:
   product = element[0] * element[1]
   n = {'value': product, 'multiplicand': element[0], 'multiplier': element[1]}
   print("{0[value]:4d} = {0[multiplicand]:3d} x {0[multiplier]:3d}".format(n))
