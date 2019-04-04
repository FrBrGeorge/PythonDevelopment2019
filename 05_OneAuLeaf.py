#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import glob

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

def SearchNames():
    Names = {}
    for x in (x[:-4] for x in glob.iglob("*.png")):
        if x in (x[:-4] for x in glob.iglob("*.txt")):
            Names[x] = open(f"{x+'.txt'}").readline()
        else:
            Names[x] = x
            print(f"Not found name for picture {x+'.png'}, set default: {x}")
    return Names

Names = SearchNames()
Images = {Names[k]:PhotoImage(file=k+".png") for k in Names}
Name = StringVar(value=tuple(Names.values()))

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
