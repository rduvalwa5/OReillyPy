'''
Created on Mar 22, 2014

@author: rduvalwa2
'''
import inspect
from arr import array

class A:
    a = 10
    b = 20
    def __init__(self):
            self.c = 30

    def multiply(self, num):
        return self.a * self.b * num
    
    def print_out(self):
        print(self.multiply())

def get_user_attributes(cls):
    boring = dir(type('dummy', (object,), {}))
    return [item
            for item in inspect.getmembers(cls)
            if item[0] not in boring]



if __name__ == "__main__":
    '''
    print(inspect.getmembers(A,inspect.isfunction))
    for ob in inspect.getmembers(A,inspect.isfunction):
        print(ob[0])
        print(inspect.getfullargspec(ob[1]))
    print(inspect.getmembers(array,inspect.isfunction))
    for ob in inspect.getmembers(array,inspect.isfunction):
        print(ob[0])
        print(inspect.getfullargspec(ob[1]))          
    '''
    a = A()
    print(a.multiply(4))
    if inspect.ismethod(a.multiply):
        print("a.multiply Is Bound Method ")
    if not inspect.ismethod(A.multiply):
        print("A.multiply Is NOT Bound Method ")

    for member in inspect.getmembers(inspect, inspect.isclass):
        print(member[0])
        
    print(inspect.getargspec(A.multiply))    
