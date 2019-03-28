#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import os

def PrintLoners(pngs, txts: list):
    Loners = set(pngs) ^ set(txts)
    for l in Loners:
        if l in pngs:
            print("There is no \'.txt\' file for " + l + ".png")
        else:
            print("There is no \'.png\' file for " + l + ".txt")


TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

Names = [os.path.splitext(file)[0] for file in os.listdir(".") 
        if file.endswith(".png")]

TxtNames = [os.path.splitext(file)[0] for file in os.listdir(".") 
        if file.endswith(".txt")]

def ReadStrFromTxt(txt: str) -> str:
    with open(txt, errors='replace') as txtFile:
        return txtFile.readline()

ListboxNames = [ReadStrFromTxt(pic+".txt") if pic in TxtNames 
        else pic for pic in Names]

Images = {ListboxNames[i]:PhotoImage(file=Names[i]+".png") 
        for i in range(0, len(Names))}

PrintLoners(Names, TxtNames)

Name = StringVar(value=ListboxNames)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
