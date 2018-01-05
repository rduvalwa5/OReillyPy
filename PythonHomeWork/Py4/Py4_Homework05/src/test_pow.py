'''
Created on Feb 1, 2014

@author: rduvalwa2
'''

from math import log 
from timeit import Timer 
import cProfile  as profile
import pstats

def groffle_fast(mass, density): 
    total = 0.0 
    masslog = log(mass * density) 
    for i in range(10000): 
        total += masslog / (i + 1)
    return total

mass = 2.5 
density = 12.0


timer_fast = Timer("total = groffle_fast(mass, density)", "from __main__ import groffle_fast, mass, density") 
print("groffle_fast time:", timer_fast.timeit(number=1000))
profile.run("groffle_fast(mass,density)", "groffleDataFast")
s = pstats.Stats("groffleDataFast")
s.print_stats()


'''
Slow Total:  33.28958002253529  Fast Total:  33.28958002253529
groffle_slow time: 3.785501196049154
groffle_fast time: 1.9862927800277248
'''
