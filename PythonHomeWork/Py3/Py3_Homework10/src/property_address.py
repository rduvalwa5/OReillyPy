import re

class ZipCodeError(AttributeError):
    pass    
      
class StateError(AttributeError):
    pass

class Address(object):

    def __init__(self, name, street_address, city, state, zip_code):
            self.zipPattern = '\d\d\d\d\d'
            self.state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "AS", "GU", "MP", "PR", "VI", "FM", "MH", "PW", "AA", "AE", "AP", "CM", "CZ", "NB", "PI"]
            self._name = name 
            self._street_address = street_address
            self._city = city
            self._state = state.upper()
            self._zip_code = zip_code

    @property
    def name(self):
        return self._name
  
    @name.setter
    def name(self, value):
        raise AttributeError
        
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
  
    @state.setter
    def state(self, value):
        pat = re.compile('[A-Z]{2}')
        mat = pat.match(value)
        if mat == None:
            raise StateError        
        elif value in self.state_codes:
            self._state = value
        else:
            raise StateError      
        
    @property
    def zip_code(self):
        return self._zip_code
  
    @zip_code.setter
    def zip_code(self, value):
        pat = re.compile('^[\d]{5,5}$')  # at least 5, but not more than 5 digits
        mat = pat.match(value) 
        if mat == None:
            raise ZipCodeError
        elif mat.group() == value:
            self._zip_code = value                  
        else:
            raise ZipCodeError
