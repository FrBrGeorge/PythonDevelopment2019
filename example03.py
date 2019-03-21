#!/usr/bin/env python3
'''
Homework on 04_PublishingAndGeometry
'''

from tkinter import *
from rgb import Colors
import random

def dump(*args, **argp):
    '''Prints any of arguments passed'''
    print("DUMP:",args,argp)

def randomcolor(bright=True):
    b, d = "ABCDEF", "0123456"
    return "#"+"".join(random.choice(c)+random.choice(b+d) for c in random.sample(((b,b,b,d,d) if bright else (d,d,d)), 3))

def addadd():
    '''Add new Button/label pair to root'''
    # Here's a trick, callback is generated too!
    def c():
        '''Change colors of this very l and b'''
        l["background"]=randomcolor(False)
        l["foreground"]=randomcolor(True)
        b["background"]=randomcolor(True)
        b["foreground"]=randomcolor(False)

    b = Button(root, text="Color", command=c)
    l = Label(root, text="Color")
    c, r = root.size()
    root.rowconfigure(r+1, weight=1)
    b.grid(row=r+1, column=0, sticky=E+W+S+N)
    l.grid(row=r+1, column=1, sticky=E+W+S+N)

TKroot = Tk()
TKroot.title("Hello")

TKroot.columnconfigure(0, weight=1)
TKroot.rowconfigure(0, weight=1)
root = Frame(TKroot)
root.grid(sticky=E+W+S+N)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)

Add = Button(root, text="Add", command=addadd)
Add.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

TKroot.mainloop()
print("Done")
#root.destroy()
