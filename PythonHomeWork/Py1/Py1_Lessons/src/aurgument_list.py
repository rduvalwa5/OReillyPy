'''
Created on Aug 10, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
""" argument_list.py 
    demonstrates passing multiple parameters  """

product = 0  #declaring these here makes them global
quotient = 0

def multiplier(*args):
    """ multiply arguments together and return the result modified to return two variables, product and a quotient"""
    if not args:
        return product, quotient
    product = args[0] # initialized to 0, to the first parameter
    for a in args[1:]: # the next series of parameters are the arguments   
       product *= a
    quotient = product / 3
    return product , quotient

print(multiplier())
print(multiplier(1,2,3,4))
print(multiplier(6,7,8,9,10,11,12,13))
print(multipliera(10,20,100)                                                                                                  