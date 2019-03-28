#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

import os 
from tkinter import *
from PIL import ImageTk as itk

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

Names = *filter(lambda x: x.endswith('.png'), os.listdir('.')), 

with open('./artik008.txt') as f:
    Names += tuple(f.read().splitlines())

Images = {k:itk.PhotoImage(file=k) for k in Names}
Name = StringVar(value=Names)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
