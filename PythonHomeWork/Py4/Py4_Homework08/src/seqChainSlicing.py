'''
Created on Mar 12, 2014
demonstrates the use of chaining and slicing on generated sequences
@author: 310122001
'''
import itertools

s1 = (1, 3, 5, 7, 11)
s2 = ['one', 'two', 'three', 'four']
def sqq(n):
    for i in range(n):
        yield i * i
        
s3 = sqq(10)

inp = itertools.chain(s1, s2, s3)
for element in inp:
    print(element)
print("recharge input")
inp = itertools.chain(s1, s2, s3)
chained = []
print("inp", inp)
for el in inp:
    chained.append(el)
print("chanined ", chained)
print("1 = input, 2 = indext start, 3 = index of last on e in result,4 = stride")
print(list(itertools.islice(inp, 2, 7, 2)))
"important here to observe that the second operation on the chained sequences starts with the first element not consumed  by the previous operation."
print(list(itertools.islice(inp, 3)))
s4 = list(itertools.chain(s1, s2))
for el in sqq(10):
    s4.append(el)
print(s4)

    
