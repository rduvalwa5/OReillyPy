'''
https://docs.python.org/2.7/library/mmap.html
Created on Apr 26, 2014
@author: rduvalwa2
Here are your instructions:
Write a program that creates a: 
1. ten megabyte data file in:
2. two different ways
3. time each method
The first technique should
   - create a memory-mapped file and write the data by setting one chunk at a time 
   - using successively higher indexes 
The second technique should 
   - create an empty binary file 
   - and repeatedly use the write() method to write a chunk of data 
Show how the timings vary with the size of the chunk.
'''
import mmap
import sys
import os

FILE_SIZE = 100000
CHUNKS = 10
CHUNK_SIZE = int(FILE_SIZE / CHUNKS)
FILE_N = "10Mil.txt"

" Create file of size "
with open(FILE_N, "wb") as f:
    f.write(b'\0' * FILE_SIZE)  # have to define size of file
    f.close()
    
with open("10Mil.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    for num in range(CHUNKS):
        print("Start Position", mm.tell())
        mm.write(b'*' * (CHUNK_SIZE))
        print("End Write", mm.tell())
    mm.seek(0)
    print(len(mm.read()))
    sys.stdout.flush()
    mm.close()
    os.unlink(FILE_N) 
