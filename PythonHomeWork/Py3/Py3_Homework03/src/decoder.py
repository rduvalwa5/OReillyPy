'''
Think of an iterator as a generator(fire hose of data)
It streams the data to the output and does not return a list
but rather an iterable stream of characters
'''

class alphabator:
    def __init__(self, l):
        self.lst = l
        self.items = len(self.lst)
        self.count = -1
    def __iter__(self):
        return self
    def __next__(self):
            try:
                self.count += 1
                self.val = self.lst[self.count]
                if isinstance(self.val, int) and self.val in range(1, 27):
                        self.val = chr(96 + self.val).upper()
            except IndexError:
                    print(StopIteration)
                    raise StopIteration
            return self.val
            
        

if __name__ == "__main__":
    m = [1, '2', 'A', 'b', 26, 19, 100, 1000001, 27]
    print(alphabator(m))
    print("alphabator is " + str(list(alphabator(m))))
