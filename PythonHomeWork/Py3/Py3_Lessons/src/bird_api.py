'''
Created on Jun 16, 2013
API for software birds carrying objects
@author: rduval
'''
from bunchclass import Bunch

class Bird(Bunch):
    """
    API for software birds carrying objects.
    """
    def pretty(self):
        """
        Replacement pretty() method
        """
        return "pretty bird!"
    def add(self, name,value):      
        """
        add an object for Bird to carry in its bask
        Name is string 
        Value is object being put in basket
        """
        if hasattr(self,name):
            raise KeyError("'%' object cannot be placed in basket")
        else:
            setattr(self,name,value)
        
    def remove(self, name):
        """
        Remove object form basket
        """
        if name in self.__dict__:
            delattr(self,name)
        else:
            raise KeyError("'%s' object not found in basket")
        
    def calculate(self):
        """
        Calculate speed of bird
        algorithm: 100 = (5 * number of objects in basket)
        result cannot be less than zero
        """
        return max(100 - len(self.__dict__) * 10, 0)
        #returns the greater of two 
    def basket(self):
        """
        Print in attractive format the list of objects in the basket
        """
        return "Basket Objects\n" + self.pretty()
if __name__ == "__main__":
    swallow = Bird(fruit=("coconut","orange"), drink="apple juice")
    swallow.add("cars", 3)
    print(swallow.basket())
    print(swallow.calculate())
    swallow.remove("drink")
    print(swallow.basket())
    print(swallow.calculate())
    swallow.remove("fruit")
    print(swallow.calculate())
    for item in range(12):
        swallow.add("rocks" + str(item), 1)
    print("Basket length is ", len(swallow.__dict__))
    print(swallow.calculate())
#    help(swallow)
    
    
        