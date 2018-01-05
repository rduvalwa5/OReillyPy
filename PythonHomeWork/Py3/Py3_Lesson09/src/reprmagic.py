"""
Demonstrate differences between __str__() and __repr__().
determine a little more about the relationship between the two representational methods,
we'll create four different classes that have different combinations of those methods.
"""
 
class neither:
    pass
 
class stronly:
    def __str__(self):
        return "STR"
 
class repronly:
    def __repr__(self):
        return "REPR"
 
class both(stronly, repronly):
    pass
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name
    def __repr__(self):
        return "Person({0.name!r}, {0.age!r})".format(self)  
    
if __name__ == "__main__":
#    from reprmagic import *
    o1 = neither()
    print("neither " , str(o1), repr(o1)) 
    o2 = stronly()
    print("stronly ", str(o2), repr(o2))
    o3 = repronly()
    print("rpronly ", str(o3), repr(o3))
    o4 = both()
    print("both ", str(o4), repr(o4))
    print("o1 ", o1)
    print("o2 ", o2)
    print("o3 ", o3)
    print("o4", o4)
    steve = Person("Steve Holden", 21)
    print(str(steve), repr(steve))
    tim = Person('Tim O\'Reilly', 55)
    print(tim)
    print("The object's name ", tim.name)
    print("The object's age ", tim.age)
    print(tim.__str__())
    print("The object type and attributes ", tim.__repr__())
    
