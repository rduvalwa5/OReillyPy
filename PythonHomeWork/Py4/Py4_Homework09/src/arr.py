"""
Class-based single-list allowing tuple subscripting
"""

class array:

    def __init__(self, M, N):
        "Create an list long enough to hold M*N elements."
        self._data = [0] * M * N
        self._rows = M
        self._cols = N

    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        print("Get Item ", key)
        row, col = self._validate_key(key)
        print("Row: ", row)
        print("_cols ", self._cols)
        print("col ", col)
        print("getItem Return: ", self._data[row * self._cols + col])
        return self._data[row * self._cols + col]

    def __setitem__(self, key, value):
        print("SET Key ", key, "Value ", value)
        "Sets the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        self._data[row * self._cols + col] = value
    
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        print("Validate Key ", key)
        row, col = key
        if (0 <= row < self._rows and
                0 <= col < self._cols): 
            return key
        raise KeyError("Subscript out of range")

