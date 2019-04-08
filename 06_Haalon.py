#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

def adjust(widg, row_val = 1,col_val = 1):
    for i in range(widg.size()[0]):
        widg.columnconfigure(i, weight=col_val)
    for i in range(widg.size()[1]):
        widg.rowconfigure(i, weight=row_val)


class App(Frame):
    """docstring for App"""
    def __init__(self, master = None, Title="Application"):
        Frame.__init__(self, master=None)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)

        self.painter1 = Painter(master = self)
        self.painter1.grid(row = 0, column = 0)

        self.painter2 = Painter(master = self)
        self.painter2.grid(row = 0, column = 1)

        adjust(self)        


class Painter(Frame):
    '''Base framed application class'''
    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self['borderwidth'] = 2
        self['relief'] = 'ridge'
        
        if not master:
            self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.create()
        

    def askcolor(self):
        col = colorchooser.askcolor()[1]
        if col:
            self.Canvas.foreground.set(col)
            self.ShowColor['foreground'] = col

   
    def clear(self):
        for item in self.Canvas.find_all():
            self.Canvas.delete(item)

    def save(self):
        filename = filedialog.asksaveasfilename()
        with open(filename, 'w') as f:
            for item in self.Canvas.find_all():
                f.write(f'{self.Canvas.coords(item)}::{self.Canvas.itemcget(item, "fill")}\n')


    def load(self):
        filename =  filedialog.askopenfilename() 
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                cords, col = line.split('::')
                self.Canvas.create_line( eval(cords), fill = col)

    def create(self):
        self.Canvas = MyCanvas(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)

        self.control = Frame(self)
        control = self.control
        control.grid(row=1, column=0, sticky=N+E+S+W)

        self.Save = Button(control, text="Save", command=self.save)
        self.Save.grid(row=0, column=0, sticky=N+E+W)

        self.Load = Button(control, text="Load", command=self.load)
        self.Load.grid(row=0, column=1, sticky=N+E+W)

        self.Clear = Button(control, text = 'Clear', command = self.clear)
        self.Clear.grid(row=0, column=2, sticky=N+E+W)

        self.AskColor = Button(control, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=3, sticky=N+E+W)

        self.ShowColor = Label(control, textvariable=self.Canvas.foreground, foreground = "midnightblue")
        self.ShowColor.grid(row=0, column=4, sticky=N+E+W)

        # tkinter.filedialog


        # self.Quit = Button(control, text="Quit", command=self.quit)
        # self.Quit.grid(row=0, column=2, sticky=N+E+W)

        # self.Swap = Button(control, text = 'Swap', command = self.swap)
        # self.Swap.grid(row=0, column=3, sticky=N+E+W)



        adjust(control, col_val = 0)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 0)
        

           
class MyCanvas(Canvas):
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

    def rightmousedown(self, event):
        '''Store mousedown coords'''
        self.item = self.find_closest(event.x, event.y)
        self.m_x, self.m_y = event.x, event.y
        # print(f'{self.coords(item)}::{self.itemcget(item, "fill")}\n')

    def rightmousemove(self, event):
        if self.item:
            dx = event.x - self.m_x
            dy = event.y - self.m_y
            coords = self.coords(self.item)
            self.coords(self.item, coords[0] + dx, coords[1] + dy,  coords[2] + dx, coords[3] + dy )
            self.m_x, self.m_y = event.x, event.y



    def rightmouseup(self, event):
        self.item = None

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

        self.bind("<Button-3>", self.rightmousedown)
        self.bind("<B3-Motion>", self.rightmousemove)
        self.bind("<ButtonRelease-3>", self.rightmouseup)
    

app = App(Title="Canvas Example")
app.mainloop()
# for item in app.Canvas.find_all():
#     print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))