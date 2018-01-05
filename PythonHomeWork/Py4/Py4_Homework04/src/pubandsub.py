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
#        print("Unsubscribe ", subscriber)
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        for subscriber in self.subscribers:
            subscriber(s)
            
if __name__ == '__main__':
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            print("Init for ", name)
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
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
    
'''
 Input 0: a
Sub0 : LINE A
Input 1: b
Sub0 : LINE B
Sub1 : LINE B
Input 2: c
Sub0 : LINE C
Sub1 : LINE C
Sub2 : LINE C
Input 3: d
Sub1 : LINE D
Sub2 : LINE D
Sub3 : LINE D
Input 4: e
Sub2 : LINE E
Sub3 : LINE E
Sub4 : LINE E
Input 5: f
Sub3 : LINE F
Sub4 : LINE F
Sub5 : LINE F
Input 6: g
Sub4 : LINE G
Sub5 : LINE G
Sub6 : LINE G
End [<bound method SimpleSubscriber.process of Sub2>, <bound method SimpleSubscriber.process of Sub3>, <bound method SimpleSubscriber.process of Sub4>, <bound method SimpleSubscriber.process of Sub5>, <bound method SimpleSubscriber.process of Sub6>]
'''       
