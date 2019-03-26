#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''


from tkinter import *
from os import listdir
from os.path import isfile, join


def get_identifier(line):
	if '.' in line:
		return line[:line.rfind('.')]
	else:
		return line


filenames = [f for f in listdir('.') if isfile(join('.', f))]
png_files = list(filter(lambda x: x.endswith('.png'), filenames))
png_identifiers = list(map(get_identifier, png_files))
txt_files = list(filter(lambda x: x.endswith('.txt'), filenames))
txt_identifiers = list(map(get_identifier, txt_files))
png_name = {}

for png_identifier in png_identifiers:
	if png_identifier in txt_identifiers:
		png_name[png_identifier] = open(png_identifier + '.txt', 'r').readline().strip()
	else:
		print("No txt file for png identifier:", png_identifier)

for txt_identifier in txt_identifiers:
	if txt_identifier not in png_identifiers:
		print("No png file for txt identifier:", txt_identifier)


TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)


def FaceSelect(*args):
    I["image"] = Images[L.selection_get()]


Images = {png_name[get_identifier(file)] if get_identifier(file) in png_name else get_identifier(file): PhotoImage(file=file) for file in png_files}
Name = StringVar(value=list(Images.keys()))

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
