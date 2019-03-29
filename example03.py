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


def add(*args):
    def c():
        l["background"] = randomcolor(False)
        l["foreground"] = randomcolor(True)
        b["background"] = randomcolor(True)
        b["foreground"] = randomcolor(False)

    b = Button(root, text="Color", command=c)
    l = Label(root, text="Color")
    c, r = root.size()
    root.rowconfigure(r + 1, weight=1)
    b.grid(row=r + 1, column=0)
    l.grid(row=r + 1, column=1)


TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.pack(side="left")
#root.place(relx = 0, rely = 0)

Add = Button(root, text = "Add")
Add.bind('<Button-1>', add)
Add.grid(row = 0, column = 0)
#Add.pack(side="left")
#Add.place(x = 10, y = 10)

Exit = Button(root, text="Quit", command = root.quit)
Exit.grid(row = 0, column = 1)
#Exit.pack(side="right")
#Exit.place(x = 70, y = 10)

root.mainloop()
