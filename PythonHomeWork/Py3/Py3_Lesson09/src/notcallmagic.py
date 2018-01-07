"""
Demonstrate how to make instances callable.
"""
 
class funclike:
	
	def notCall(self, *args, **kwargs):
		print("Args are:", args)
		print("Kwargs are:", kwargs)
 
f = funclike()
f(1, 2, 3, this="one", that="the other")

"""
E:\Python\Lesson_9>python notcallmagic.py
Traceback (most recent call last):
  File "notcallmagic.py", line 12, in <module>
    f(1, 2, 3, this="one", that="the other")
TypeError: 'funclike' object is not callable
"""
