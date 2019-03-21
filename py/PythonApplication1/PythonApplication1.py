
from tkinter import * 
import time
import random 

def bt_func(*args):
    bt3.grid(row = 1, column = 0, sticky = W + E + N + S)
    txt.grid(row = 1, column = 1, sticky = W + E + N + S)

def bt3_func(*args):
    txt.configure(bg = "#%02x%02x%02x" % (random.randint(0xAA, 0xFF),random.randint(0xAA, 0xFF),random.randint(0xAA, 0xFF)))
    txt.configure(fg = "#%02x%02x%02x" % (random.randint(0x00, 0x66),random.randint(0x00, 0x66),random.randint(0x00, 0x66)))
                 
TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.place(relheight = 1.0, relwidth = 1.0)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 2)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)

bt = Button(root, command = bt_func, text = "ADD")
bt.grid(row = 0, column = 0, sticky = W + E)

bt_exit= Button(root, text = "EXIT", command = TKroot.destroy)
bt_exit.grid(row = 0, column = 1, sticky = W + E)


bt3 = Button(root, text = "BUTTON", bg = "darkRED", fg = "peachpuff")
bt3.bind('<Button 1>', bt3_func)

txt = Label(root, text="LABELLABELLABELLABELLABEL")


TKroot.mainloop()

