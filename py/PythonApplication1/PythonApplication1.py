
from tkinter import * 
import random 
    
#сделать ветку откатиться до нуля
#скопировать туда реп и после откатиться до переноса во фрейм далее по дз

def bt_func(*args):
    x = coloredlabel()

class coloredlabel:
    roww = 1
    def __init__(*args):
        def bt_func2(*args):
            txt.configure(bg = "#%02x%02x%02x" % (random.randint(0xAA, 0xFF),random.randint(0xAA, 0xFF),random.randint(0xAA, 0xFF)))
            txt.configure(fg = "#%02x%02x%02x" % (random.randint(0x00, 0x66),random.randint(0x00, 0x66),random.randint(0x00, 0x66)))
        bt = Button(root, text = "BUTTON", bg = "darkRED", fg = "peachpuff")
        bt.bind('<Button 1>', bt_func2)
        txt = Label(root, text="LABELLABELLABELLABELLABEL")
        bt.grid(row = coloredlabel.roww, column = 0, sticky = W + E + N + S)
        txt.grid(row = coloredlabel.roww, column = 1, sticky = W + E + N + S)
        coloredlabel.roww = coloredlabel.roww + 1
        return
    

TKroot = Tk()
TKroot.title("=)")
root = Frame(TKroot)
root.place(relheight = 1.0, relwidth = 1.0)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 3)

bt = Button(root, command = bt_func, text = "ADD")
bt.grid(row = 0, column = 0, sticky = W + E)

bt_exit= Button(root, text = "EXIT", command = TKroot.destroy)
bt_exit.grid(row = 0, column = 1, sticky = W + E)


TKroot.mainloop()

