'''
Created on Jul 5, 2013
@author: rduvalwa2
Instructions:
1. Create a Python3_Homework07 project and assign it to your Python3_Homework working set
2  In the Python3_Homework07/src folder, create a program named furnishings.py
   that includes a Furnishing class
3. During instantiation, this class should ask for a "room" argument
4. create the following classes that inherit from the Furnishing class:
   a. Sofa
   b. Bookshelf
   c. Bed
   d. Table
5. Use the built-in list type to record the furniture in your own home 
   that matches the classes above. 
   So for example, you might have:
   >>> from furnishings import * >>> home = [] >>> home.append(Bed('Bedroom'))>>> 
   home.append(Sofa('Living Room'))
6. write a map_the_home() function to convert that to a built-in dict type where the rooms are the
   individual keys and the associated value is the list of furniture for that room. 
   If we ran that code against what we display in our command line, we might see:
   >>> map_the_home(home){'Bedroom': [<__main__.Bed object at 0x39f3b0>], 'Living Room': 
   [<__main__.Sofa object at 0x39f3b0>]} 
7. Also write a counter() function that prints the types of furniture and how many there are
   of each type. The results, based on our example:
   >>> counter(home)Beds: 1Bookshelves: 0Sofas: 1Tables: 0
8. Your project should meet the following conditions:
   a. The program should be able to produce the same results as the list above. 
   b. You should include a test_furnishings.py program that tests the map_the_home() function.
Submit furnishings.py and test_furnishings.py when they are working to your satisfaction.
'''
from collections import defaultdict

class Furnishing(object):
        def __init__(self, room):
            self.room = room

class Sofa(Furnishing):
            pass
            
class Bookshelf(Furnishing):
            pass

class Bed(Furnishing):
            pass

class Table(Furnishing):
            pass

HOME = []

def map_the_home(home):
    pair = []
    for item in home:
        pair.append((item.room, item))
        mapped = defaultdict(list)
        for k, v in pair:
                mapped[k].append(v)
    return mapped

def counter(home):
    sofas, bookshelves, beds, tables, items = 0, 0, 0, 0, 0
    for obj in home:
        if isinstance(obj, Bed):
            beds = beds + 1
        if isinstance(obj, Sofa):
            sofas = sofas + 1
        if isinstance(obj, Bookshelf):
            bookshelves = bookshelves + 1
        if isinstance(obj, Table):
            tables = tables + 1
        items = items + 1 
    print("Beds: {0} Bookshelves: {1} Tables: {2} Sofas: {3}".format(beds, bookshelves, tables, sofas))
    counts = {'Beds':beds, 'Sofas':sofas, 'Tables':tables, 'Bookshelves':bookshelves, 'Items':items}
    return counts

if __name__ == "__main__":
    HOME.append(Bed('Bedroom_Master'))
    HOME.append(Table('Bedroom_Master'))
    HOME.append(Bookshelf('Bedroom_Master'))
    HOME.append(Table('Kitchen'))
    HOME.append(Sofa('Living Room')) 
    HOME.append(Bed('Bedroom_Blue')) 
    print(map_the_home(HOME))
    counter(HOME)
