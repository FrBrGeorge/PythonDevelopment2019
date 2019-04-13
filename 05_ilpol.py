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
    #print("L.selection_get = ",L.get(L.curselection()))
    I["image"]=Images[text_picture[L.selection_get()]]

ListNames = []
rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        
        if file.endswith(".png"):
           ListNames.append(file)



Names = list(name[0:len(name)-4] for name in ListNames)
Picture_names = Names.copy()
Images = {k:PhotoImage(file=k+".png") for k in Names}

PictureTxt = Names

for i in range(len(ListNames)):
    txt = ListNames[i].replace(".png", ".txt")
    if txt in os.listdir():
        file = open(txt, 'r')
        file_context = file.read()
        PictureTxt[i] = file_context.rstrip()
        file.close()
    else:
        print("There is no text for ", PictureTxt[i])

text_picture = {}
for text, picture_name in zip(Names, Picture_names):
    text_picture[text] = picture_name


Name = StringVar(value=Names)
L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()