'''
Created on May 12, 2014
@author: rduvalwa2
'''
import Py4_HomeWork15_B, Py4_HomeWork_15Os
from timeit import timeit


def timeControl():        
        Py4_HomeWork15_B

def timeControlChunk1MB():
    Py4_HomeWork15_B.CHUNKS = 10
    Py4_HomeWork15_B.CHUNK_SIZE = Py4_HomeWork15_B.FILE_SIZE / Py4_HomeWork15_B.CHUNKS
    Py4_HomeWork15_B
    
def timeControlChunk500KB():
    Py4_HomeWork15_B.CHUNKS = 20
    Py4_HomeWork15_B.CHUNK_SIZE = Py4_HomeWork15_B.FILE_SIZE / Py4_HomeWork15_B.CHUNKS
    Py4_HomeWork15_B

def timeControlChunk100KB():
    Py4_HomeWork15_B.CHUNKS = 100
    Py4_HomeWork15_B.CHUNK_SIZE = Py4_HomeWork15_B.FILE_SIZE / Py4_HomeWork15_B.CHUNKS
    Py4_HomeWork15_B

def timeControlChunk20KB():
    Py4_HomeWork15_B.CHUNKS = 500
    Py4_HomeWork15_B.CHUNK_SIZE = Py4_HomeWork15_B.FILE_SIZE / Py4_HomeWork15_B.CHUNKS
    Py4_HomeWork15_B

def timeControlChunk10MB():
    Py4_HomeWork15_B.CHUNKS = 1
    Py4_HomeWork15_B.CHUNK_SIZE = Py4_HomeWork15_B.FILE_SIZE / Py4_HomeWork15_B.CHUNKS
    Py4_HomeWork15_B

def timeControlChunk1B():
    Py4_HomeWork15_B.CHUNKS = 10000000
    Py4_HomeWork15_B.CHUNK_SIZE = Py4_HomeWork15_B.FILE_SIZE / Py4_HomeWork15_B.CHUNKS
    Py4_HomeWork15_B
    
def timeControlChunk1B_OS():
    Py4_HomeWork_15Os.CHUNKS = 10000000
    Py4_HomeWork_15Os.CHUNK_SIZE = Py4_HomeWork_15Os.FILE_SIZE / Py4_HomeWork_15Os.CHUNKS
    Py4_HomeWork_15Os



print("timeControl", timeit("timeControl()", "from __main__ import timeControl"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk1MB", timeit("timeControlChunk1MB()", "from __main__ import timeControlChunk1MB"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk500KB", timeit("timeControlChunk500KB()", "from __main__ import timeControlChunk500KB"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk100KB", timeit("timeControlChunk100KB()", "from __main__ import timeControlChunk100KB"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk20KB", timeit("timeControlChunk20KB()", "from __main__ import timeControlChunk20KB"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk10MB", timeit("timeControlChunk10MB()", "from __main__ import timeControlChunk10MB"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk1B", timeit("timeControlChunk1B()", "from __main__ import timeControlChunk1B"))
print("Chunks:", Py4_HomeWork15_B.CHUNKS)
print("Chunk Size:", Py4_HomeWork15_B.CHUNK_SIZE)

print("timeControlChunk1B_OS", timeit("timeControlChunk1B_OS()", "from __main__ import timeControlChunk1B_OS"))
print("Chunks:", Py4_HomeWork_15Os.CHUNKS)
print("Chunk Size:", Py4_HomeWork_15Os.CHUNK_SIZE)
