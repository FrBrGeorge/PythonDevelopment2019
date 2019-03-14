
from tkinter import * 
import time

def fnb(*args):
    print("a", *args)

def move(*args):
    for i in range (100):
        txt.place(x=i,y=i)
        time.sleep(0.1)

root = Tk()

bt = Button(root, command = fnb, text = "   command                          ")
bt.pack()
bt2 = Button(root, text = "               bind                     ")
bt2.pack(side = TOP, fill=X)
bt2.bind('<Button 1>', fnb)
bt3 = Button(root, text = "              move                ")
bt3.bind('<Button 1>', move)
bt3.pack(side  = LEFT)
btq = Button(root, command = root.destroy, text = "           quit                           ")
btq.pack()

txt = Label(root, text="LABELLABELLABELLABELLABEL")
txt.configure(bg = "black", fg = "white")
txt.place(x = 10, y = 10)


#txt.grid

root.mainloop()

print("A")
