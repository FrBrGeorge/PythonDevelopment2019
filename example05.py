#!/usr/bin/env python3
'''
Пример работы с редактируемым текстом
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

TKroot = Tk()
TKroot.title("Text")

root = Frame(TKroot)
root.grid()

txt = Entry(root, text="Text")
txt.grid()
def GetText():
    print(txt.get())
get = Button(root, text="Get", command=GetText)
get.grid()

mainloop()
