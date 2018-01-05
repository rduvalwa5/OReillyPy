'''
Created on Oct 24, 2013
After Maveraick install
@author: rduvalwa2
'''

class StateError(AttributeError):
            print("Not a state.")

class Address(object):
    def __init__(self, name, street_address, city, state, zip_code):
            self._state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "AS", "GU", "MP", "PR", "VI", "FM", "MH", "PW", "AA", "AE", "AP", "CM", "CZ", "NB", "PI"]
            self._name = name 
            self._street_address = street_address
            self._city = city
            self._state = state
            self._zip_code = zip_code
            print(self.__dict__)


    @property
    def state_codes(self):
        return self._state_codes

    @property
    def name(self):
        return self._name
  
    @name.setter
    def name(self, value):
        print(value, "........", self._name)
        if value == "Daniel Greenfeld":
            print("Raise AttributeError")
            raise AttributeError
        else:
            self._name = value 
        
    @property
    def street_address(self):
        return self._street_address
  
    @street_address.setter
    def street_address(self, value):
        self._street_address = value 
        
    @property
    def city(self):
        return self._city
  
    @city.setter
    def city(self, value):
        self._city = value 
        
    @property
    def state(self):
        return self._state

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = int(value)
  
    @state.setter
    def state(self, value):
            if value.isupper():
                if value in self.state_codes:
                            self._state = value
            else:  
                    raise StateError
                
    @property
    def zip_code(self):
        return self._zip_code
  
    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value 
