#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
import os

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I['image']=Images[L.selection_get()]

Names = dict()
wopng = []
wotxt = []
for v in os.listdir('.'):
    if os.path.isfile(v):
        if v.endswith('.png'):
            v = v[0:-4]
            k = v
            t = v + '.txt'
            if (t in os.listdir('.')) and os.path.isfile(t) and os.path.getsize(t) > 0:
                f = open(t, 'r')
                k = f.readline().strip()
            else:
                wotxt.append(v + '.png')
            Names[k] = v
        elif v.endswith('.txt'):
            v = v[0:-4]
            t = v + '.png'
            if  (t not in os.listdir('.')) or not os.path.isfile(t):
                wopng.append(v + '.txt')

wotxt.sort()
wopng.sort()
print('.png files without paired .txt:', *wotxt)
print('.txt files without paired .png:', *wopng)

Images = {k: PhotoImage(file = Names.get(k) + '.png') for k in Names.keys()}
Name = StringVar(value=sorted(list(Names.keys())))

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
