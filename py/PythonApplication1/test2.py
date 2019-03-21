
'''
Работа с textvariable
'''

from tkinter import * 

TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.place(relheight = 1.0, relwidth = 1.0)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 2)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)

txt = Entry(root, text = "TEXT")
txt.grid()
def GetText(*args):
    print(txt.get())


get = Button(root, text = "get", command =GetText)
get.grid();

TKroot.mainloop()