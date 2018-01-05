
import configparser
from optparse import OptionParser
import re
import logging

LOG_FILENAME = "property_address.log"

#LOG_FORMAT = "%(asctime)s %(name)s:%(levelname)s:%(filename)s function:%(funcName)s line:%(lineno)d %(message)s"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"

DEFAULT_LOG_LEVEL = "error" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }
def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level],format=LOG_FORMAT) # add format to config


class ZipCodeError(AttributeError):
    pass    
      
class StateError(AttributeError):
    pass

class Address(object):

    def __init__(self, name, street_address, city, state, zip_code):
            self.zipPattern =  '\d\d\d\d\d'
            self.state_codes = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","AS","GU","MP","PR","VI","FM","MH","PW","AA","AE","AP","CM","CZ","NB","PI"]
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
    def name(self,value):
        raise AttributeError
        
    @property
    def street_address(self):
        return self._street_address
  
    @street_address.setter
    def street_address(self,value):
        self._street_address = value 
        
    @property
    def city(self):
        return self._city
  
    @city.setter
    def city(self,value):
        self._city = value 
        
    @property
    def state(self):
        return self._state
  
    @state.setter
    def state(self,value):
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
    def zip_code(self,value):
        pat = re.compile('^[\d]{5,5}$')  #at least 5, but not more than 5 digits
        mat = pat.match(value) 
        if mat == None:
            logging.error('ZIPCODE exception')
            raise ZipCodeError
        elif mat.group() == value:
            self._zip_code = value                  
        else:
            logging.error('ZIPCODE exception')
            raise ZipCodeError
'''
Modify property_address.py to accept the following options 
 if called directly, with the five address values used to instantiate an Address class if no parser errors are thrown.
 -
 option       default                        address?               task
 -l/--level    INFO                              yes       Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL 
 -n/--name     Throws a parser error if empty    yes       Sets the name value of the Address object 
 -a/--address  Throws a parser error if empty    yes       Sets the street_address value of the Address object 
 -c/--city     Throws a parser error if empty    yes       Sets the city value of the Address object 
 -s/--state    Throws a parser error if empty    yes       Sets the state value of the Address object 
 -z/--zip_code Throws a parser error if empty    yes       Sets the zip_code value of the Address object 
'''  
def main(options):
    "routes requests"
    if options.action == 'add':
        return email_add(options.email)
    elif options.action == 'delete':
        return email_delete(options.email)
    elif options.display == True:
        return email_display()
  
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-l', '--level', dest="action", action="store", help="Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL")
	parser.add_option('-n','--name',dest="action",
#    parser.add_option('-a', '--action', dest="action", action="store",help="requires -e option. Actions: add/delete")
#    parser.add_option('-e', '--email', dest="email", action="store", help="email used in the -a option")
#    parser.add_option('-d', '--display', dest="display",  type="int", action="store",help="show all emails limited by value")    
    (options, args) = parser.parse_args()
    # validation
#    if options.action and not options.email:
#        parser.error("option -a requires option -e")
#    elif options.email and not options.action:
#        parser.error("option -e requires option -a")
			