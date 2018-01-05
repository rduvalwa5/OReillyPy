'''
Created on Apr 27, 2014
https://docs.python.org/2.7/library/mmap.html
@author: rduvalwa2
'''
import mmap

 # Open a file in binary (b) mode for writing.
fp = open("mybinaryfile", "w")
# Write whatever data you like to it.
fp.write('No' * 1000000)
fp.close()
fp = open("mybinaryfile", "r")
print(len(fp.read()))
fp = open("mybinaryfile", "r")
print(fp.tell())
# print(fp.read())
