'''
Created on Jan 19, 2014
@author: rduvalwa2
'''
class Publisher:
    def __init__(self):
        self.subscribers = {}
        
    def subscribe(self, subname, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
#        self.subscribers.append(subscriber)
        self.name = subname
        self.process = subscriber
        self.subscribers.update({self.name:self.process})
        
    def unsubscribe(self, subscriber):
#        print("Unsubscribe ", subscriber)
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
        
    def publish(self, name, s):
        for subscriber in self.subscribers:
            subscriber(s)
            
if __name__ == '__main__':
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            print("Init for ", name)
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.name, self.process)
            self.count = 0
        def process(self, s):
#            print("Processing ",self, "Count ",self.count)
            if self.count < 3:
                print(self, ":", s.upper())
            elif self.count > 3:                    
                self.publisher.unsubscribe(publisher.subscribers[0])
            self.count = self.count + 1
            print("Newsub", publisher.subscribers)
            
        def __repr__(self):
            return self.name

    publisher = Publisher()
    for i in range(8): 
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i)) 
        publisher.publish("Line " + line)
    print("End", publisher.subscribers) 
    
