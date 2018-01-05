"""
  worker.py
  worker process receives input
  pushes result to output
"""
                 
from multiprocessing import Process
import sys
    
class WorkerProcess(Process):
    def __init__(self, iq, oq, *args, **kw):
        """Initialize process and save Queue references."""
        Process.__init__(self, *args, **kw)        
        self.iq, self.oq = iq, oq                
    def run(self):                            
        while True:                              
            work = self.iq.get() 
            print(self.name, " working on ", work)               
            if work is None:                    
                self.oq.put(None)                    
                print("Worker", self.name, "done")    
                self.iq.task_done()                    
                break                                
            i, c = work                            
            result = (i, self.process(c))  # this is the "work"
            self.oq.put(result)                              
            self.iq.task_done()    
        sys.stdout.flush()                          
    def process(self, s):
        """This defines how the string is processed to produce a result."""      
        return s.upper()

