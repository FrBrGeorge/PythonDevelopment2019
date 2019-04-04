from tkinter import *
import os


TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

txt = []
png = []
name_img = {}
for filename in os.listdir():
	if filename.endswith('.png'):
		png.append(os.path.splitext(filename)[0])
	if filename.endswith('.txt'):
		txt.append(os.path.splitext(filename)[0])

for imgname in png:
	if imgname not in txt:
		name_img[imgname] = PhotoImage(file = imgname+'.png')
	else:
		with open(imgname+'.txt') as f:
			try:
				name_img[f.readline().strip()] = PhotoImage(file = imgname+'.png')
			except:
				name_img[imgname] = PhotoImage(file = imgname+'.png')

def FaceSelect(*args):
	I["image"]=name_img[L.selection_get()]

Name = StringVar(value=list(name_img.keys()))

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
