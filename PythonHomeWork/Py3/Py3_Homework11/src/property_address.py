'''
Your project should meet the following conditions:
 a. property_address.py must append messages such as the following to a logfile named property_address.log
 b. each time test_property_address.py is run:  
    property_address.log:
    -
    2011-12-05 19:36:14,970 - ERROR - state - STATE exception 
    2011-12-05 19:36:14,970 - INFO - __init__ - Creating a new address 
    2011-12-05 19:36:14,986 - ERROR - zip_code - ZIPCODE exception 
'''    

import re
import logging

LOG_FILENAME = "property_address.log"

# LOG_FORMAT = "%(asctime)s %(name)s:%(levelname)s:%(filename)s function:%(funcName)s line:%(lineno)d %(message)s"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"

DEFAULT_LOG_LEVEL = "error"  # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }
def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)  # add format to config


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
            logging.info('Creating a new address')

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
            logging.error('STATE exception')
            raise StateError        
        elif value in self.state_codes:
            self._state = value
        else:
            logging.error('STATE exception')
            raise StateError      
        
    @property
    def zip_code(self):
        return self._zip_code
  
    @zip_code.setter
    def zip_code(self, value):
        pat = re.compile('^[\d]{5,5}$')  # at least 5, but not more than 5 digits
        mat = pat.match(value) 
        if mat == None:
            logging.error('ZIPCODE exception')
            raise ZipCodeError
        elif mat.group() == value:
            self._zip_code = value                  
        else:
            logging.error('ZIPCODE exception')
            raise ZipCodeError


if __name__ == "__main__":
    start_logging(level="info") 
    home = Address(name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VA', zip_code='12345')
    print(home.__dict__)
    print(home.name , home.city)
    home.zip_code = 'asdfg'
