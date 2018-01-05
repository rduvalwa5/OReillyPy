'''
Created on Dec 13, 2013

@author: rduvalwa2
'''
"""
Naive implementation of list-of-lists creation.
"""
'''
def array(M, N):
    "Create an M-element list of N-element row lists."
    rows = []
    print("element: ", M, "element in row list: ", N)
    for _ in range(M):
'''
# Modify
#        cols = []
#        for _ in range(N):
#            cols.append(0)
#        rows.append(cols)
'''
        rows.append([0] * N)
    print("Rows ", rows)
    return rows
'''
"""
Convert function to Class
#Class-based list-of-lists allowing tuple subscripting
Class-based single-list allowing tuple subscripting
"""
class array:
# __init__ creates the list and binds it to an instance variable
    def __init__(self, M, N):
#        "Create an M-element list of N-element row lists."
        "Create a list long enough to hold M*N elements"
#        self._rows = []
#        for _ in range(M):
#            self._rows.append([0] * N)
        self._data = [0] * M * N 
        self._rows = M
        self._cols = N 
        
# instance variable that __getitem__() can access            
    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
#        row, col = key
#        return self._rows[row][col]
        row, col = self._validate_key(key)
        return self._data[row * self._cols + col]
   
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
#        row, col = key
#        self._rows[row][col] = value
        row, col = self._validate_key(key)
        self._data[row * self.cols + col] = value
        
    def _validate_key(self, key):
        """Validate a key against the array's shape, returning good tuples
          Raises KeyError on problem."""
        row, col = key
        if(0 <= row < self.rows and 0 <= col < self._cols):
            return key
        raise KeyError("Subscript out of rangs")
