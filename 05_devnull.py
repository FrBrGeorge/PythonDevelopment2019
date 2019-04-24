#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
from os import path, listdir

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

dir = path.dirname(path.realpath(__file__))
Names = [id[3:-3] for id in listdir(dir) if "05_" == id[:3] and ".py" == id[-3:]]	
Names += ["FrBrGeorge", "FrBrGeorge_2"]

with_images_names = [k for k in Names if k+".png" in listdir(dir)]
with_images_names_but_dont_loads = with_images_names.remove('artik008')
Images = {k:PhotoImage(file=k+".png") for k in with_images_names}
Name = StringVar(value=with_images_names)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
