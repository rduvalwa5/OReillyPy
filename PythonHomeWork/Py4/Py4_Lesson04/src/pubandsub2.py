'''
Created on Dec 29, 2013
check for errors and identify subscribers
@author: rduvalwa2
'''
class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
        for name in self.subscribers:
            print (name)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        for subscriber in self.subscribers:
            subscriber.process(s)

if __name__ == '__main__':
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            publisher.subscribe(self)
            self.name = name
            self.publisher = publisher
        def process(self, s):
            print(self.name, ":", s.upper())

    publisher = Publisher()
    for i in range(3):
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
    newSub = publisher.subscribers[0]
    print(publisher.subscribers)
    pub = len(publisher.subscribers) - 1
    while pub > -1:
        print(publisher.subscribers)
#        print("Starting Length: ", len(publisher.subscribers))
        publisher.unsubscribe(publisher.subscribers[pub])
        pub = pub - 1
        print("Pub is ", pub)
#        print("Ending Length: ", len(publisher.subscribers))
#    publisher.unsubscribe(publisher.subscribers[0])
    print("Finished ", publisher.subscribers)    
    print("Finished ", len(publisher.subscribers))
    publisher.unsubscribe(newSub)    
    
