
'''
Работа с textvariable
'''

from tkinter import *

def GetText(*args):
    print(txt.get())

def PutText(*args):
    pass

TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.place(relheight = 1.0, relwidth = 1.0)



txt = Entry(root, text = "TEXT")
txt.grid(columnspan =2)

txt2 = Entry(root, text = "TEXT")
txt2.grid(columnspan =2)

get = Button(root, text = "get", command =GetText)
get.grid();

put = Button(root, text = "put", command = PutText)
put.grid(column  = 1, row = 2);



TKroot.mainloop()