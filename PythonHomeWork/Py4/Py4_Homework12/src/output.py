"""
  output.py
"""

identity = lambda x: x  # List Comprehension

import multiprocessing
import sys

class OutThread(multiprocessing.Process):
    def __init__(self, N, q, sorting=True, *args, **kw):
        """Initialize process and save queue reference"""
        print("Output Class Started")
        multiprocessing.Process.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
    def run(self):
        """Extracts items from the output queue and print untill all are done"""
        while self.workers:
            p = self.queue.get()
            print("Worker............ ", self.workers, "Queue element ", p)
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)
        print("Pre out", self.output)
        print("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output)))
        print("Size", len("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output))))
        print("Output process terminating")
        sys.stdout.flush()
