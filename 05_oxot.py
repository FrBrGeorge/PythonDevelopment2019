#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import glob
import os
import codecs

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
	global Ndict
	if Ndict.get(L.selection_get()):
		I["image"]=Images[Ndict[L.selection_get()]+'.png']
	else:
		I["image"]=Images[L.selection_get()+'.png']


Names = glob.glob('*.png')
Images = {k:PhotoImage(file=k) for k in Names}
Names = list(map(lambda x: x[:-4], Names))
Name = StringVar(value=Names)

a = Name.get()[1:-1].split(', ')
b = list(map(lambda x: x[1:-1], a))
bb = list(map(lambda x: x[1:-1], a))

Ndict = {}

for n, i in enumerate(b):
	if os.path.isfile(i+'.txt'):
		F = codecs.open(i+'.txt', 'r', encoding='iso-8859-1')
		c = F.readline()
		Ndict[c] = bb[n]
		bb[n] = c

Name2 = StringVar(value=bb)

L = Listbox(root, listvariable=Name2)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
