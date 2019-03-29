#!/usr/bin/env python3
'''
Homework on 04_PublishingAndGeometry
'''



from tkinter import *
from rgb import Colors
import random

def randomcolor(bright=True):
    b, d = "ABCDEF", "0123456"
    return "#"+"".join(random.choice(c)+random.choice(b+d) for c in random.sample(((b,b,b,d,d) if bright else (d,d,d)), 3))


def add():
    def c():
        l["background"] = randomcolor(False)
        l["foreground"] = randomcolor(True)
        b["background"] = randomcolor(True)
        b["foreground"] = randomcolor(False)

    b = Button(root1, text="Color", command=c)
    l = Label(root1, text="Color")
    c, r = root1.size()

    root1.columnconfigure(0, weight=1)
    root1.columnconfigure(1, weight=1)

    root1.rowconfigure(r + 1, weight=1)
    #root1.rowconfigure(r, weight=1)

    b.grid(row=r + 1, column=0, sticky=E + W + S + N)
    l.grid(row=r + 1, column=1, sticky=E + W + S + N)


TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx = 0, rely = 0, relwidth = 1)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)

Add = Button(root, text="Add", command=add)
Add.grid(row=0, column=0, sticky=E+W+S+N)

Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

root1 = Frame(TKroot)
root1.place(relx = 0, rely = 0.2, relheight = 1, relwidth = 1)

root.mainloop()

