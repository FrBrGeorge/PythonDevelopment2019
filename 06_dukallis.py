#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

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

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)


class MyApp(App):
    def askcolorLeft(self):
        self.Canvas.foreground.set(colorchooser.askcolor()[1])

    def askcolorRight(self):
        self.CanvasTwo.foreground.set(colorchooser.askcolor()[1])

    def cpLtoR(self):
        for item in self.Canvas.find_all():
            self.CanvasTwo.create_line(self.Canvas.coords(item),fill = app.Canvas.itemcget(item, "fill"))

    def cpRtoL(self):
        for item in self.CanvasTwo.find_all():
            self.Canvas.create_line(self.CanvasTwo.coords(item),fill = app.CanvasTwo.itemcget(item, "fill"))

    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)
        self.CanvasTwo = Paint(self, foreground = "green")
        self.CanvasTwo.grid(row=0, column=2, sticky=N+E+S+W)
        self.Frame = Frame(self, relief = GROOVE, bd = 3)
        self.Frame.grid(row=0, column=1, sticky=N+E+S+W)
        self.Frame.columnconfigure(0, weight=1)
        self.Frame.AskColor = Button(self.Frame, text="Left color", command=self.askcolorLeft)
        self.Frame.AskColor.grid(row=0, column=0, sticky=N+W)
        self.Frame.AskColorTwo = Button(self.Frame, text="Right color", command=self.askcolorRight)
        self.Frame.AskColorTwo.grid(row=0, column=1, sticky=N+E)
        self.Frame.CopyLeft = Button(self.Frame, text="Copy to the right", command=self.cpLtoR)
        self.Frame.CopyLeft.grid(row=1, column=0, sticky=N+W)
        self.Frame.CopyRight = Button(self.Frame, text="Copy to the left", command=self.cpRtoL)
        self.Frame.CopyRight.grid(row=1, column=1, sticky=N+W)
        self.Frame.CleanLeft = Button(self.Frame, text="Clean left")
        self.Frame.CleanLeft.grid(row=2, column=0, sticky=N+W)
        self.Frame.CleanRight = Button(self.Frame, text="Clean right")
        self.Frame.CleanRight.grid(row=2, column=1, sticky=N+E)
        self.Frame.SaveRight = Button(self.Frame, text="Save")
        self.Frame.SaveRight.grid(row=3, column=1, sticky=N+E)
        self.Frame.LoadRight = Button(self.Frame, text="Load")
        self.Frame.LoadRight.grid(row=4, column=1, sticky=N+E)
        self.Frame.Quit = Button(self.Frame, text="Quit", command=self.quit)
        self.Frame.Quit.grid(row=6, column=0, columnspan=2, sticky=S)

app = MyApp(Title="Canvas Example")
app.mainloop()
