#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import os
import sys

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[OrigName[L.selection_get()]]

Names = set()
Alias = dict()
OrigName = dict()
Files = os.listdir(".")
for n in Files:
    if n.endswith(".png"):
        n0 = n[:-4]
        Names.add(n0)
        a = n0
        nt = n0 + ".txt"
        if nt in Files:
            try:
                with open(nt) as f:
                    a = f.read().strip()
            except UnicodeError:
                print("WARNING: encoding problem: " + nt)
        else:
            print("WARNING: not found " + nt)
        if a in Alias.values():
            print("ERROR: " + n0 + ": alias " + a +
                  " already used for " + OrigName[a])
            sys.exit(1)
        Alias[n0] = a
        OrigName[a] = n0

Aliases = tuple(Alias.values())
Images = {k:PhotoImage(file=k+".png") for k in Names}
Name = StringVar(value=Aliases)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
