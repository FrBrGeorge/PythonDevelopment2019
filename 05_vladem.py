#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
from os import listdir
from os.path import isfile, join, exists

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[Aliases[L.selection_get()]]

Names = [f for f in listdir("./") if isfile(join("./", f)) and f.endswith(".png")]
Aliases = {open(fname[:-4:] + ".txt").read().replace('\n', '') if exists(fname[:-4:] + ".txt") else fname: fname for fname in Names}
Images = {k:PhotoImage(file=k) for k in Names}
Name = StringVar(value=list(Aliases.keys()))

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
