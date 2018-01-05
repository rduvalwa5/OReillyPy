'''
Created on Mar 28, 2014
 This problem demonstrates the impact of changing the local directory with threading.
 Observations:
 1. The current threads local directory will be the same as the previous threads local directory provided the current thread is launched
    before a previous thread can change the local directory.
 2. The only factors determining what the local directory of a thread will be is when the previous thread changed the local directory.
    If a sleep is put in before the thread changes the local directory, this can be used to allow all thread to be launched before a 
    local directory is changed.  This results in all launched threads having the same local directory.
    By manipulating 
 3. The lesson to be aware of is the impact of one thread on another and how this cross interference can create an undesirable result.
 author: rd
'''
 
import os
import threading
import time

home = ""
startingDirectories = []

def compareDir(lst):
    pathSame = 0
    pathDifferent = 0
    currentPath = ""    
    for i in lst:
        thePath = i[1]
        if thePath == currentPath :
            pathSame += 1
        elif currentPath == "":
            currentPath = thePath
            pathSame += 1
        else:
            currentPath = thePath
            pathDifferent += 1
    return  pathSame , pathDifferent

def getCurrentDir():
    return  os.getcwd()

def changeDirectory(path):
    try:
        print("Start Directory ", getCurrentDir())
        os.chdir(path)
        for file in listFiles():
            print(file)
    except FileNotFoundError:
        print("FileNotFoundError")
#        changeDirectory(getCurrentDir())
    
def listFiles():
    yield os.listdir(".")
    
def run(i, name, path):
    "provide thread number and path of current local directory"
    startingDirectories.append((i, getCurrentDir()))
    print(i, " is Starting NOW!!!!")
    """A sleep here results in all threads launching before the local directory is changed.
       Without a sleep here there will be a mix of threads having the same and different local 
       directories
    """
    time.sleep(0) 
    changeDirectory(path)
               
if __name__ == "__main__":
    bgthreads = threading.active_count()
    threads = []
    paths = ["..", "../../", "/users/rduvalwa2", "/library" ]
    
    for i in range(len(paths)):
        t = threading.Thread(target=run, args=(i, "Thread-" + str(i), paths[i]))
        try:
            t.start()
        except RuntimeError:
            print("Exception RuntimeError")
        threads.append((i, t))
    for i, t in threads:
        t.join()
#        print("Thread", i , "done")
    print("All Threads Are Done")
    print(startingDirectories)
    diffs = compareDir(startingDirectories)
    print("Starting Paths the Same ", diffs[0])
    print("Starting Paths that Differ ", diffs[1])
