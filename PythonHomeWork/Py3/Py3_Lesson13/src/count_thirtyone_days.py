'''
Created on Nov 25, 2013

@author: rduvalwa2
'''
# import datetime
from datetime import datetime, timedelta  # more attractive import
# now = datetime.datetime.now()
now = datetime.now()
delta = timedelta(31)  # create a timedelata of 31 days
# date = now.strftime("%d")
# delivery = now + int(date) + 31
delivery = now + delta
# print("Today: %s" % date)
print("Today is %s" % now.strftime("%d"))
# print("Delivery: %s" % delivery)
print("Delivery: %s" % delivery.strftime("%d"))
