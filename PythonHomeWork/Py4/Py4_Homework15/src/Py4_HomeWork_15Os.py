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
FILE_SIZE = 10000000
CHUNKS = 10
CHUNK_SIZE = int(FILE_SIZE / CHUNKS)
FILE_N = "10Mil_Os.txt"

" Create file of size "
with open(FILE_N, "wb") as f:
    for num in range(CHUNKS):
        f.write(b'*' * (CHUNK_SIZE))
    print("OS Write File done")
    f.close()
    
