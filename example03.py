#!/usr/bin/env python3
'''
Homework on 04_PublishingAndGeometry
'''


from tkinter import *

def add(*args):
    print("DUMP:", args)

root = Tk()
root.title("Hello")

Add = Button(root, text = "Add")
Add.bind('<Button-1>', add)
Add.grid(row = 0, column = 1)
#Add.pack(side="left")
#Add.place(x = 10, y = 10)

Exit = Button(root, text="Quit", command = root.quit)
Exit.grid(row = 0, column = 2)
#Exit.pack(side="right")
#Exit.place(x = 70, y = 10)

root.mainloop()

