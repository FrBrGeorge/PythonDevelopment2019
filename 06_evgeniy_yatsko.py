#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser

class App(Frame):
    '''Base framed application class'''
    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.create()
        self.adjust()

    def create(self):
        '''Create all the widgets'''
        self.bQuit = Button(self, text='Quit', command=self.quit)
        self.bQuit.grid()

    def adjust(self):
        '''Adjust grid sise/properties'''
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)
        
class Paint(Canvas):
    '''Canvas with simple drawing'''
    def mousedown(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None
        self.anotherOne.cursor = None

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        if self.anotherOne.cursor:
            self.anotherOne.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())
        self.anotherOne.cursor = self.anotherOne.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
        '''Dragging is done'''
        self.anotherOne.cursor = None
        self.cursor = None
        #print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

        self.anotherOne = None

class MyApp(App):
    def askcolor(self):
        color = colorchooser.askcolor()[1]
        self.Canvas.foreground.set(color)
        self.Canvas2.foreground.set(color)
        self.ShowColor.config(fg = color)
    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)

        self.Canvas2 = Paint(self, foreground="midnightblue")
        self.Canvas2.grid(row = 3, column = 0, rowspan=3, sticky=N+E+S+W)

        self.Canvas.anotherOne = self.Canvas2
        self.Canvas2.anotherOne = self.Canvas

        self.Frame = Frame(self)
        self.Frame.grid(row = 0, column = 1, sticky = N+W)

        self.AskColor = Button(self.Frame, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=1, sticky=N+W)
        
        self.ShowColor = Label(self.Frame, textvariable=self.Canvas.foreground, fg = self.Canvas.foreground.get())
        self.ShowColor.grid(row=1, column=1, sticky=N+W)
        
        self.Quit = Button(self.Frame, text="Quit", command=self.quit)
        self.Quit.grid(row=2, column=1, sticky=N+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))

