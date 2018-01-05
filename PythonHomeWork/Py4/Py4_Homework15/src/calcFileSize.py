'''
Calculate a file size
'''
import struct

SLOTFMT = b"B99999s"
# SLOTFMT = b"B9999s"
print(SLOTFMT)
SLOTSIZE = struct.calcsize(SLOTFMT)
print(SLOTSIZE)
SLOTS = 100  # Number of subprocesses


def calcFile(SLOTS , SLOTSIZE):
        return SLOTS * SLOTSIZE

print(calcFile(SLOTS, SLOTSIZE))
