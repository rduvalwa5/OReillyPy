'''
Created on Apr 15, 2014
@author: rduvalwa2
'''
class mine:
    def __add__(self, other):
        print("__add__({}, {})".format(self, other))
        return NotImplemented
    def __radd__(self, other):
        print("__radd__({}, {})".format(self, other))
        return 42
    def __repr__(self):
        return "[Mine {}]".format(id(self))

class yours:
    def __add__(self, other):
        print("__add__({}, {})".format(self, other))
        return NotImplemented
    def __radd__(self, other):
        print("__radd__({}, {})".format(self, other))
        return NotImplemented
    def __repr__(self):
        return "[Yours {}]".format(id(self)) 
m1 = mine()
m2 = mine()
m1, m2
# ([Mine 4300644112], [Mine 4300643600])
y1 = yours()
y2 = yours()
y1, y2
# ([Yours 4300644240], [Yours 4300643728])
try: 
    m1 + m2
except TypeError:
    print("m1+m2 TypeError: unsupported operand type(s) for +: \'mine\' and \'mine\'")
# __add__([Mine 4300644112], [Mine 4300643600])
# Traceback (most recent call last):
#  File "<console>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'mine' and 'mine'
try:
    y1 + y2
except TypeError:
    print(" y1+y2 TypeError: unsupported operand type(s) for +: \'yours\' and \'yours\'")
# __add__([Yours 4300644240], [Yours 4300643728])
# Traceback (most recent call last):
#  File "<console>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'yours' and 'yours'
try:
    m1 + y2
except TypeError:
    print("m1+y2 TypeError: unsupported operand type(s) for +: \'mine\' and \'yours\'")
# __add__([Mine 4300644112], [Yours 4300643728])
# __radd__([Yours 4300643728], [Mine 4300644112])
# Traceback (most recent call last):
#  File "<console>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'mine' and 'yours'
print("y1+m2: ", y1 + m2)
# __add__([Yours 4300644240], [Mine 4300643600])
# __radd__([Mine 4300643600], [Yours 4300644240])
# 42 
'''
__add__([Mine 4302666384], [Mine 4302663952])
m1+m2 TypeError: unsupported operand type(s) for +: 'mine' and 'mine'
__add__([Yours 4302664016], [Yours 4302664272])
 y1+y2 TypeError: unsupported operand type(s) for +: 'yours' and 'yours'
__add__([Mine 4302666384], [Yours 4302664272])
__radd__([Yours 4302664272], [Mine 4302666384])
m1+y2 TypeError: unsupported operand type(s) for +: 'mine' and 'yours'
__add__([Yours 4302664016], [Mine 4302663952])
__radd__([Mine 4302663952], [Yours 4302664016])
'''
