'''
Created on Aug 8, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
def ret_lower(mystring):
    message="This is now lowercase:"
#      return "message"
    return message, mystring.lower()
s = input('Enter upper case: ')
#print(s)
print(ret_lower(s))