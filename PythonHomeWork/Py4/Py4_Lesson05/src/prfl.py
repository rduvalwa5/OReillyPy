'''
Created on Jan 5, 2014

@author: rduvalwa2
'''
def f1():
    for i in range(300):
        f2()
        
def f2():
    for i in range(300):
        f3()

def f3():
    for i in range(300):
        pass

def f4():
    for i in range(100):
        f5()

def f5():
    i = 0
    for j in range(100):
        i += j
        
def f6():
    for i in range(100):
        f3()
        
if __name__ == '__main__':
    import cProfile  as profile
    import pstats
    profile.run("f1()", "profiledata")
    s = pstats.Stats("profiledata")
    s.print_stats()
    
    
    
# runs on Mac
# cProfile.run("f1()")

'''
       90304 function calls in 0.745 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.744    0.744 <string>:1(<module>)
      300    0.026    0.000    0.744    0.002 prfl.py:10(f2)
    90000    0.718    0.000    0.718    0.000 prfl.py:14(f3)
        1    0.000    0.000    0.744    0.744 prfl.py:6(f1)
        1    0.000    0.000    0.745    0.745 {built-in method exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
