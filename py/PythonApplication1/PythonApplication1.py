
from tkinter import * 
import time

def fnb(*args):
    print("a", *args)

def move(*args):
    for i in range (100):
        txt.place(x=i,y=i)
        time.sleep(0.1)

TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.pack(fill = BOTH, expand = 1)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 2)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.rowconfigure(2, weight = 1)
bt = Button(root, command = fnb, text = "   command                          ")
bt.grid(row = 0, column = 0)

bt2 = Button(root, text = "               bind                     ")
bt2.grid(row = 0, column = 1)
bt2.bind('<Button 1>', fnb)

bt3 = Button(root, text = "              move                ", bg = "darkRED", fg = "peachpuff")
bt3.bind('<Button 1>', move)
bt3.grid(row = 1, column = 0, sticky = W + E + N + S, columnspan = 2)

btq = Button(root, command = root.destroy, text = "           quit                           ")
btq.grid(row = 2, column = 1)

txt = Label(root, text="LABELLABELLABELLABELLABEL")
txt.configure(bg = "black", fg = "white")

#txt.grid()

root.mainloop()

print("A")
