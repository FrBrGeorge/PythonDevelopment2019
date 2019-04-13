#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *

import os
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

my_txt = "vmmnnn.txt"

Names = []

if os.path.isfile(my_txt):
    with open(my_txt) as f:
        Names = [line.strip('\n') for line in f]
    i = 0
    while i < len(Names):
        name_i = Names[i]
        if (os.path.isfile(name_i + ".png")):
            i += 1
        else:
            Names.remove(name_i)
else:
    pict = glob.glob('*.png')
    Names = list(map(lambda x: x[0:len(x) - 4], pict))

Images = {k: PhotoImage(file=k + ".png") for k in Names}
Name = StringVar(value=Names)


#Names = "FrBrGeorge", "FrBrGeorge_2"
#Images = {k:PhotoImage(file=k+".png") for k in Names}
#Name = StringVar(value=Names)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
