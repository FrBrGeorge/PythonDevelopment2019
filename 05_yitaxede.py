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
    I["image"]=Images[Names[L.selection_get()]]

Img_ids = set(map(lambda s: s[:-4], filter(lambda s: s.lower().endswith(".png"), os.listdir())))
#Names = {visible_name : Img_id}
Names = {id : id for id in Img_ids}
Txt_ids = set(map(lambda s: s[:-4], filter(lambda s: s.lower().endswith(".txt"), os.listdir())))
Images = {name : PhotoImage(file=name+".png") for name in Names}

dumb_counter = 0

for img_id in Img_ids:
    if img_id in Txt_ids:
        f = open(img_id+".txt", "r", encoding="utf-8")
        old_name = img_id
        try:
            new_name = f.readline().strip()
        except UnicodeDecodeError:
            new_name = "I USE NON-UNICODE ENCODING FOR MY TEXT FILES. KILL ME PLZ! " + str(dumb_counter)
            dumb_counter += 1
        f.close()
        Names[new_name] = Names[old_name]
        del Names[old_name]
    else:
        print("It looks like there is no " + img_id + ".txt for " + img_id + ".png")
        
for txt_id in Txt_ids:
    if not txt_id in Img_ids:
        print("It looks like there is no " + txt_id + ".png for " + txt_id + ".txt")
        
Name = StringVar(value=list(Names.keys()))

Scr = Scrollbar(root, orient=HORIZONTAL)
Scr.grid(column=0, row=1, sticky=E+W)

L = Listbox(root, listvariable=Name, height=20, xscrollcommand=Scr.set)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()
Scr.config(command=L.xview)

TKRoot.mainloop()
