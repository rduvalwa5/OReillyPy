'''
 Here are your instructions:
   1. Create a Python3_Homework03 project and assign it to your Python3_Homework working set. 
   2. In the Python3_Homework03/src folder, create a file named decoder.py
   3. which contains an iterator named alphabator
      a.  When passed a list, simply return objects as-is unless they are integers
        between 1 and 26
      b. in which case it should convert that number to the corresponding letter.
       The integer-to-letter correspondence is 1=A, 2=B, 3=C, 4=D, and so on.
   4.  use any technique you've learned in lesson 3 to execute this project
   5.Your alphabator iterator must pass the unittest below:
     test_decoder.py
'''
# def alphabator(lst):
#    b = []
#    for i in lst.__iter__():
#            if isinstance(i,int) and i in range(1,27):
#                b.append(chr(96 + i).upper())
#            else:
#                b.append(i)
#    return b

def alphabator(lst):
    b = []
    it = lst.__iter__()
    while it:
        try:
            nxt = it.__next__()
            if isinstance(nxt, int) and nxt in range(1, 27):
                b.append(chr(96 + nxt).upper())
            else:
                b.append(nxt)
        except StopIteration:
            return b
            

if __name__ == "__main__":
        lst = [1, '2', 'A', 'b', 26, 19, 100, 1000001, 27]
        x = alphabator(lst)
        
        print("x is: " + str(x))
