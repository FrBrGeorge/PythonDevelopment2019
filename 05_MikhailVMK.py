#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''
from os import path, listdir
from tkinter import *

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]
Directory = path.dirname(path.realpath(__file__))
DefaultNames = [fname[:len(fname)-4] for fname in listdir(Directory) if len(fname)>=4 and fname[len(fname)-4:] == ".png"]  
DesiredNamesMap = {x: open(Directory + x + ".txt").readline() for x in DefaultNames if Directory + x + ".txt" in listdir(Directory)}
Names = [DesiredNamesMap.get(x, x) for x in DefaultNames]
Images = {k:PhotoImage(file=k+".png") for k in Names}
Name = StringVar(value=Names)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
