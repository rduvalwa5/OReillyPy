'''
Created on Apr 15, 2014

@author: rduvalwa2
'''
import functools

def fp(a, b, c="summat", d="nowt"):
        print("a b c d:", a, b, c, d)
print("function fp()")
fp("ayeup", "geddaht")
# a b c d ayeup geddaht summat nowt
fp1 = functools.partial(fp, 1, b=2)
print("partial function fp1()")
fp1()
# a b c d 1 2 summat nowt
try:
    fp1("ayeup", "geddaht")
except TypeError:
    print("TypeError fp() got multiple values for argument 'b'")
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: fp() got multiple values for keyword argument 'b'
print("partial function fp1(c=\"ayeup\", d=\"geddaht\")")
fp1(c="ayeup", d="geddaht")
# a b c d 1 2 ayeup geddaht
fp2 = functools.partial(fp, 1, c="two")
try:
    fp2("ayeup", "geddaht")
except TypeError:
    print("TypeError: fp() got multiple values for argument 'c'")
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: fp() got multiple values for keyword argument 'c'
print("fp2")
fp2
# <functools.partial object at 0x10063d6d8>
print("partial function fp2(\"ayeup\", c=\"geddaht\")")
fp2("ayeup", c="geddaht")
# a b c d 1 ayeup geddaht nowt
