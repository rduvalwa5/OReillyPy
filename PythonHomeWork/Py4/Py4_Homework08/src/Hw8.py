'''
Created on Mar 17, 2014
Lesson 8, Project 1
 Here are your instructions:
 Write a program that uses timeit() to show the difference between a list comprehension and the list() 
 function applied to:
  a list of a million random numbers.
  a generator that generates a sequence of a million random numbers. 
 List Comprehension
 http://docs.python.org/3/library/timeit.html
'''
from timeit import timeit
from random import randrange

ls = []
for x in range(1000000):
    ls.append(randrange(1000000))
    
def compGenerators():
#    print(len(ls))
    listTime = timeit("sum(x for x in ls)", "from __main__ import ls", number=1)
    comprehensiveListTime = timeit("sum([randrange(1000000) for x in range(1000000)])", "from random import randrange", number=1)
    generatorTime = timeit("sum((randrange(1000000)) for x in range(1000000))", "from random import randrange", number=1)
    print("List Time ", listTime)
    print("List Comp Time ", comprehensiveListTime)
    print("Generator Time ", generatorTime)


def compare(time):
    comprehensiveListTime = timeit("(sum([randrange(1000000) for x in range(1000000)]))", "from random import randrange", number=1)
    print("CompListTime ", comprehensiveListTime)
    
    if time > comprehensiveListTime:
        diff = comprehensiveListTime - time
        return ("ComprehesiveTime_Faster", diff)
    elif time < comprehensiveListTime:
        diff = time - comprehensiveListTime
        return ("ComprehesiveTime_Slower", diff)
    else:
        diff = time - comprehensiveListTime
        return ("ComprehesiveTime_Same", diff)
    
if __name__ == "__main__":
#    print(len(ls))
#    compGenerators()
    listTime = timeit("(sum((x) for x in ls))", "from __main__ import ls", number=1)
    generatorTime = timeit("sum((randrange(1000000)) for x in range(1000000))", "from random import randrange", number=1)
    compTime = timeit("(sum([randrange(1000000) for x in range(1000000)]))", "from random import randrange", number=1)
    
    print("List ", compare(listTime))
    print("Generator ", compare(generatorTime))
    print("Comprehensive Time ", compare(compTime))
    
    
