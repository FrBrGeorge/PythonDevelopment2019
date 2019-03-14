#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *

def dump(*args):
    print("DUMP:",args)

root = Tk()
root.title("Hello")

Butt = Button(root, text="Butt ON")
Butt.bind('<Button-1>', dump)
Butt.grid(row=0, column=0)
Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=0, column=1)
Txt = Label(root, text="This is a label", bg="PeachPuff")
Txt.grid(row=1, column=0, columnspan=2)

root.mainloop()
print("Done")
#root.destroy()
