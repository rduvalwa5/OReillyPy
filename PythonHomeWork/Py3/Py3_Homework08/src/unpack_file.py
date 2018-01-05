"""
Pack and unpack test
"""
import random, os, struct
File = r"wireshark.bin"
data = []

data = open("wireshark.bin", "rb").read()  # let Python automatically close file
print(len(data))
header = data[:191]
start = 0
btes = 32 
for i in range(6):
    print(i)
    end = start + btes
    print(start, end)
    print(header[start:end])
    start = start + btes
    print(start, end)

packetheader = data[192:320]  # magic wireshark number (also reveals byte order)
print("packet header: ", packetheader) 
btes = 32  
start = 192 
for i in range(10):
    print(i)
    end = start + btes
    print(start, end)
    print(struct.unpack('', packetheader[start:end]))
    start = start + btes

#
# magic = struct.unpack('>L', data[0:4])[0]  # before the data = data[24:] line above
# print(magic)
