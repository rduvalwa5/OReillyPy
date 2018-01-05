'''
Created on Apr 15, 2014

@author: rduvalwa2
'''
import inspect
a, b, c = "Module a", "Module b", "Module c" 
def outer():
    def inner():
        nonlocal b
        global c
        a = "Inner a"
        b = "Inner b"
        c = "Inner c"
        print("inner", a, b, c)  # inner Inner a Inner b Inner c
    a = "Outer a"
    b = "Outer b"
    c = "Outer c"
    print("outer 1", a, b, c)  # outer 1 Outer a Outer b Outer c
    inner()
    print("outer 2", a, b, c)  # outer 2 Outer a Inner b Outer c
print("module 1", a, b, c)  # module 1 Module a Module b Module c
outer()
print("module 2", a, b, c)  # module 2 Module a Module b Inner c
for name in inspect.getmembers(outer()):
        print(name)


'''
if __name__ == "__main__":
    import inspect
#    from nonlocal import outer
    a = outer()
#    for name in a.__dir__():
#        print(name)
    for name in inspect.getmembers(a):
        print(name)
        

 module 1 Module a Module b Module c
 outer 1 Outer a Outer b Outer c
 inner Inner a Inner b Inner c
 outer 2 Outer a Inner b Outer c
 module 2 Module a Module b Inner c
'''
