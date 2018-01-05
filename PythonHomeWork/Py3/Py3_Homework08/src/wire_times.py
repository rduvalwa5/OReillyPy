'''
From web site information
http://stackoverflow.com/questions/10281002/read-wireshark-dump-file-for-packet-times
 0xa1b23c4d (identical) 
 0x4d3cb2a1 (swapped).
'''
import struct
numberOfPackets = 1
accumLength = 0

data = open("wireshark.bin", "rb").read()  # let Python automatically close file
print("Data Length ", len(data))
expectBytes = len(data)
# print(data[0:24])

# data2 = data[24:]
# print(struct.unpack('!LLLL',data2[:16]))
"""
Get magic number to determine the order identical(Big-endian)
or swapped(Little-endian)
"""
magic = struct.unpack('!L', data[0:4])[0]
if magic == 0xa1b2c3d4:
    order = '>'
    print("identical ", order)
elif magic == 0xd4c3b2a1:
    order = '<'
    print("swapped ", order)
else:
    print("NotWireSharkFile")

data = data[24:]    
accumLength = accumLength + 24
"""
try:
    field0, field1, field2, field3 = struct.unpack('%sllll' % order, data[:16])
    print("Packet Number: ", numberOfPackets)                 # actual packets
    numberOfPackets = numberOfPackets + 1
#field0, field1, field2, field3 = struct.unpack('>llll', data[:16])
    print("timestamp seconds", field0)
    print("timestamp microseconds", field1)
#print("number of octets of packet saved in file" ,field2)
    print("actual length of packet" , field3)
except struct.error:
        print("No packets") 
"""
"""
field0a, field1a, field2a, field3a = struct.unpack('<llll', data[:16])
print("a timestamp seconds", field0a)
print("a timestamp microseconds", field1a)
print("a number of octets of packet saved in file" ,field2a)
print("a actual length of packet" , field3a)
"""
print("Length: ", len(data))
while len(data) > 0:
    try:
        field0, field1, field2, field3 = struct.unpack('%sllll' % order, data[:16])
        print("Packet Number: ", numberOfPackets, ",timestamp seconds,", field0, ",timestamp microseconds,", field1, ",actual length of packet,", field3)
#        print("timestamp seconds", field0)
#        print("timestamp microseconds", field1)
#        print("number of octets of packet saved in file" ,field2)
#        print("actual length of packet" , field3)
#        print("Length: ", len(data))
        numberOfPackets = numberOfPackets + 1
        accumLength = accumLength + field3
#        print("Packet Number: ", numberOfPackets)
        data = data[16 + field3:]    

    except struct.error:
        print(len(data))
        print(data)
        print("End of data: ", len(data))
print("End of Data")
print("The number of packets: ", numberOfPackets)
print("Accumalated bytes: ", accumLength, "Expected Bytes: ", expectBytes)
