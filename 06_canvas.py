#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *

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

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        l=self.create_line((self.x0, self.y0, event.x, event.y))
        print(l)

    def mouseup(self, event):
        '''Dragging is done'''
        print(self.find_all())

    def __init__(self, master=None):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

class MyApp(App):
    def create(self):
        self.Canvas = Paint(self)
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)
        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=0, column=1, sticky=N+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
