'''
Created on Nov 25, 2013

@author: rduvalwa2
'''
from datetime import datetime, timedelta

delivery = datetime.now()
delta = timedelta(1)
count = 0
while count < 31:
    delivery = delivery + delta
    if delivery.isoweekday() in (6, 7):
        continue
    count += 1
    
now = datetime.now()
print(now)
print(delivery)
print("Today is %s" % now.strftime("%d"))
print("Delivery: %s" % delivery.strftime("%d"))
