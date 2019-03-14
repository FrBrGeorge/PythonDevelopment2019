#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)

Butt = Button(root, text="Butt ON")
Butt.bind('<Button-1>', dump)
Butt.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)
Txt = Label(root, text="This is a label", bg="PeachPuff")
Txt.grid(row=1, column=0, columnspan=2, sticky=E+W+N)

TKroot.mainloop()
print("Done")
#root.destroy()
