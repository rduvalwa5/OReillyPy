'''
Created on Mar 5, 2014
What is the difference between a function decorated with @staticmethod and one decorated with @classmethod?
http://stackoverflow.com/questions/11788195/module-function-vs-staticmethod-vs-classmethod-vs-no-decorators-which-idiom-is
@author: 310122001
'''
class A(object):
    def foo(self, x):
        print ("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print ("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)" % x)

if __name__ == "__main__":
    a = A()
    print("a", a)
    print(a.foo(1))
    print(a.class_foo(1))
    print(a.static_foo(1))
    print(a.static_foo("hi"))
    
