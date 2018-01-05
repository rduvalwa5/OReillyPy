'''
Created on Apr 13, 2014
@author: rduvalwa2
'''
import multiprocessing
import time
import sys

def run(i, name):
    """Sleep for a given number of seconds report and terminate"""
    time.sleep(i)
    print(name, "finished after", i, "seconds")
    sys.stdout.flush()
if __name__ == '__main__':
    for i in range(6):
        t = multiprocessing.Process(target=run, args=(i, "P" + str(i)))
        t.start()
    print("Process started")
