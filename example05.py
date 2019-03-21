#!/usr/bin/env python3
'''
Пример работы с редактируемым текстом
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

def GetText():
    print(txt.get())

def PutText():
    t = txt.get()
    str2.set(t)

TKroot = Tk()
TKroot.title("Text")

root = Frame(TKroot)
root.grid()

txt = Entry(root, text="Text")
txt.grid(columnspan=2)
str2 = StringVar()
str2.trace("w", dump)
txt2 = Entry(root, text="Tex2", textvariable=str2)
txt2.grid(columnspan=2)
getButton = Button(root, text="Get", command=GetText)
getButton.grid()
putButton = Button(root, text="Put", command=PutText)
putButton.grid(column=1,row=2)

mainloop()
