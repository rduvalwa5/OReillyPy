'''
Created on Jan 7, 2013
sidebyside.py
@author: rduvalwa2
'''
from tkinter import *

root = Tk()

#w = Label(root, text="Red Label", bg="red", fg="white")
#w.pack(side=LEFT)
#w = Label(root, text="Green Label", bg="green", fg="black")
#w.pack(side=LEFT)
#w = Label(root, text="Blue Label", bg="blue", fg="white")
#w.pack(side=LEFT)

#w = Label(root, text="Red Label", bg="red", fg="white")
#w.pack(side=TOP)
#w = Label(root, text="Green Label", bg="green", fg="black")
#w.pack(side=TOP)
#w = Label(root, text="Blue Label", bg="blue", fg="white")
#w.pack(side=TOP)

w = Label(root, text="Red Label", bg="red", fg="white")
w.pack(side=TOP,fill=BOTH)
w = Label(root, text="Green Label", bg="green", fg="black")
w.pack(side=TOP,fill=BOTH, expand=True)
w = Label(root, text="Blue Label", bg="blue", fg="white")
w.pack(side=TOP,fill=BOTH,expand=True)

mainloop()
