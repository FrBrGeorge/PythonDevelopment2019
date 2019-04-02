#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import glob
import os

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

PictureNames = glob.glob('*.png')
Names = list(name[0:len(name)-4] for name in PictureNames)
Images = {k:PhotoImage(file=k+".png") for k in Names}

PictureTxt = Names

for i in range(len(PictureNames)):
    txt = PictureNames[i].replace(".png", ".txt")
    if txt in os.listdir():
        file = open(txt, 'r')
        file_context = file.read()
        PictureTxt[i] = file_context
        file.close()
    else:
        print("No txt file for image - ", PictureTxt[i])

Name = StringVar(value=Names)
L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
