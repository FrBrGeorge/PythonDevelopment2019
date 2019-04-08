#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser

def adjust(widg, row_val = 1,col_val = 1):
    for i in range(widg.size()[0]):
        widg.columnconfigure(i, weight=col_val)
    for i in range(widg.size()[1]):
        widg.rowconfigure(i, weight=row_val)



class App(Frame):
    '''Base framed application class'''
    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.create()
        

    def askcolor(self):
        self.canvas1.foreground.set(colorchooser.askcolor()[1])
    

    def create(self):
        self.canvas1 = Paint(self, foreground="midnightblue")
        self.canvas1.grid(row=0, column=0, sticky=N+E+S+W)

        self.control = Frame(self, bg = 'gray')
        control = self.control
        control.grid(row=0, column=1, sticky=N+E+S+W)

        self.AskColor = Button(control, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=0, sticky=N+E+W, pady=30)

        self.ShowColor = Label(control, textvariable=self.canvas1.foreground)
        self.ShowColor.grid(row=1, column=0, sticky=N+E+W, pady=30)

        self.Quit = Button(control, text="Quit", command=self.quit)
        self.Quit.grid(row=2, column=0, sticky=N+E+W, pady=30)

        adjust(control, row_val = 0)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 0)
        self.rowconfigure(0, weight = 1)
        

           
class Paint(Canvas):
    '''Canvas with simple drawing'''
    def mousedown(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
        '''Dragging is done'''
        self.cursor = None
        #print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)
    

app = App(Title="Canvas Example")
app.mainloop()