""" 
Here are your instructions:
Project: 
Take the following function and using timings (and profiling if necessary to determine where the program is spending its time),
reduce its execution time as much as you can. 
You should be able to get it down to less than one third of what it is now.   
Test both functions in the same file (the original and your faster version) to compare their respective execution times.  
Also confirm that they give the same answer.
""" 
from math import log 
from timeit import Timer 
import cProfile  as profile
import pstats

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog / (i + 1)
    return total

def groffle_fast(mass, density): 
    total = 0.0 
    masslog = log(mass * density) 
    for i in range(10000): 
        total += masslog / (i + 1)
    return total

mass = 2.5 
density = 12.0

# print("Slow Total: ", groffle_slow(mass, density)," Fast Total: ", groffle_fast(mass, density))
timer = Timer("total = groffle_slow(mass, density)", "from __main__ import groffle_slow, mass, density") 
print("groffle_slow time:", timer.timeit(number=1000))

# profile.run("groffle_slow(mass,density)","groffleData")
# s = pstats.Stats("groffleData")
# s.print_stats()

timer_fast = Timer("total = groffle_fast(mass, density)", "from __main__ import groffle_fast, mass, density") 
print("groffle_fast time:", timer_fast.timeit(number=1000))
# profile.run("groffle_fast(mass,density)","groffleDataFast")
# s = pstats.Stats("groffleDataFast")
# s.print_stats()

'''
Slow Total:  33.28958002253529  Fast Total:  33.28958002253529
groffle_slow time: 3.7504659210098907
groffle_fast time: 1.9904523799777962

Slow Total:  33.28958002253529  Fast Total:  33.28958002253529
groffle_slow time: 3.7758633919875138
Sat Feb  1 22:59:33 2014    groffleData

         10004 function calls in 0.005 seconds

   Random listing order was used

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
    10000    0.001    0.000    0.001    0.000 {built-in method log}
        1    0.004    0.004    0.005    0.005 /Users/rduvalwa2/DevTools/eclipse-indigo/workspace/Python3_Git/Py4_Git/Py4_Git/Py4_Lesson_5_Homework/src/groffle.py:15(groffle_slow)
        1    0.000    0.000    0.005    0.005 {built-in method exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


groffle_fast time: 2.0146401840029284
Sat Feb  1 22:59:35 2014    groffleDataFast

         5 function calls in 0.002 seconds

   Random listing order was used

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method log}
        1    0.000    0.000    0.002    0.002 {built-in method exec}
        1    0.002    0.002    0.002    0.002 /Users/rduvalwa2/DevTools/eclipse-indigo/workspace/Python3_Git/Py4_Git/Py4_Git/Py4_Lesson_5_Homework/src/groffle.py:22(groffle_fast)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
