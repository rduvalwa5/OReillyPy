'''
CHere are your instructions:

Modify the Subscriber.process() method so that the instance counts the number of times the method has been called. 
If, after processing the current message, it has processed three messages, it unsubscribes itself. 

Remove the unsubscribe code from the loop at the end of the main program, since it should no longer be necessary. 

Insert print() statements in your modified program until you think you have worked out why it no longer operates correctly, 
and see if you can suggest a way to fix it (whether or not you are able to implement your suggestion).
---------------------
Overall Comments:
Each simple subscriber should be keeping track of how many times its own process( ) is called
and unsubscribe itself after that number of times gets to 3.  The counting should be happening
internally to each subscriber.

There's no need to do anything with multiplier, I suggest removing it from the picture.

When things are working correctly, each subscriber should get three consecutive issues
starting with one of the same number e.g. Sub3 gets Issue3, Issue4, Issue5, while Sub4
gets Issues 4, 5, 6 and so on.  Excerpting from the current version:

Input 5: I5
Sub0 : I5
Sub1 : I5
Sub3 : I5
Sub4 : I5
Sub5 : I5
Count is  3

Sub0 is still hanging around to get Issue5.  Clearly something is wrong.
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
            subscriber(s)

if __name__ == '__main__':
    def multiplier(s):
        print(2 * s)

    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
        def process(self, s):
            print(self, ":", s.upper())
        def __repr__(self):
            return self.name

    publisher = Publisher()
    publisher.subscribe(multiplier)
    count = 0
    for i in range(6): 
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
        count += 1
        print("Count is " , count)
        # this print is useful to compare to the list after the subscriber is removed
        for sub in publisher.subscribers:
                print(sub)
        if count == 3:
            # This removes the last entry
            publisher.unsubscribe(publisher.subscribers[-1])
            count = 0
            # This print statement shows me that the count is counting correctly, I always mess this up
            print("Count is reset " , count)
            # This print verifies the correct subscriber was removed
            for sub in publisher.subscribers:
                    print(sub)
# This print statement show me the final
    for sub in publisher.subscribers:
            print(sub)
