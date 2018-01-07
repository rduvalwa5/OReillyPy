'''
Created on Jul 30, 2012
@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""factorial.py
   two loops 
   outer loops, variable c counts upward
   inner loop generates the factorial based on value of counter
   The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. from WikiPedia
"""
counter = 0
factorial = 1
while (factorial < 1000):
    print(factorial)
    counter += 1
    factorial = 1
    for n in range (counter, 0, -1): # generate factorial
            factorial = factorial * n