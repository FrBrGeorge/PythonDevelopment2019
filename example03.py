#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Действие по умолчанию для кнопки (очевидно, клик)
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

root = Tk()
root.title("Hello")

Butt = Button(root, text="Butt ON", command=dump)
Butt.grid()
root.mainloop()

