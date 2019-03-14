#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Явная привязка обработчика к событию
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

root = Tk()
root.title("Hello")

Butt = Button(root, text="Butt ON")
Butt.bind('<Button-1>', dump)
Butt.grid()
root.mainloop()

