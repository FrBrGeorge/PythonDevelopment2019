
'''
Работа с textvariable
'''

from tkinter import *

def GetText(*args):
    print(txt.get())

def PutText(*args):
    t = txt.get()
    txt2.delete(0, END)
    txt2.insert(0, t)

TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.place(relheight = 1.0, relwidth = 1.0)

txt = Entry(root, text = "TEXT")
txt.grid(columnspan =2)

txt2 = Entry(root, text = "TEXT2")
txt2.grid(columnspan =2)

getBT = Button(root, text = "get", command =GetText)
getBT.grid();

put = Button(root, text = "put", command = PutText)
put.grid(column  = 1, row = 2);



TKroot.mainloop()