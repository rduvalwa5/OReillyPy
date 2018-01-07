'''
@author: rduvalwa2
'''
class Centipede(): 
    stomach = [] 
    legs = []    
    def __call__(self, *args, **kwargs):
        print("ARGS is: ", args[0])
        if args[0] in [self, self.stomach, self.legs]:
            raise AttributeError
            print("Already got" , args)
        else:
            self.stomach.append(args[0])
            
#    def __setattr__(self):
#            self.key = args
#            self.value = kwargs
#            print("ATTR: setting attribute {0!r} ".format(self.key))
#            self.__dict__[args] = kwargs
#            raise
 
#    def __getattr__(self, key):
#        print("ATTR: getting attribute {0!r}".format(key))
#        self.__setattr__(key, "No value")
#        return "No value"

    def __str__(self):
        return ','.join(self.stomach) 
    
    def __repr__(self):        
        lst = []
        for item in self.__dict__:
            lst.append(item[0:])
        return ','.join(sorted(lst, reverse=True))
        
if __name__ == "__main__":
#    from centipede import Centipede
    ralph = Centipede()
    ralph('chocolate')
    ralph('bbq')   
    ralph.friends = ['Steve', 'Daniel', 'Guido']        
    ralph.favorite_show = "Monty Python's Flying Circus"        
    ralph.age = '31'
    ralph('cookies')         
    ralph('salad') 
#    ralph.legs = ['shoes','socks','sandals'] 
    ralph('salad')      
    print("stomach", ralph.stomach)
    print("ralph.stomach", ralph.stomach)
    print("dict :", ralph.__dict__)
#    print("ralph: ", ralph)
    print("ralph.__str__: ", ralph.__str__())
    print(ralph.age)
    print(ralph.__repr__())
    legs = []
    ralph(legs)
    # ralph('stomach')
    # xralph(ralph)
    # ralph(setattr)
    # ralph([])
