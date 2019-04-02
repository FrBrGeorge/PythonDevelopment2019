#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''

from tkinter import *
from PIL import Image, ImageTk
import os

TKRoot = Tk()
TKRoot.title("HW_5_Bikbulatov")

screen_w = TKRoot.winfo_screenwidth()
screen_h = TKRoot.winfo_screenheight()
osx = screen_w/4
osy = screen_h/4
TKRoot.geometry('%dx%d+%d+%d' % (screen_w/2, screen_h/2, osx, osy))
TKRoot.resizable(False, False)

root = Frame(TKRoot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


def FaceSelect(*args):
	I["image"] = Images[Names_ident[L.selection_get()]]

Names_png = []
Names_txt = []
for name_file in os.listdir():
	if ".png" in name_file:
	    Names_png.append(name_file)
	elif ".txt" in name_file:
		Names_txt.append(name_file)

Images = {}
for k in Names_png : 
	img = Image.open(k)
	Images[k] = ImageTk.PhotoImage(img.resize((250, 250), Image.ANTIALIAS))

Names = []
Names_ident = {}
for i in range(len(Names_png)):
	png_file = Names_png[i].split('.', 1)[0]
	for j in range(len(Names_txt)):
		txt_file = Names_txt[j].split('.', 1)[0]
		if png_file == txt_file:
			with open(Names_txt[j], 'r',encoding='utf-8', errors='ignore') as file:
				info = file.read()
				Names.append(info)
				Names_ident[info] = Names_png[i]
				break
		elif j == len(Names_txt)-1 :
			print("No any txt files for", Names_png[i],". So name in Listbox will be unknown")
			Names.append(png_file+"_unknown")
			Names_ident[png_file+"_unknown"] = Names_png[i]

for name_file in os.listdir():
	if '.txt' in name_file and not(name_file.replace(".txt", ".png") in os.listdir()):
		print("No .png file for file:", name_file)

Name = StringVar(value=Names)

L = Listbox(root, listvariable=Name)
L.grid( row=0, column=0, sticky=E+W+N+S, padx=10,pady=10)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)

I = Label(root)
I.grid(row=0, column=1, sticky=E+W+N+S, padx=10,pady=10)
FaceSelect()

Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=1, column=0, columnspan=2, sticky=E+W+N+S, padx=10,pady=10)

TKRoot.mainloop()
