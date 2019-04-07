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
        self._create()
        self._adjust()

    def _create(self):
        '''Create all the widgets'''
        self.bQuit = Button(self, text='Quit', command=self.quit)
        self.bQuit.grid()

    def _adjust(self):
        '''Adjust grid sise/properties'''
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)
        
class CanvasPanel(Canvas):
    '''Canvas with simple drawing'''
    def _mousedown(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def _mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def _mouseup(self, event):
        '''Dragging is done'''
        self.cursor = None
        #print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self._mousedown)
        self.bind("<B1-Motion>", self._mousemove)
        self.bind("<ButtonRelease-1>", self._mouseup)

class WorkSpace(App):
    def _create(self):
        self._canvasPanel = CanvasPanel(self, foreground="midnightblue")
        self._canvasPanel.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)        
        self._canvasTools = CanvasToolPanel(self, self._canvasPanel)
        self._canvasTools.grid(row=0, column=1, rowspan=3, sticky=N+E+S+W)
    
    def printCanvasObjects(self):
        for item in self._canvasPanel.find_all():
            print(*self._canvasPanel.coords(item), self._canvasPanel.itemcget(item, "fill"))

class CanvasToolPanel(Frame):
    def __init__(self, root, canvasPanel):
        Frame.__init__(self, root)
        self._canvasPanel = canvasPanel
        self._askColor = Button(self, text="Color", command=self._askcolor)
        self._askColor.grid(row=0, column=0, sticky=N+W)
        self._showColor = Label(self, textvariable=self._canvasPanel.foreground)
        self._showColor.grid(row=1, column=0, sticky=N+W+E)
        self._quit = Button(self, text="Quit", command=root.quit)
        self._quit.grid(row=2, column=0, sticky=N+W)

    def _askcolor(self):
        self.Canvas.foreground.set(colorchooser.askcolor()[1])


app = WorkSpace(Title="Canvas Example")
app.mainloop()
app.printCanvasObjects()

