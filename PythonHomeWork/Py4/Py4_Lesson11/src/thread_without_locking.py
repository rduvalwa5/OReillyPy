"""
 thread.py: Without threading.Lock, threads sleep in parallel.
"""
import threading
import time
class MyThread(threading.Thread):
    def __init__(self, lock, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.lock = lock
    def run(self):
        for i in range(10):
            self.lock.acquire()
            time.sleep(0.1)
            self.lock.release()
        self.lock.acquire() 
        print(self.name, "finished")
        self.lock.release() 

lock = threading.Lock()
bgthreads = threading.active_count()
tt = [MyThread(lock) for i in range(6)]
for t in tt:
    print(t)
    t.start()
print("Threads started")
while threading.active_count() > bgthreads:
    time.sleep(2)
    print("tick")
print("All threads done")
