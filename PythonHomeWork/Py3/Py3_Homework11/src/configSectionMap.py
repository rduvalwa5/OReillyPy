'''
Created on Nov 23, 2013

@author: rduvalwa2
'''
import configparser

Config = configparser.RawConfigParser()
Config.read('propertyaddress.cfg')
print(Config.sections())

val = Config.get('validators', 'zip_code')

print(val)
