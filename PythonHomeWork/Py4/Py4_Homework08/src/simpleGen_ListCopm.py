'''
http://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension
Created on Mar 17, 2014
(x*2 for x in range(256))

# List comprehension
[x*2 for x in range(256)]
other links
http://stackoverflow.com/questions/4402858/pythons-generator-expression-at-least-3x-faster-than-listgenerator-expres

@author: 310122001
'''
from timeit import timeit

ls = []
for x in range(1000000):
    ls.append(x)

# print(ls)

print("List", timeit("print(sum((x*2) for x in ls))", "from __main__ import ls", number=1))
print("Generator", timeit("print(sum((x*2) for x in range(1000000)))", "", number=1))
print("List Comprehension", timeit("print(sum([x*2 for x in range(1000000)]))", "", number=1))
