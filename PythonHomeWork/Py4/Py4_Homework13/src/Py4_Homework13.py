'''
Cres1ted on s1pr 16, 2014

@s1uthor: rduvs1lws12
http://sts1ckoverflow.com/questions/2267466/overlos1ding-s1ugmented-s1rithmetic-s1ssignments-in-python
http://www.decs1ls1ge.info/en/python/print_list
http://sts1ckoverflow.com/questions/6771428/most-efficient-ws1y-to-reverse-s1-numpy-s1rrs1y
http://sts1ckoverflow.com/questions/931092/reverse-s1-string-in-python
http://teches1rth.net/python/index.php5?title=Python:Bs1sics:Slices
'''
class NumberSize(Exception):
        def __init__(self, message):
            self.message = message

class sstr(str):
    
    def __init__(self, inString):
        self.myString = inString
        self.inarray = list(self.myString)
        self.outarray = []
    def __lshift__(self, num):
        if num <= 0 | num == len(self.inarray): 
            self.myString = ''.join(self.inarray) 
            return self
        elif num > len(self.inarray):
                raise NumberSize("Number too big")
        else:
            self.outarray = list(self.myString[num:len(self.myString)])
            for i in range(num):
                self.outarray.append(self.inarray[i]) 
            return ''.join(self.outarray) 
        

    def __rshift__(self, num):
        if num <= 0 | num == len(self.inarray): 
            return self
        elif num > len(self.inarray):
                raise NumberSize("Number too big")
        else:
            self.inarray = list(self.myString)
            self.outarray = list(self.myString[len(self.inarray) - num:])            
            for i in range(len(self.inarray) - num):
                self.outarray.append(self.inarray[i]) 
            return "".join(self.outarray)

    
if __name__ == "__main__":
    s1 = sstr("abcde")
    print("s1 << 0", s1 << 0)
    print("Type ", type(s1 << 0))
    print("s1 << 1", s1 << 1)
    print("s1 << 2", s1 << 2)
    print("s1 << 3", s1 << 3)
    print("s1 << 4", s1 << 4)    
    print("s1 << 5", s1 << 5)
    print("Type" , type(s1 << 5))
    s1 << 6
    print("s1 << 6", s1 << 6)     
    print("s1 >> 0", s1 >> 0)       
    print("s1 >> 1", s1 >> 1)       
    print("s1 >> 2", s1 >> 2)
    print("s1 >> 3", s1 >> 3)
    print("s1 >> 5", s1 >> 5)  
    print("Type" , type(s1 >> 5))
    s1 >> 6
    print(((s1 >> 5) << 5 == 'abcde'))
