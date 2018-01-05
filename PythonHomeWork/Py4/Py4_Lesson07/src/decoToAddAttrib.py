'''
Created on Feb 27, 2014
Using a decorator to add attributes rather than wrapping a function
@author: rduvalwa2
'''

# def framework(f):
#    f.framework = True
#    f.author = "Myself"
#    return f

# @framework
def somefunc():
        mybook = ""


if __name__ == "__main__":
        a = somefunc()
        somefunc("History")
        print(a.__dict__)
#        print(mybook)
#        return mybook

# print(somefunc("History"))
# somefunc.framework
# print("somefunc ",somefunc.author)
# print(somefunc.__dict__)
