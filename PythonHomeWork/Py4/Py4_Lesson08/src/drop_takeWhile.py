'''
Created on Mar 12, 2014

@author: 310122001
'''
import itertools
def lt5(n):
    return n <= 5
s1 = [1, 3, 2, 4, 5, 6, 4, 2, 3, 1]
"Drops all values that are less than 5 until is reaches a value that is not less than 5"
print(list(itertools.dropwhile(lt5, s1)))
"Returns all values that are less than 5 until is reaches a value that is not less than 5"
print(list(itertools.takewhile(lt5, s1)))
