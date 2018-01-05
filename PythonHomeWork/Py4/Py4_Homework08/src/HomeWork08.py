'''
Created on Mar 17, 2014
Lesson 8, Project 1
 Here are your instructions:
 Write a program that uses timeit() to show the difference between a list comprehension and the list() 
 function applied to:
  a list of a million random numbers.
  a generator that generates a sequence of a million random numbers. 
 List Comprehension
 ------------------------------------------------------ 
 http://docs.python.org/3/library/timeit.html
'''
from timeit import timeit
from random import randrange, random

listSize = 1000000
numRange = 100

def input_list():
    "create a conventional list and returning that list"
    lst = []
    for x in range(listSize):
        lst.append(randrange(numRange))
    return lst

def input_list2():
    "Creating a list from a comprehensive list and returning that list"
    lst = []
    lst = [randrange(numRange) for x in range(listSize)]  # this creates a comprehensive list
    return lst

def gen_list():
    "creating a generator"
    for x in range(listSize):
        yield randrange(numRange)
        
def comp_list():
#    from random import randrange, random
    "returns a comprehensive list"
    return [randrange(numRange) for x in range(listSize)]


def compare(time):
    "time the length of time that it takes to consume the list"
    "comprehensive list expression"
    comprehensiveListTime = timeit("[randrange(numRange) for x in range(1000000)]", "from HomeWork08 import comp_list,numRange,randrange", number=1)  # 1
#    comprehensiveListTime = timeit("([randrange(numRange) for x in comp_list()])","from HomeWork08 import comp_list,numRange,randrange ", number=1) #2

    print("CompListTime ", comprehensiveListTime, "Input Time ", time)
    
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
    listTime = timeit("(randrange(numRange) for x in input_list())", "from HomeWork08 import input_list,numRange", number=1)
    listTime2 = timeit("(randrange(numRange) for x in input_list2())", "from HomeWork08 import input_list2,numRange", number=1)
    generatorTime = timeit("(randrange(numRange) for x in range(listSize))", "from HomeWork08 import listSize,numRange,randrange", number=1)
    generatorTime2 = timeit("(randrange(numRange) for x in gen_list()) ", "from HomeWork08 import gen_list,numRange", number=1)
    compTime = timeit("([randrange(numRange) for x in comp_list()])", "from HomeWork08 import comp_list,numRange,randrange ", number=1)

#    listTime = timeit("input_list()","from HomeWork08 import input_list", number=1)
#    listTime2 = timeit("input_list2()","from HomeWork08 import input_list2", number=1)
#    generatorTime = timeit("(randrange(100) for x in range(1000000))","from random import randrange", number=1)
#    generatorTime2 = timeit("gen_list() ","from HomeWork08 import gen_list", number=1)
#    compTime = timeit("([randrange(100) for x in range(1000000)])","from random import randrange", number=1)


    "Conventional list construct"
    print("List ", compare(listTime))
    "List created by a comprehensive list construct"
    print("List2 ", compare(listTime2))
    "generator function"
    print("Generator ", compare(generatorTime))
    "generator expression"
    print("Generator2 ", compare(generatorTime2))
    "comprehensive list in function"
    print("Comprehensive Time ", compare(compTime))
    
    
'''
#1
CompListTime  1.590739492520564 Input Time  1.650076584960835
List  ('ComprehesiveTime_Faster', -0.059337092440270967)
CompListTime  1.590811059256116 Input Time  1.5468747861551726
List2  ('ComprehesiveTime_Slower', -0.04393627310094339)
CompListTime  1.5927111418287332 Input Time  7.12816091175128e-06
Generator  ('ComprehesiveTime_Slower', -1.5927040136678214)
CompListTime  1.5883917614426935 Input Time  2.5661379283725694e-06
Generator2  ('ComprehesiveTime_Slower', -1.588389195304765)
CompListTime  1.5915734873472296 Input Time  3.138162006560189
Comprehensive Time  ('ComprehesiveTime_Faster', -1.5465885192129596)

#2
CompListTime  3.133588578519258 Input Time  1.6616150815917812
List  ('ComprehesiveTime_Slower', -1.4719734969274767)
CompListTime  3.125229241654919 Input Time  1.5522799280112773
List2  ('ComprehesiveTime_Slower', -1.5729493136436419)
CompListTime  3.1277568875142006 Input Time  6.843034475512155e-06
Generator  ('ComprehesiveTime_Slower', -3.127750044479725)
CompListTime  3.1289270464094603 Input Time  2.851264364611694e-06
Generator2  ('ComprehesiveTime_Slower', -3.1289241951450957)
CompListTime  3.134004577990062 Input Time  3.1306147097869084
Comprehensive Time  ('ComprehesiveTime_Slower', -0.0033898682031536786)


'''    
