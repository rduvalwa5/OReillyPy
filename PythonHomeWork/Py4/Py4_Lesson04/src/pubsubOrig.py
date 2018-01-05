'''
Here are your instructions:

Modify the Subscriber.process() method so that the instance counts the number of times the method has been called. 
If, after processing the current message, it has processed three messages, it unsubscribes itself. 

Remove the unsubscribe code from the loop at the end of the main program, since it should no longer be necessary. 

Insert print() statements in your modified program until you think you have worked out why it no longer operates correctly, 
and see if you can suggest a way to fix it (whether or not you are able to implement your suggestion).
'''

class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        for subscriber in self.subscribers:
#            subscriber.process(s)
            subscriber(s)

if __name__ == '__main__':
    def multiplier(s):
        print(2 * s)

    class SimpleSubscriber:
        def __init__(self, name, publisher):
#            publisher.subscribe(self)
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
        def process(self, s):
            print(self, ":", s.upper())
        def __repr__(self):
            return self.name

    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6): 
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
        if len(publisher.subscribers) > 3:
            publisher.unsubscribe(publisher.subscribers[0])
            
'''
 Input 0: pub
 pubpub
 Sub0 : PUB
 Input 1: and
 andand
 Sub0 : AND
 Sub1 : AND
 Input 2: sub
 subsub
 Sub0 : SUB
 Sub1 : SUB
 Sub2 : SUB
 Input 3: and
 Sub0 : AND
 Sub1 : AND
 Sub2 : AND
 Sub3 : AND
 Input 4: dub
 Sub1 : DUB
 Sub2 : DUB
 Sub3 : DUB
 Sub4 : DUB
 Input 5: and
 Sub2 : AND
 Sub3 : AND
 Sub4 : AND
 Sub5 : AND
'''
