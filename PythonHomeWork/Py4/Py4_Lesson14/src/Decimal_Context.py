'''
Created on Apr 22, 2014
Demonstration of Decimal Context
@author: rduval
'''
from decimal import *
myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)
setcontext(myothercontext)
print("getContext()", getcontext())
print(Decimal(1) / Decimal(7))
print(ExtendedContext)
setcontext(ExtendedContext)
print("ExtendedContext" , getcontext())
print(Decimal(1) / Decimal(7))
print("infinity", Decimal(42) / Decimal(0))
setcontext(BasicContext)
print("BasicContext", getcontext())
try:
    Decimal(42) / Decimal(0)
except Exception:
     print("Exception decimal.DivisionByZero")
with localcontext() as ctx:
      ctx.prec = 42
      s = Decimal(1) / Decimal(7)
      print(s)
  
s = +s
print(s)

'''
getContext() Context(prec=60, rounding=ROUND_HALF_DOWN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
0.142857142857142857142857142857142857142857142857142857142857
Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[])
ExtendedContext Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[])
0.142857143
infinity Infinity
BasicContext Context(prec=9, rounding=ROUND_HALF_UP, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[Clamped, InvalidOperation, DivisionByZero, Overflow, Underflow])
Exception decimal.DivisionByZero
0.142857142857142857142857142857142857142857
0.142857143
'''
