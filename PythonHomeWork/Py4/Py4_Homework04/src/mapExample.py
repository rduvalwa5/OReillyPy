'''
Created on Jan 19, 2014

@author: rduvalwa2
'''

class mapEx:
    def init(self, mapp={'A':1, 'B':2}):
        self.inA = {}
        
    def upDate(self, key, value):
        self.inA.update({key:value})
      
    def removeKey(self, key):
        del self.inA[key]
           
    def printInit(self):
        for key, item  in self.inA.items():
            print(key, " : ", item)
               
if __name__ == '__main__': 
    myMap = {'Aa':100, 'Bb':200, 'Cc':300}
    for key, item  in myMap.items():
        print(key, " : ", item)
    print(myMap)
    aMap = mapEx(myMap)
#    a(myMap)
    aMap.printInit()

        
'''
>>> inA = {'Aa':100,'Bb':200,'Cc':300}
>>> for key in inA:
...      print(inA[key])
... 
100
200
300
>>> for key in inA:
...      print(key , inA[key])
... 
Aa 100
Bb 200
Cc 300
>>> for key in inA:
...      print(key , inA[key])
... 
Dd 400
Aa 100
Bb 200
Cc 300
D d
>>> inA.update({'Dd':400})
>>> for key in inA:
...      print(key , inA[key])
... 
Dd 400
Cc 300
Bb 200
D d
Aa 100
>>> inA.update({'Dd':450})
>>> for key in inA:
...      print(key , inA[key])
... 
Dd 450
Cc 300
Bb 200
D d
Aa 100
>>> for key, item in inA.items():
...    print(key, ":" , item)
... 
Dd : 450
Cc : 300
Bb : 200
D : d
Aa : 100
>>> del inA['D']
>>> for key, item in inA.items():
...    print(key, ":" , item)
... 
Dd : 450
Cc : 300
Bb : 200
Aa : 100
>>> inA.update({'Ee':540})
>>> for key, item in inA.items():
...    print(key, ":" , item)
... 
Dd : 450
Cc : 300
Bb : 200
Aa : 100
Ee : 540
>>> 
'''
