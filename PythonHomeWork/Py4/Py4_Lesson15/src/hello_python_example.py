'''
Created on Apr 23, 2014

@author: rduvalwa2
'''
with open("hello.txt", "wb") as f:
    print(f.write(b"Hello Python!\n"))
# 14
import mmap
with open("hello.txt", "r+b") as f:
    mapf = mmap.mmap(f.fileno(), 0)
    print("Map tell after open", mapf.tell())
    print(mapf.readline())  # print b"Hello Python!\n"
    print("Map tell after mapf.readline()", mapf.tell())
    print(mapf[:5])  # prints b"Hello"
    print("Map tell after map index mapf[:5]", mapf.tell())
    mapf[6:] = b" world!\n"
    print(mapf.seek(0))
    print(mapf.readline()) 
    mapf.close()

# b'Hello Python!\n'
# b'Hello'
# 14
# b'Hello  world!\n' 
