'''
Created on May 27, 2013
cmdline.py
Simple program to dump command line arguments
@author: rduval
'''
import sys
for n, arg in enumerate(sys.argv):
    print(n, ":", arg)
    
