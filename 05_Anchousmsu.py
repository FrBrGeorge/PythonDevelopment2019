#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import glob, os


TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

def NamesListbox():
    for name in Names_images:
        try:
            with open(name + '.txt', 'r') as f:
                text = f.read()
                Names_txt.remove(name)
        except:
            print('No file .txt for ' + name + '.png')
            text = name
        Images[text] = PhotoImage(file=name+".png")
        Names.append(text)
    for name in Names_txt:
        print('No file .png for ' + name + 'txt')

os.chdir(os.getcwd())
Names_images = [file[:-4] for file in glob.glob("*.png")]
Names_txt = [file[:-4] for file in glob.glob("*.txt")]

Images = {}
Names = []
NamesListbox()

Name = StringVar(value=tuple(Names))

L = Listbox(root, listvariable = Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
