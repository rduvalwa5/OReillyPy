"""                                  
control.py
Create queues
start output process
start worker processes
pushes inputs into the input queue using the output of a generator
"""                                 
from multiprocessing import Queue, JoinableQueue    
from output import OutThread                
from worker import WorkerProcess 
from alphaGenerator import alphaGen               

if __name__ == '__main__':
        WORKERS = 2                    
        
        inq = JoinableQueue(maxsize=int(WORKERS * 1.5))
        outq = Queue(maxsize=int(WORKERS * 1.5))                  
        
        ot = OutThread(WORKERS, outq, sorting=False)              
        ot.start()                              
        
        for i in range(WORKERS):                
            w = WorkerProcess(inq, outq)            
            w.start()                            
        instring = alphaGen(10)

        # feed the process pool with work units    
        for work in enumerate(instring):        
            inq.put(work)                        
        # terminate the process pool                
        for i in range(WORKERS):                
            inq.put(None)                        
        inq.join()    
        print("input is ", instring)                                    
        print("Control process terminating")    

