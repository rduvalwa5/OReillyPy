'''
Created on Apr 18, 2014

@author: rduvalwa2
'''
class sstr(str):
    def __init__(self, inString):
        self.myString = inString
        self.inArray = list(self.myString)
        self.outArray = []
    def __lshift__(self, num):
        if num <= 0 | num == len(self.inArray): 
            self.myString = ''.join(self.inArray) 
            return self
        
        elif num == len(self.inArray):
            self.myString = [a for i in range(len(self.inArray))]
            return self

        elif num > len(self.inArray):
            pass
#            raise  Exception("Error " + str(num) + " greater that string length " + str(len(self.inArray)))

        else:
            self.outArray = list(self.myString[num:len(self.myString)])
            for i in range(num):
                self.outArray.append(self.inArray[i]) 
            self.myString = ''.join(self.outArray) 
            return self
        

    def __rshift__(self, num):
        if num <= 0 | num == len(self.inArray): 
            self.myString = ''.join(self.inArray) 
            return self

        elif num == len(self.inArray):
            self.myString = ''.join(self.inArray) 
            return self

        elif num > len(self.inArray):
            pass
#            raise  Exception("Error " + str(num) + " greater that string length " + str(len(self.inArray)))

        else:
            self.outArray = list(self.myString[len(self.inArray) - num:])            
            for i in range(len(self.inArray) - num):
                self.outArray.append(self.inArray[i]) 
            self.myString = "".join(self.outArray)
            return self

    
if __name__ == "__main__":
    a = sstr("abcde")
    print("a << 0", a << 0)
    print("Type ", type(a << 0))
    print("a << 1", a << 1)
    print("a << 2", a << 2)
    print("a << 3", a << 3)
    print("a << 4", a << 4)    
    print("a << 5", a << 5)
    print("Type" , type(a << 5))
    print("a << 6", a << 6)     
    print("a >> 1", a >> 1)       
    print("a >> 2", a >> 2)
    print("a >> 3", a >> 3)
    print("a >> 5", a >> 5)  
    print("Type" , type(a >> 5))
    print("a >> 6", a >> 6)    
    print(((a >> 5) << 5 == 'abcde'))
