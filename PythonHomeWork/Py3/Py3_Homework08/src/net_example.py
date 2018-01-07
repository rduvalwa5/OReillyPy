# Python read wireshark dump file for packet times
import random, os, struct
#
# 0xa1b23c4d (identical) 
# 0x4d3cb2a1 (swapped).

data = open("wireshark.bin", "rb").read()  # let Python automatically close file
magic1 = open("wireshark.bin", "rb").read(4)
print(type(magic1))
for a in magic1:
#    print(struct.unpack('>L',a))
    print(a)
print("magic1", magic1 , struct.unpack('>L', magic1)[0])

print(magic1[0], magic1[1], magic1[2], magic1[3])
print(struct.unpack('>L', magic1[0:4])[0])
magic = data[:4]  # magic wireshark number (also reveals byte order)
gmt_correction = data[8:12]  # GMT offset
data = data[24:]  # actual packets

magic = struct.unpack('>L', data[0:4])[0]

print("0xa1b2c3d4", 0xa1b2c3d4)
print("0xd4c3b2a1", 0xd4c3b2a1)
print("magic1 " , magic)
print("magic2 " , struct.unpack('>L', data[0:4])[0])
print("magic3 " , magic, 0xa1b2c3d4)
print("magic4 " , magic, 0xd4c3b2a1)

print('all', struct.unpack('>L', magic1[0:4])[0], 0xd4c3b2a1 , struct.unpack('>L', data[0:4])[0])
"""
all 3569595041 3569595041 555692100
NotWireSharkFile
1144004385
285325
66
66
555692100
-1923480576
1107296256
1107296256
"""
    
magic = struct.unpack('!L', data[0:4])[0]  # before the data = data[24:] line above
if magic == 0xa1b2c3d4:
    order = '>'
elif magic == 0xd4c3b2a1:
    order = '<'
else:
    print("NotWireSharkFile")
    
field0, field1, field2, field3 = struct.unpack('%sllll' % '<', data[:16])
print(field0)
print(field1)
print(field2)
print(field3)
# payload = data[16 : 16 + field?]
# data = data[16 + field?]

"""
1144004385
285325
66
66
"""

field0, field1, field2, field3 = struct.unpack('%sllll' % '>', data[:16])
print(field0)
print(field1)
print(field2)
print(field3)

"""
555692100
-1923480576
1107296256
1107296256
"""
