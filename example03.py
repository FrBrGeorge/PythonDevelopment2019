#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

TKroot = Tk()
TKroot.title("Hello")

TKroot.columnconfigure(0, weight=1)
TKroot.rowconfigure(0, weight=1)
root = Frame(TKroot)
root.grid(sticky=E+W+S+N)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

Add = Button(root, text="Add")
Add.bind('<Button-1>', dump)
Add.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

TKroot.mainloop()
print("Done")
#root.destroy()
