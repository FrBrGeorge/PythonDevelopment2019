
from tkinter import * 

def fnb(*args):
    print("a", *args)

root = Tk()

bt = Button(root, command = fnb, text = "command")
bt.grid()
bt2 = Button(root, text = "bind")
bt2.grid()
bt2.bind('<Button 1>', fnb)

btq = Button(root, command = root.destroy, text = "quit")
btq.grid()
root.mainloop()

print("A")
