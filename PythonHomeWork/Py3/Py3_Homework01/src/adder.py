'''
Created on May 28, 2013
Lesson 1, Project 1 Instructions:
  1. Create a Python3_Homework01 project and assign it to your Python3_Homework working set. 
  2  In the Python3_Homework01/src folder, create a program named adder.py;
  3. in it, create a function that takes two objects and adds them together only if they are both of the integer type. 
  4. Raise a TypeError otherwise.  
  5. Then, create a test_adder.py file that tests the correctness of this function.
  6. When they are working to your satisfaction, submit adder.py and test_adder.py.
@author: rduvalwa2
'''

def addIntegers(n1, n2):
            if isinstance(n1, int) and isinstance(n2, int):
                result = n1 + n2
                return result
            else:
                raise TypeError                

if __name__ == "__main__":
        try:
            print(addIntegers(1, 2))
        except TypeError:
            print(TypeError)
        try:    
            print(addIntegers('abc', 56))
        except TypeError:
            print(TypeError)
        try:
            print(addIntegers('21', '56'))
        except TypeError:
            print(TypeError)
        try:
            print(addIntegers('1000000021', '10000000056'))
        except TypeError:
            print(TypeError)
