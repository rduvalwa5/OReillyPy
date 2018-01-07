"""
Pack and unpack test
"""
import random, os, struct
File = r"char.bin"
s1 = "Write a string of characters \n and \t unprintable characters to binaray?!"

# rlist = [random.random() for i in range(10)]
# print(rlist)
print(len(s1))
slist = list(s1)
f = open(File, "r")
f.write(s1)
# for ltr in s1:
#    print(type(ltr), ltr)
#    x = struct.pack("=s",ltr)
#    f.write(x)
f.close()
f = open(File, "rb")
x = f.read()
for ltr in x:
    print(chr(ltr))
    print(struct.unpack("=s", ltr))
f.close()

