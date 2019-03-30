#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''
import os
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



ListNames = []
rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        
        base = (os.path.splitext(os.path.basename(file))[0])
        if file.endswith(".png"):
            #print (base)
            ListNames.append(base)


for file in ListNames:
      txt_file = file + ".txt"
      if txt_file in os.listdir(): 
          with open(txt_file, 'r') as file2:
            for line in file2:
                #line = line.strip("\n")
                print(line)
                ListNames.append(line)

      else:
          print("there is no file ",txt_file)

ListNames = [x.strip() for x in ListNames]

Names = tuple(ListNames)
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
