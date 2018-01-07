'''
Created on Oct 16, 2013
decorator getter and setter property example
@author: rduvalwa2
'''
class Creature(object):

    sizes = {1: "small", 2: "medium", 3: "big"} 

    def __init__(self, creature, size, color, legs):
            self._creature = creature  # internal data attributes are set 
            self._size = size
            self._color = color
            self._legs = legs
            print("Orig: ", self._creature, "Size: ", self._size, "Color: ", self._color)
    
    @property
    def creature(self):
        return self._creature.capitalize()
  
#    def setage(self, value):
    @creature.setter
    def creature(self, value):
        self._creature = value 
       
    @property  # this is the getter
    def size(self):
        return self.sizes[self._size]
        
    @size.setter  # the setter incorporates the getter
    def size(self, value):
        print("Setter: ", value)
        try:        
            self.size[value]  # throw error if valie != a key
        except IndexError:
            raise IndexError
        self._size = value

    @property
    def legs(self):
        return self._legs()
    
    @legs.setter
    def legs(self, value):
        print("Attribute legs is read only!")
#        raise AttributeError

    
        

#    @property
#    def color(self):
#        return self._color
        
#    def color(self):
#        return self._color
#    <bound method Creature.color of <__main__.Creature object at 0x10059afd0>>



if __name__ == "__main__":
    spid = Creature("beetle", 1, "red", 6)
    print("spid.creature getter: ", spid.creature)
    spid.creature = "spider"
    print("Creature is now: ", spid.creature)
    print("Size getter ", spid.size)
    spid.size = 3
    print("Size now ", spid.size)
    print("spid._color no getter: ", spid._color)
#    print("spid.color throws error <bound method Creature.color of <__main__.Creature object at 0x10059afd0>>")
#    spid._color = "blue"
#    print("Color now :",spid._color)    
    spid.color = "brown"
    print("Color was set to brown: ", spid.color)    
    spid.legs = 8
    print("dict is :", spid.__dict__)
    



'''        
     E:\Python\Lesson_10>python
     Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
     Type "help", "copyright", "credits" or "license" for more information.
     >>> from creature import *
     >>> spid = Creature("beetle",1,"red")
     Orig:  beetle Size:  1 Color:  red
     >>> spid.size
     'small'
     >>> spid._color
     'red'
     >>> spid.color
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     AttributeError: 'Creature' object has no attribute 'color'
     >>> spid.size = 6
     Setter:  6
     Traceback (most recent call last):
       File ".\creature.py", line 33, in size
         self.size[value] # throw error if valie != a key
     IndexError: string index out of range
     #
     During handling of the above exception, another exception occurred:
     #
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       File ".\creature.py", line 35, in size
         raise IndexError
     IndexError
     >>> spid.size = 2
     Setter:  2
     >>> spid.size
     'medium'
     >>> spid.size = 3
     Setter:  3
     >>> spid.size
     'big'
     >>> spid.creater
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     AttributeError: 'Creature' object has no attribute 'creater'
     >>> spid.creature
     'Beetle'
     >>> spid.creature = "dog"
     >>> spid.creature
     'Dog'
     >>>
     ===========================
     E:\Python\Lesson_10>python
     Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
     Type "help", "copyright", "credits" or "license" for more information.
     >>> from creature import *
     >>> spid.creature
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     NameError: name 'spid' is not defined
     >>> spid = Creature("beetle",1,"red")
     Orig:  beetle Size:  1 Color:  red
     >>> spid.color = "black"
     >>> spid.color
     'black'
     >>> spid.color
     'black'
     >>> spid._color
     'red'
     >>> spid._dict_
     Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
     AttributeError: 'Creature' object has no attribute '_dict_'
     >>> spid.__dict__
     {'_size': 1, '_color': 'red', '_creature': 'beetle', 'color': 'black'}
     >>> spid._color = "brown"
     >>> spid.__dict__
     {'_size': 1, '_color': 'brown', '_creature': 'beetle', 'color': 'black'}
     >>>
'''
