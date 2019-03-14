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
Butt.grid()
Exit = Button(root, text="QuiEt!", command=root.quit)
Exit.grid()
root.mainloop()
print("Done")
#root.destroy()
