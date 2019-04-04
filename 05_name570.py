#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import os

TKRoot = Tk()
TKRoot.columnconfigure(0, weight = 1)
TKRoot.rowconfigure(0, weight = 1)
root = Frame(TKRoot)
root.grid(column = 0, row = 0, sticky = E + W + S + N)
root.columnconfigure(0, weight = 0)
root.columnconfigure(1, weight = 1)

def FaceSelect(*args):
    I["image"] = Images[NamesDict[L.selection_get()]]



Names = []
Images = {}

for k in os.listdir():
    if ".png" in k:
        Names.append(k)

Images = { k : PhotoImage(file = k) for k in Names}

NamesDict = {}

for i in range(len(Names)):

    txt_for_img = Names[i].replace(".png", ".txt")

    if txt_for_img in os.listdir():
        file = open(txt_for_img, 'r')
        file_context = file.read()
        NamesDict[file_context] = Names[i]
        Names[i] = file_context
        file.close()

    else:
        print("No name for file = ", Names[i], ". Using default name")
        NamesDict[Names[i]] = Names[i]


for file in os.listdir():
    if '.txt' in file and not(file.replace(".txt", ".png") in os.listdir()):
        print("There is no .png file for file ", file)




#Images = {k:PhotoImage(file = k) for k in Names}
Name = StringVar(value = Names)

L = Listbox(root, listvariable = Name)
L.grid(column = 0, row = 0, sticky = E + W + N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row = 0, column = 1, sticky = E + W + S +N)
FaceSelect()

TKRoot.mainloop()
