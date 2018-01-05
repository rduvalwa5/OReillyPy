'''
Created on Apr 15, 2014

@author: rduvalwa2
'''
def f(a, *, b, c=2):
    print("A", a, "B", b, "C", c) 
try: f(1, 2)
except TypeError:
    print("TypeError: f() takes 1 positional argument but 2 were given")
try: print(f(1, c=3))
except TypeError:
    print("TypeError: f() missing 1 required keyword-only argument: 'b'")
f(1, b=2, c=3)
f(1, b=2)
try: f("a", "b", "C")
except TypeError:
    print("TypeError: f() takes 1 positional argument but 3 were given")
f("a", b='*')

'''
TypeError: f() takes 1 positional argument but 2 were given
TypeError: f() missing 1 required keyword-only argument: 'b'
A 1 B 2 C 3
A 1 B 2 C 2
TypeError: f() takes 1 positional argument but 3 were given
A a B * C 2
'''
