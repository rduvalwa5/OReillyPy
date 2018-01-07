'''
Created on Jun 16, 2013
demonstarte api
@author: rduval
'''
from bird_api import Bird

class Flock(object):
    birds = []
    def add_bird(self,bird):
        """
        add bird
        """
        self.birds.append(bird)
    def race(self):
        """
        Show how far the birds of the flock can go in one hour with loads
        """
        print("Distance flown in one hour by flock")
        for bird in self.birds:
            distance = "-" * (bird.calculate()// 10)
            notice = "%s: %s carrying %s items" % (distance, bird.name, len(bird.__dict__))
            print(notice)
            
if __name__ == "__main__":
    swallow = Bird(coconut=1, name="Swallow")
    african = Bird(coconut=1,piece="of string", visited=False, name="African Swallow")
    european = Bird(coconut=1,lottery_numbers=(23,12,34), piece="of string", visited=True, name="European Swallow")
    european.add("cereal boxes", 5)
    european.add("Norway", True)
    european.add("England", True)
    flock = Flock()
    flock.add_bird(swallow)
    flock.add_bird(african)
    flock.add_bird(european)
    flock.race()
    '''
    API example,
    import the Bird class from the bird_api module
    call it to create a number of birds (Bird instances)
    add the birds to our flock object
    race them against each other
    When you run the program the output clearly shows that the least-heavily 
    laden swallow travels farthest. 
    Distance flown in one hour by flock
    --------: Swallow carrying 2 items
    ------: African Swallow carrying 4 items
    --: European Swallow carrying 8 items
    '''


    
            
