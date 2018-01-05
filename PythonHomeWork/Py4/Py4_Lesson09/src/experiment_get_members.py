'''
Created on Mar 21, 2014
@author: 310122001
Experimenting with getmembers()"
'''

import inspect
from smtplib import SMTP
from pprint import pprint
pprint(inspect.getmembers(SMTP))
''' 
 [('__class__', <class 'type'>),
 ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>),
 ('__dict__', <dict_proxy object at 0x1006b7910>),
 ('__doc__',
  "This class manages a connection to an SMTP or ESMTP server.\n
    SMTP Objects:\n
        SMTP objects have the following attributes:\n
            helo_resp\n
                This is the message given by the server in response to the\n
                most recent HELO command.\n\n
            ehlo_resp\n
                This is the message given by the server in response to the\n
                most recent EHLO command. This is usually multiline.\n\n
            does_esmtp\n
                This is a True value _after you do an EHLO command_, if the\n
                server supports ESMTP.\n\n
            esmtp_features\n
                This is a dictionary, which, if the server supports ESMTP,\n
                will _after you do an EHLO command_, contain the names of the\n
                SMTP service extensions this server supports, and their\n
                parameters (if any).\n\n
                Note, all extension names are mapped to lower case in the\n
                dictionary.\n\n
        See each method's docstrings for details.  In general, there is a\n
        method of the same name to perform each SMTP command.  There is also a\n
        method called 'sendmail' that will do an entire mail transaction.\n        "),
 ('__eq__', <slot wrapper '__eq__' of 'object' objects>),
 ('__format__', <method '__format__' of 'object' objects>),
    ...
 ('__str__', <slot wrapper '__str__' of 'object' objects>),
 ('__subclasshook__',
  <built-in method __subclasshook__ of type object at 0x1b002aed0>),
 ('__weakref__', <attribute '__weakref__' of 'SMTP' objects>),
 ('_get_socket', <function _get_socket at 0x1007a3d98>),
 ('close', <function close at 0x116437958>),
    ... 
 ('verify', <function verify at 0x116437628>),
 ('vrfy', <function verify at 0x116437628>)]
''' 
pprint(inspect.getmembers(SMTP, inspect.ismethod))
''' 
 []
'''
pprint(inspect.getmembers(SMTP, inspect.isfunction))
'''
 [('__init__', <function __init__ at 0x1007a3c88>),
 ('_get_socket', <function _get_socket at 0x1007a3d98>),
 ('close', <function close at 0x116437958>),
    ...
 ('verify', <function verify at 0x116437628>),
 ('vrfy', <function verify at 0x116437628>)]
'''
smtp = SMTP()
pprint(inspect.getmembers(smtp, inspect.ismethod))
'''
 [('__init__',
  <bound method SMTP.__init__ of <smtplib.SMTP object at 0x100644c90>>),
 ('_get_socket',
  <bound method SMTP._get_socket of <smtplib.SMTP object at 0x100644c90>>),
 ('close', <bound method SMTP.close of <smtplib.SMTP object at 0x100644c90>>),
    ...
 ('verify',
  <bound method SMTP.verify of <smtplib.SMTP object at 0x100644c90>>),
 ('vrfy', <bound method SMTP.verify of <smtplib.SMTP object at 0x100644c90>>)]
 '''
