#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
from pathlib import Path

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    I["image"]=Images[L.selection_get()]

def get_image_name(image_path):
    txt_path = image_path.parent / (image_path.stem + ".txt")
    if txt_path.is_file():
        with txt_path.open("r") as file:
            return file.read()
    else:
        return image_path.stem

Images = {}
dir_path = Path(__file__).parent
for file_path in dir_path.iterdir():
    if file_path.suffix == ".png":
        image_name = get_image_name(file_path)
        Images[image_name] = PhotoImage(file=file_path.name)
Name = StringVar(value=list(Images))

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
