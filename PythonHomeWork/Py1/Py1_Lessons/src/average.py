'''
Created on Aug 8, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
""" average.py 
     Averages a list, tuple or set of numeric values"""

def average(lst):
    return sum(lst) / len(lst)

tst_lst = [1,2,3,4]
print('Average this list: {0}'.format(tst_lst))
print(average(tst_lst))

t = (243,132,987,342,13)
print('Average this tuple: ',t)
print(average(t))
s = {1,2,3,4,25}
print('Average the set: {0}'.format(s))
print(average(s))