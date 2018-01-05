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
import sys
import os
import timeit
import time   

class Homework15:
        
    def firstTechnique(self, FileSize, Chunks, FileName):
        start = time.clock()
        self.fileName = FileName        
        self.fileSize = FileSize
        self.chunks = Chunks
        self.chunkSize = int(self.fileSize / self.chunks)
        self.fmt = self.getFormat()

        with open(self.fileName, "wb") as f:
            f.write(b'\0' * self.fileSize)  # have to define size of file
            f.close()
    
        with open(self.fileName, "r+b") as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        offset = 0
        chunkLabel = 0 
        for c in range(self.chunks):
                mm[offset:self.chunkSize + offset ] = self.packChunk(chunkLabel, b'*' * self.chunkSize)[1:]
                offset = offset + self.chunkSize
                chunkLabel += 1
                if chunkLabel == 255:
                    chunkLabel = 0
        "Prove mmap was written to"
#        mm.tell()
#        mm.seek(self.fileSize - int (self.fileSize/10))
#        print("Print last 1/10 characters", mm.read())
#        mm.seek(0)
#        fileLength = len(mm.read(self.fileSize))
#        print("End of write, File length ", fileLength, "Chunks ", self.chunks, "Chunk Size ", self.chunkSize)
        sys.stdout.flush()
        mm.close()
        os.unlink(self.fileName)
        end = time.clock()        
        return end - start / 1000

    def secondTechnique(self, FileSize, Chunks, FileName):
        start = time.clock()
        self.fileSize = FileSize
        self.chunks = Chunks
        self.fileName = FileName
        self.chunkSize = int(self.fileSize / self.chunks)

        with open(self.fileName, "wb") as f:
                f.write(b'')
                f.close()

        with open(self.fileName, "r+b") as f:
            try:
                mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            except ValueError:
 #               print("ValueError: cannot mmap an empty file")
                f.close()
                with open(self.fileName, "w+b") as f:
                    self.fmt = self.getFormat()
                    f.write(self.packChunk(0, b'\)' * self.chunkSize)[1:])
                    f.close()
                    with open(self.fileName, "r+b") as f:
                        chunkLabel = 0
                        for i in range(self.chunks):
                            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
                            if mm.size() < self.chunkSize:
                                mm.resize(mm.size() + self.chunkSize)
                                mm.write(self.packChunk(chunkLabel, b'*' * self.chunkSize)[1:])
                                chunkLabel += 1
                            else:
                                mm.write(self.packChunk(chunkLabel, b'*' * self.chunkSize)[1:])
                                if chunkLabel == 255:
                                    chunkLabel = 0
                    sys.stdout.flush()
                    mm.close()
        end = time.clock()        
        return end - start / 1000
        
    def packChunk(self, c, s):
        """Generate slot string from individual data elements."""
        return struct.pack(self.fmt, c, s)


    def getFormat(self):
#        self.chunkSize = chunkSize
        if self.chunkSize == 1:  # 10000000 chunks
                    return b"B1s"
        if self.chunkSize == 10:  # 1000000 chunks
                    return b"B10s"
        elif self.chunkSize == 104:  # 100000 chunks
                    return b"B104s"
        elif self.chunkSize == 1048:  # 10000 chunks
                    return b"B1048s"
        elif self.chunkSize == 10485:  # 10000 chunks
                    return b"B10485s"
        elif self.chunkSize == 20971:  
                    return b"B20971s"
        elif self.chunkSize == 52428:  
                    return b"B52428s"
        elif self.chunkSize == 104857:  # 100 hunks
                    return b"B104857s"
        elif self.chunkSize == 1048576:  # 10 chunks
                    return b"B1048576s"
        elif self.chunkSize == 10485760:
                    return b"B10485760s"
        else:
            sys.exit("Chunk Size not covered Exit")
        
if __name__ == "__main__":
    import timeit
    debug = False
    timeResults = []
    if debug == False:        
        chunks = [1, 10, 100, 1000, 10000 , 100000, 1000000, 10000000]  # ,100000000]
        file_size = 1024 * 1024 * 10
        fileNameX = "meth1.txt"
        fileNameY = "emptyFile.txt"
        for chunk in chunks:
            x = Homework15
            y = Homework15
            timeResults.append(("1st", chunk, x().firstTechnique(file_size, chunk, fileNameX)))
            timeResults.append(("2nd", chunk, y().secondTechnique(file_size, chunk, fileNameY)))
    for result in timeResults:
        print(result)


    if debug == True:
        fileNameX = "meth1.txt"
        fileNameY = "emptyFile.txt"
        chunk = 100
        file_size = 1024 * 1024 * 10    
        x = Homework15
        print(x().firstTechnique(file_size, chunk, fileNameX))
#        x = Homework15.firstTechnique(file_size,chunk,fileNameX)
#        x.firstTechnique(file_size,chunk,fileNameX)
#        y = Homework15().secondTechnique(file_size,chunk,fileNameY)
#        print("Technique_1 ",timeit("x().firstTechnique(file_size,chunk,fileNameX)","from __main__ import x,files_size,chunk,fileNameX"))
#        print("Technique_2 ",timeit("y","from __main__ import y"))


'''
Timeit did not work very well, it obviously was not timing correctly
('1st', 1, 0.126701843)
('2nd', 1, 0.22505519599999999)
('1st', 10, 0.26942779099999997)
('2nd', 10, 0.300107321)
('1st', 100, 0.336407595)
('2nd', 100, 0.353348258)
('1st', 1000, 0.390697299)
('2nd', 1000, 0.43394591699999996)
('1st', 10000, 0.492036647)
('2nd', 10000, 0.76424048)
('1st', 100000, 0.954846251)
('2nd', 100000, 3.472563362)
('1st', 1000000, 4.9907244649999996)
('2nd', 1000000, 29.650599777)
('1st', 10000000, 43.76100739)
('2nd', 10000000, 291.175604313)
'''


