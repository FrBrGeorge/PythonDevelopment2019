
from tkinter import * 
import time
import random 

def bt_func(*args):
    bt3.grid(row = 1, column = 0)
    txt.grid(row = 1, column = 1)

def bt3_func(*args):
    txt.configure(bg = "#%06x" % random.randint(0, 0xFFFFFF), fg = "#%06x" % random.randint(0, 0xFFFFFF))

TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.pack(fill = BOTH, expand = 1)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 2)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.rowconfigure(2, weight = 1)

bt = Button(root, command = bt_func, text = "ADD")
bt.grid(row = 0, column = 0)

bt_exit= Button(root, text = "EXIT", command = TKroot.destroy)
bt_exit.grid(row = 0, column = 1)


bt3 = Button(root, text = "BUTTON", bg = "darkRED", fg = "peachpuff")
bt3.bind('<Button 1>', bt3_func)

txt = Label(root, text="LABELLABELLABELLABELLABEL")



#txt.grid()

root.mainloop()

print("A")
