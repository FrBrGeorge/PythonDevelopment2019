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
	

if os.path.isfile("cizlota.txt"):
	Names = [line.rstrip('\n') for line in open("cizlota.txt")]
	i = 0
	while i < len(Names):
		if (os.path.isfile(Names[i] + ".png") == False):
			Names.remove(Names[i])
		else:
			i += 1
			
	Images = {k:PhotoImage(file=k+".png") for k in Names}
	Name = StringVar(value=Names)
else:
	Namespng = glob.glob('*.png')
	Names = list(map(lambda x: x[0:len(x)-4], Namespng))
	Images = {k:PhotoImage(file=k+".png") for k in Names}
	Name = StringVar(value=Names)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
