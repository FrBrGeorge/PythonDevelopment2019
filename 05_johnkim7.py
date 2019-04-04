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

Names = []
for file in os.listdir():
    if ".png" in file:
        Names += [k]
Images = { k : PhotoImage(file = k) for k in Names}

for i in range(len(Names)):
    txt_file = Names[i].replace(".png", ".txt")
    if txt_file in os.listdir():
        with open(txt_file, 'r') as file:
            Names[i] = file.read()
    else:
        print("No file:", Names[i], ". Using default name")
        Names[i] = 'default'

for file in os.listdir():
    if '.txt' in file and not(file.replace(".txt", ".png") in os.listdir()):
        print("No .png file for file:", file)

Name = StringVar(value = Names)

L = Listbox(root, listvariable = Name)
L.grid(column = 0, row = 0, sticky = E + W + N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row = 0, column = 1, sticky = E + W + S + N)
FaceSelect()

TKRoot.mainloop()
