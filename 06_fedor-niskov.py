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

class MyApp(App):
    def askcolor(self):
        self.Canvas.foreground.set(colorchooser.askcolor()[1])

    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)
        self.ControlPanel = Frame(self)
        self.ControlPanel.grid(row=0, column=1, sticky=N+E+S+W)
        self.ControlPanel.AskColor = Button(self.ControlPanel, text="Color", command=self.askcolor)
        self.ControlPanel.AskColor.grid(row=0, column=0, sticky=W+E)
        self.ControlPanel.ShowColor = Label(self.ControlPanel, textvariable=self.Canvas.foreground)
        self.ControlPanel.ShowColor.grid(row=1, column=0, sticky=W+E)
        self.ControlPanel.Quit = Button(self.ControlPanel, text="Quit", command=self.quit)
        self.ControlPanel.Quit.grid(row=2, column=0, sticky=W+E)

    def adjust(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        for i in range(self.ControlPanel.size()[1]):
            self.ControlPanel.rowconfigure(i, weight=0)
        self.ControlPanel.columnconfigure(0, weight=1)


app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item))
    print(app.Canvas.itemcget(item, "fill"))

