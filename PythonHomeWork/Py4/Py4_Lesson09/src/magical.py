'''
 Created on Mar 21, 2014
'''
import sys
print(__name__)
module = sys.modules[__name__]
try:
    print(a)
except NameError:
    print("NameError")
setattr(module, "a", 42)
try:
    print(a)
except NameError:
    print("NameERror")

