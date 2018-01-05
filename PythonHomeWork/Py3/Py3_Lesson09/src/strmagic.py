"""
Demonstrate string representations using inheritance
"""
class Person:
    """
    Represents a person
    does not have an __str__() method 
    """
    def __init__(self, name):
        self.name = name
 
class NamedPerson(Person):  
    """
    Represents a person using their name,
     NamedPerson has an __str__() method
    """
    def __str__(self):
        return self.name
    
if __name__ == "__main__":
#    from strmagic import *
    print("1. ", "Danny Greenfiled".__str__())
    p1 = Person("Danny Greenfield")
    print("2. ", p1.__str__())
    print("3. " , p1)
    p2 = NamedPerson("Danny Greenfiled")
    print("4. " , p2)
    print("5. " , p2.__str__())
    
