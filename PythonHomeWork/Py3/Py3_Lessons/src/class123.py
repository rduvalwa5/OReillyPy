"""
A simple iterator object specification.
"""
class gen123:
    def __init__(self, lst):
        "Initialize the iterator object."
        self.lst = lst
        self.itemno = 0
        self.count = 1
    def __iter__(self):
        "This object is not an iterable."
        return self
    def __next__(self):
        "Return the next value in the output sequence."
 
        if self.count > self.itemno:
#            print("Count is " + str(self.count)  + " " + "Item num is " + str(self.itemno))
            try:
                self.val = self.lst[self.itemno]
            except IndexError:
                print("List length is " + str(len(self.lst)))
                print("StopIteration")
                raise StopIteration
                print(StopIteration)
            self.itemno += 1
            self.count = 1
        self.count += 1
        return self.val
if __name__ == "__main__":
    m = ["a","A","b","B","c","C"]
    print(list(gen123(m)))
    for letter in gen123(m):
        print(letter)
#        print("")