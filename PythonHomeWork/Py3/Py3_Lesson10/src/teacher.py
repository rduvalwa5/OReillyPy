'''
Created on Oct 16, 2013
decorator getter and setter property example
@author: rduvalwa2
'''
class Teacher(object):
    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}   

    def __init__(self, first_name, last_name, age, classes, grade):
            self._first_name = first_name  # internal data attributes are set 
            self._last_name = last_name
#            Self._age = age
            self.age = age
            self._classes = classes
            self._grade = grade
            print("Init Grade: ", self._grade)
    
    @property
    def first_name(self):
        return self._first_name.capitalize()

    @property
    def last_name(self):
        return self._last_name.capitalize()
   
#    def getage(self):
    @property
    def age(self):
        return self._age
   
#    def setage(self, value):
    @age.setter
    def age(self, value):
        self._age = int(value)
        print("age.setter: ", self._age)

#    age = property(getage, setage, doc="Teacher's age: must be convertible to integer")
       
    @property
    def classes(self):
        print("property classes: ", self._classes)
        return sorted(self._classes)

    @property
    def grade(self):
        print("property grade: ", self._grade)
        return self.grades[self._grade]
    
    @grade.setter
    def grade(self, value):
        self.grade[value]  # throw error if valie != a key
        self._grade = value
        print("geade setter: ", value)
        
    @grade.deleter
    def grade(self):
        self.age += 1
        del self._grade
        
    
'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
'''    
