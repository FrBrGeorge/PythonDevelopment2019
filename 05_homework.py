#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["text"]=L.selection_get()

Names = {"FrBrGeorge": "Fr. Br. George", "FrBrGeorge_2": "FrBrGeorge avatar"}
Ids = tuple(Names.keys())
Nicks = tuple(Names.values())
Name = StringVar(value=Nicks)
Id = StringVar(value=Nicks)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)

TKRoot.mainloop()
