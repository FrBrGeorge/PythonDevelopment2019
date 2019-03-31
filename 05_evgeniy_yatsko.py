#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

import glob
import os.path
from tkinter import *

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]



try:
	with open("evgeniy_yatsko.txt") as in_file:
		Names = in_file.read().splitlines()
except OSError:
	Names = glob.glob('*.png')
Images = {k:PhotoImage(file=k) for k in Names}
Name = StringVar(value=Names)



L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N, rowspan = 3)
FaceSelect()

I2 = Label(root, text = "Нету txt:",)
I2.grid(row = 1, column = 0, sticky = E+W+N)

def check_existing():
	return [image_name for image_name in glob.glob('*.png') if not os.path.exists(image_name[:-3] + "txt")]

not_existing_names = StringVar(value = check_existing())
print(not_existing_names.get())
L2 = Listbox(root, listvariable = not_existing_names)
L2.grid(row = 2, column = 0, sticky = E+W+N)

TKRoot.mainloop()
