'''
Created on Mar 17, 2014
This demonstrates List Comprehension
'''
from random import randrange

squaresConventional = []
lstBig = []
listSize = 10
myList = []
for x in range(10):
    squaresConventional.append(x ** 2)
    
squaresEmbedForLoop = []
squaresEmbedForLoop = [x ** 2 for x in range(10)] 
print("squaresEmbedForLoop ", squaresEmbedForLoop)

squaresLambdaList = []
squaresLambda = map(lambda x: x ** 2, range(10))
squaresLambdaList = list(squaresLambda)

generated = ((x ** 2) for x in range(10))
print("generated", generated)
for x in range(5):
    print(next(generated))
print(next(generated))


def embeddedList(lSize):
        return [randrange(lSize) for x in range(lSize)]

print("embedddd ", embeddedList(listSize))   
    
print("squaresConventional \n", squaresConventional)
print("squaresEmbedForLoop \n", squaresEmbedForLoop)
print("squaresLambda \n", list(squaresLambda))
print("squaresLambda type ", type(squaresLambda))
print(type(list(squaresLambda)))
for element in squaresLambda:
    print(element)
if squaresEmbedForLoop == list(squaresLambda):
    print("squaresEmbedForLoop equals squaresLambda")
else:
    print("squaresEmbedForLoop NOT equal squaresLambda")
    print(len(squaresEmbedForLoop), " NOT ", len(list(squaresLambda)))

if squaresEmbedForLoop == squaresLambdaList:
    print("squaresEmbedForLoop equals squaresLambdaList")
    print(len(squaresEmbedForLoop), " equals ", len(squaresLambdaList))
else:
    print("squaresEmbedForLoop NOT equal squaresLambdaList")

test1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
test2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
if test1 == test2:
    print("test1 equals test2")
else:
    print("test1 NOT equals test2")

