'''
arr as array instead of list
'''
'''
import array as sys_array

class array:
    def __init__(self,M,N):
        #"Create a list long enough to hold M*N elements"
        "Create an M-element list of N-element row lists."
        self._data = sys_array.array("i",[0] * M * N)
        self._rows = M
        self._cols = N
        
    def __getitem(self,key):
        "Returns the appropriate element for a two element subscription tuple."
        row, col= self._validate_key(key)
        print("_cols ", self._cols)
        print("col ", col)
        print(self._data[row*self._cols+col])
        return self._data[row*self._cols+col]
    
    def __setitem__(self,key,value):
        print("Set input: ", key, value)
        row, col = self.validate_key(key)
        self._data[row*self._cols+col] = value
        print("Data is: ", self.__getitem(key))
        
    def _validate_key(self,key):
        """Validates a key agains the array's shape and retruns good tuples Raise KeyError"""
        print("Validate key: ", key)
        row, col = key
        if (0 <= row < self.__rows and 0 <= col< self._cols):
            return key
        raise KeyError("Subscript out of range")
'''
"""
Class-based array allowing tuple subscripting
"""
import array as sys_array

class array:

    def __init__(self, M, N):
        "Create an M-element list of N-element row lists."
        self._data = sys_array.array("i", [0] * M * N)
        self._rows = M
        self._cols = N

    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        print("Row: ", row)
        print("_cols ", self._cols)
        print("col ", col)
        print("getItem Return: ", self._data[row * self._cols + col])
        return self._data[row * self._cols + col]
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        self._data[row * self._cols + col] = value
        print("Data is: ", self._data[row * self._cols + col])
    
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        row, col = key
        if (0 <= row < self._rows and
                0 <= col < self._cols):
            return key
        raise KeyError("Subscript out of range")

    
    
