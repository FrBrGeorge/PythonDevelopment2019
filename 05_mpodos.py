#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
from os import listdir

pngFiles = []
txtFiles = []
for f in listdir():
    if f.endswith(".png"):
        pngFiles.append(f.split('.')[0])
    if f.endswith(".txt"):
        txtFiles.append(f.split('.')[0])

for png in pngFiles:
    if png not in txtFiles:
        print("No txt for %s.png" % png)
for txt in txtFiles:
    if txt not in pngFiles:
        print("No png for %s.txt" % txt)

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

Names = pngFiles
Images = dict()
for idx, k in enumerate(Names):
    kName = k
    if k in txtFiles:
        f = open(k+".txt", "r")
        kName = f.readline()
        f.close()
    Names[idx] = kName
    Images[kName] = PhotoImage(file=k+".png")
Name = StringVar(value=Names)
L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
