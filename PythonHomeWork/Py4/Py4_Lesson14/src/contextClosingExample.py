'''
Created on Apr 22, 2014
https://docs.python.org/3/library/contextlib.html
@author: rduval
'''

from contextlib import contextmanager
# from contextlib import suppress
from urllib.error import URLError 



@contextmanager
def closing(thing):
    print("This is ", thing)
    try:
        print("TRY CLOSING THING")
        yield thing
    finally:
        print("FINALLY CLOSING THING")
        thing.close()
        
         
# from contextlib import closing
from urllib.request import urlopen


with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

        
with closing(urlopen('https://pygon.org')) as page:
    for line in page:
        print(line)


# with suppress(URLError):  #urllib.error.URLError: <urlopen error>
#    page = urlopen('https://pygon.org')
#    for line in page:
#        print(line)

        
