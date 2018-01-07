"""
floattest.py: check for inaccuracies in floating-point test representations.
"""
import random, os, struct
filename = r"floatdata.bin"
rlist = [random.random() for i in range(10)]
print(rlist)
f = open(filename, "wb")
f.write(struct.pack("=10d", *rlist))
# for x in rlist:
#    print(x, file=f)
f.close()
f = open(filename, "rb")
for i in range(10):
    s = f.read(8)
#    x = float(f.readline())
    x, = struct.unpack("=d", s)
    if x != rlist[i]:
        print(i, x, rlist[i], abs(x - rlist[i]))
    else:
        print(i, x, "values agree")
print(filename, os.stat(filename).st_size)
f.close()

