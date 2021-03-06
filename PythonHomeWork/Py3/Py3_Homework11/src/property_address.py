'''
Python 3 Lesson 12 Homework
'''    
import configparser
from optparse import OptionParser
import re
import logging

LOG_FILENAME = "" 
CONFIG_FILE = "/Users/rduvalwa2/DevTools/eclipse-indigo/workspace/Python3_Git/Py3_Git/Python3_Homework12/src/propertyaddress.cfg"
LOG_FORMAT = ""
USAGE = "Usage: property_address.py [options] \nproperty_address.py: error: options -n, -a, -c, -s, -z are required "

config = configparser.RawConfigParser()
config.read(CONFIG_FILE)
zip_rule = config.get('validators', 'zip_code')
state_rule = config.get('validators', 'state')

DEFAULT_LOG_LEVEL = "error"
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level.lower()], format=LOG_FORMAT) 
class ZipCodeError(AttributeError):
    pass    
      
class StateError(AttributeError):
    pass

class InvalidEmail(Exception):
    pass

class Address(object):
    def __init__(self, name, street_address, city, state, zip_code):
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
        pat = re.compile(state_rule)
        mat = pat.match(value)
        if mat == None:
            logging.error('STATE exception')
            raise StateError
        else:  
            self._state = value     
        
    @property
    def zip_code(self):
        return self._zip_code
  
    @zip_code.setter
    def zip_code(self, value):
        pat = re.compile(zip_rule)
        mat = pat.match(value) 
        if mat == None:
            logging.error('ZIPCODE exception')
            raise ZipCodeError
        elif mat.group() == value:
            self._zip_code = value                  
        else:
            logging.error('ZIPCODE exception')
            raise ZipCodeError

def main(options):
    "routes requests"
    Address(name=options.name, street_address=options.address, city=options.city, state=options.state, zip_code=options.zip_code)
    
if __name__ == '__main__':    
    LOG_FORMAT = config.get('log', 'format')
    LOG_FILENAME = config.get('log', 'output')
    parser = OptionParser(usage=USAGE)
    parser.add_option("-l", "--level",
                        action="store",
                        dest="level",
                        default="INFO",
                        help="Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL")

    parser.add_option('-n', '--name', '--action', dest="name", action="store", help="Sets the name value of the Address object")
    parser.add_option('-a', '--address', dest="address",
                            action="store", help="Sets the street_address value of the Address object")
    parser.add_option('-c', '--city', dest="city", action="store", help="Sets the city value of the Address object")  
    parser.add_option('-s', '--state', dest="state", action="store", help="Sets the state value of the Address object")
    parser.add_option('-z', '--zip', dest='zip_code', action='store', help="Sets the zip_code value of the Address object")
    (options, args) = parser.parse_args()
    
    start_logging(filename=LOG_FILENAME, level=(options.level).lower()) 

# validation
    if options.name is None:
        logging.error('Name exception: No name attribute')
        parser.error("require -n name")
        
    if options.address is None:
        logging.error('Address exception: No address attribute')
        parser.error("require -a address")
        
    if options.city is None:
        logging.error('City exception: No city attribute')
        parser.error("require -c city")
        
    if options.state is None:
        logging.error('State exception: No state attribute')
        parser.error("require -s state")
    else:
        pat = re.compile(state_rule)
        mat = pat.match(options.state) 
        if mat == None:
            logging.error('State exception: Rule Match')
            raise StateError        
                       
    if options.zip_code is None:
        logging.error('Zipcode exception: No zip code attribute')
        parser.error("require -z zipcode")
    else:
        pat = re.compile(zip_rule) 
        mat = pat.match(options.zip_code) 
        if mat == None:
            logging.error('ZIPCODE exception: Rule Match')
            if options.level == "WARNING":
                parser.error("usage: property_address.py [options]\nproperty_address.py: error: option -z requires a valid 5-digit US zip code ")
            raise ZipCodeError
        elif mat.group() == options.zip_code:
            pass                 
    main(options)
