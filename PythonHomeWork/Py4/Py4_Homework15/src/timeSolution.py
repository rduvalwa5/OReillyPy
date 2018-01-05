'''
Created on Apr 12, 2014
@author: rduvalwa2
'''
from Py4_HomeWork_15 import Homework15
from timeit import timeit

        
chunks = [1, 10, 100, 200, 1000, 10000 , 100000, 1000000]  # ,10000000]
# chunk = 10000
for chunk in chunks:
    fileName = "meth1.txt"
    x = Homework15().firstTechnique(10000000, chunk, fileName)
    print("firstTechnique", timeit("x", "from __main__ import x"))
