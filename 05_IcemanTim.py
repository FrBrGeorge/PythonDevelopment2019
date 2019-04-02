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
	I["image"] = Images[L.selection_get()] 


Names = "7", "cizlota_1", "6"
Images = {}
for k in Names : 
	img = Image.open(k+".png")
	Images[k] = ImageTk.PhotoImage(img.resize((250, 250), Image.ANTIALIAS))
Name = StringVar(value=Names)

l = os.listdir()
print(l)

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



# Модифицировать это дерево таким образом, чтобы:
# - программа просматривал все .png-файлы в текущем каталоге, и из всех идентификаторов строила Listbox
# - программа также просматривала файлы вида идентификатор.txt, в которых хранится предпочитаемое имя для Listbox, и из этих имён его и составляла
# - (необязательно) программа должна сообщать о том, сто для каких-то .png нет соответствующих .txt и наоборот