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

import struct
import mmap
import multiprocessing as multiProcess
import os
import time
import sys

FILENAME = "mappedfile"

SLOTFMT = "B9999999s"
SLOTS = 10  # Number of subprocesses

# SLOTFMT = "B99999s"
# SLOTS = 100 # Number of subprocesses

# SLOTFMT = "B9999999s"
# SLOTS = 1 # Number of subprocesses

SLOTSIZE = struct.calcsize(SLOTFMT)

EMPTY = 255
TERM = 254
FILESIZE = SLOTSIZE * SLOTS


def unpackslot(bytes):
#    """Return slot data as (slot#, string)."""
    return struct.unpack(SLOTFMT, bytes)

def packslot(slot, s):
    """Generate slot string from individual data elements."""
    s_bytes = s.encode(encoding='UTF-8', errors='strict')
#    decoded_s = s_bytes.decode(encoding='UTF-8',errors='strict')
    return struct.pack(SLOTFMT, slot, s_bytes)

def run(slot):
    """Implements the independent processes that will consume the data."""
    offset = SLOTSIZE * slot
    sys.stdout.flush()
    f = open(FILENAME, "r+b")
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    while True:
        while mapf[offset] == EMPTY:
            time.sleep(0.01)
        if mapf[offset] == TERM:
            sys.stdout.flush()
            mapf.close()
            return 
#        x, s = unpackslot(mapf[offset:offset+SLOTSIZE])
        s = unpackslot(mapf[offset:offset + SLOTSIZE])
        sys.stdout.flush()
        mapf[offset] = EMPTY

if __name__ == "__main__":
    f = open(FILENAME, "wb")
    f.write(FILESIZE * b'\0')
    f.close()
    f = open(FILENAME, "r+b")
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

    processTable = []
    for slot in range(SLOTS):
        offset = slot * SLOTSIZE
        mapf[offset] = EMPTY
        p = multiProcess.Process(target=run, args=(slot,))
        processTable.append(p)
        p.start()
 
    for i in range(4):
        for slot in range(SLOTS):
            offset = slot * SLOTSIZE
            mapf[offset + 1:offset + SLOTSIZE] = packslot(slot, SLOTSIZE * "*")[1:]
            mapf[offset] = slot
    
    for slot in range(SLOTS):
        offset = SLOTSIZE * slot
        mapf[offset] = TERM
    
    for p in processTable:
        p.join()

    mapf.close()
    byteCount = len(f.read())
    print("ByteCount ", byteCount)
#    print(f.read()) 
    print("SLOTFMT", SLOTFMT)
    sys.stdout.flush()
    f.close()
    os.unlink(FILENAME) 
