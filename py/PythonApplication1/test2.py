
'''
Работа с textvariable
'''

from tkinter import *

def dump(*args):
    print(args)

def GetText(*args):
    print(txt.get())

def PutText(*args):
    t = txt.get()
    s.set(t)
    
TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.place(relheight = 1.0, relwidth = 1.0)

s = StringVar()
s.set("Hello")
s.trace("w", dump)

txt = Entry(root)
txt.grid(columnspan =2)

txt2 = Entry(root, textvariable = s)
txt2.grid(columnspan =2)

getBT = Button(root, text = "get", command =GetText)
getBT.grid();

put = Button(root, text = "put", command = PutText)
put.grid(column  = 1, row = 2);



TKroot.mainloop()