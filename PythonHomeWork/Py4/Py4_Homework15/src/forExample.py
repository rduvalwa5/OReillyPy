'''
Created on May 11, 2014

@author: rduvalwa2
'''

def forExample(x):
    for a, b in x:
        yield a, b
    
if __name__ == "__main__":
    x = [("abc", 2), ("xyz", 10)]
    
    for size, slots in forExample(x):
        print(size)
        print(slots)
        
        
        
" 1000 B9999s    =  timeControl 0.37429375998908654"
" 100 B99999s   = timeControl  0.3761624449980445"
" 10 B999999s  = timeControl  0.3628144640097162"
" 1  B9999999s = timeControl  0.3754035330057377"
