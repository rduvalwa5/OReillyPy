'''
Created on Mar 18, 2014

@author: 310122001
'''
'''
Created on Mar 17, 2014
This demonstrates List Comprehension
'''
from random import randrange
" List "
myList = []
for x in range(10):
    myList.append(x ** 2)
    
print("List ", myList)
print(type(myList))

"ListComprehension"
ListComprehension = []
ListComprehension = [x ** 2 for x in range(10)] 
print("ListComprehension ", ListComprehension)
print(type(ListComprehension))

"Generator"
generated = ((x ** 2) for x in range(10))
print("generated", generated)
for x in range(5):
    print(next(generated))
print(type(generated))

"LambdaList"
squaresLambdaList = []
squaresLambda = map(lambda x: x ** 2, range(10))
squaresLambdaList = list(squaresLambda)
print("squaresLambdaList ", squaresLambdaList)
print(type(squaresLambda))


