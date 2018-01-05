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
#    def multiplier(s):
#        print(2*s)

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
#    publisher.subscribe(multiplier)
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
