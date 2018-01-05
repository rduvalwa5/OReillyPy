'''
Instructions:
Modify the logic of the Tree object to :
a) Allow data to be stored as an additional attribute of each node 
  (the data should be passed as an additional argument to __init__()).
b) provide a find() method that locates a key (whose value is passed to find() as an argument)
   and returns the data associated with the node; if the key is not present in the tree, the
   method should raise a KeyError exception.
'''

class Tree:
    def __init__(self, key, data=""):
        " Create a new Tree object with empty L and R subtrees."
        self.key = key
        self.data = data
        self.left = self.right = None
    def insert(self, key, data):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value")
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in  self.left.walk():
#                print("Left ",n)
                yield n[0], n[1]
        yield self.key, self.data
        if self.right:
            for n in self.right.walk():
#                print("Right ",n)
                yield n[0], n[1]

    def find(self, key):
#        print("Key is ", key)
        found = False
#        print("Search right")
        for n in self.right.walk():
#            print("n is ", n)
#            print("Type",type(n))
            if n[0] == key:
                found = True
                return n[1]
        if found == False:
#            print("Search left")
            for n in self.left.walk():
#                print("n is ", n)
                if n[0] == key:
                        found = True
                        return n[1]
        if found == False:
            if key == self.key:
                return self.data 
        if found == False:
                raise KeyError("Key is not present")       
                    
if __name__ == '__main__':
    t = Tree("D", "Data_" + "D")
    for c in "BJYQKFAC":
        t.insert(c, "Data_" + c)
    print(list(t.walk()))
    for item in "DBJYQKFAC":
        print(t.find(item))
    lst = ['a', 'b', 'c', 'd', 'e']
    print(lst[3:6])
                    
            
        
