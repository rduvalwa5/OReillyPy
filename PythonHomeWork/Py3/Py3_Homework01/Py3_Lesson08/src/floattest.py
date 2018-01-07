"""
 floattest.py: checks for inaccuracies in floating-point test representations.
 """
import random, os
rlist = [random.random() for i in range(10)]
filename = r"floatdata.txt"
f = open(filename, "w")
for x in rlist:
    print(x, file=f)
f.close()
f = open(filename)
for i in range(10):
    x = float(f.readline())
    if x != rlist[i]:
        print(i, x, rlist[i], abs(x - rlist[i]))
    else:
        print(i, x, rlist[i], abs(x - rlist[i]))
        print(i, x, "values agree")
print(filename, os.stat(filename).st_size)
f.close()
