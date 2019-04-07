#!/usr/bin/env python3
'''
Пример объектной организации кода
'''
from collections import namedtuple
PanelCoords = namedtuple("PanelCoords", ["row", "column", "rowspan", "columnspan"])

from _tkinter import TclError
from tkinter import *
from tkinter import colorchooser

from RgbNamedColors import Colors

def encodedColorValid(encodedColor):
    if not isinstance(encodedColor, str):
        return False
    if encodedColor in Colors.keys():
        return True
    if len(encodedColor) != 7:
        return False
    if encodedColor[0] != "#":
        return False
    for char in encodedColor[1:]:
        if not char.isdigit() and not char in "abcdefABCDEF":
            return False
    return True

def decodedColorValid(decodedColor):
    if not isinstance(decodedColor, tuple):
        return False
    if len(decodedColor) != 3:
        return False
    for color in decodedColor:
        if not isinstance(color, int):
            return False
        if color < 0 or color > 255:
            return False
    return True             

def getContrastColor(decodedColor):
    assert decodedColorValid(decodedColor)
    return ((decodedColor[0] + 128) % 256, (decodedColor[1] + 128) % 256, (decodedColor[2] + 128) % 256)

def encodeColor(decodedColor):
    assert decodedColorValid(decodedColor)
    colorString = "#"
    for i in range(0, len(decodedColor)):
        color = format(decodedColor[i], 'x')
        if len(color) == 1:
            colorString += '0'
        colorString += color    
    return colorString

def decodeColor(encodedColor):
    assert encodedColorValid(encodedColor)
    if encodedColor in Colors.keys():
        r = int(Colors[encodedColor][0])
        g = int(Colors[encodedColor][1])
        b = int(Colors[encodedColor][2])  
    else:      
        r = int(encodedColor[1:3], 16)
        g = int(encodedColor[3:5], 16)
        b = int(encodedColor[5:7], 16)
    return r, g, b

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

class WorkSpace(App):
    def _create(self):
        self._canvasToolsCoords = PanelCoords(row=0, column=1, rowspan = 3, columnspan = 1) 
        self._canvasTools = CanvasToolPanel(self)
        self._canvasTools.grid(row=self._canvasToolsCoords.row,
                            column=self._canvasToolsCoords.column,
                            rowspan=self._canvasToolsCoords.rowspan,
                            columnspan=self._canvasToolsCoords.columnspan,
                            sticky=N+E+S+W)        
        self._canvasPanelCoords = PanelCoords(row=0, column=0, rowspan = 3, columnspan = 1)
        self._canvasPanel = CanvasPanel(self, self._canvasTools)
        self._canvasPanel.grid(row=self._canvasPanelCoords.row,
                            column=self._canvasPanelCoords.column,
                            rowspan=self._canvasPanelCoords.rowspan,
                            columnspan=self._canvasPanelCoords.columnspan,
                            sticky=N+E+S+W) 
    def _adjust(self):
        self.rowconfigure(0, weight=12)
        self.columnconfigure(0, weight=12)
        self.columnconfigure(1, weight=0)


    def printCanvasObjects(self):
        for item in self._canvasPanel.find_all():
            print(*self._canvasPanel.coords(item), self._canvasPanel.itemcget(item, "fill"))

        
class CanvasPanel(Canvas):
    '''Canvas with simple drawing'''
    def _mousedown(self, event):
        self._canvasTools.mousedown(self, event)
    def _mousemove(self, event):   
        self._canvasTools.mousemove(self, event)
    def _mouseup(self, event):   
        self._canvasTools.mouseup(self, event)

    def __init__(self, master=None, canvasTools=None, *ap, **an):
        Canvas.__init__(self, master, *ap, **an)
        self._canvasTools = canvasTools
        self.bind("<Button-1>", self._mousedown)
        self.bind("<B1-Motion>", self._mousemove)
        self.bind("<ButtonRelease-1>", self._mouseup)

class CanvasToolPanel(Frame):
    def __init__(self, root, color='black'):
        Frame.__init__(self, root)
        self['borderwidth'] = 2
        self['relief'] = 'raised'
        self._toolColor = StringVar()
        self._toolColor.set(color)
        self._askColor = Button(self, text="Color", command=self._askcolor)
        self._askColor.grid(row=0, column=0, sticky=N+W)
        self._showColor = Entry(self,
                            textvariable=self._toolColor,
                            background =self._toolColor.get(),
                            foreground = encodeColor(getContrastColor(decodeColor(color))),
                            validatecommand = (self.register(decodedColorValid), '%P'),
                            validate='key')
        self._showColor.grid(row=1, column=0, sticky=N+W+E)
        self._quit = Button(self, text="Quit", command=root.quit)
        self._quit.grid(row=2, column=0, sticky=N+W)

    def _askcolor(self):
        color = colorchooser.askcolor(color = self._toolColor.get())[1]
        self._toolColor.set(color)
        self._showColor.config(background = color)
        self._showColor.config(foreground = encodeColor(getContrastColor(decodeColor(color))))
    
    def mousedown(self, canvasPanel, event):
        '''Store mousedown coords'''
        canvasPanel.x0, canvasPanel.y0 = event.x, event.y
        canvasPanel.cursor = None 
    def mousemove(self, canvasPanel, event):
        '''Do sometheing when drag a mouse'''
        if canvasPanel.cursor:
            canvasPanel.delete(canvasPanel.cursor)
        canvasPanel.cursor = canvasPanel.create_line((canvasPanel.x0, canvasPanel.y0, event.x, event.y), fill=self._toolColor.get())

    def mouseup(self, canvasPanel, event):
        '''Dragging is done'''
        canvasPanel.cursor = None
        

app = WorkSpace(Title="Canvas Example")
app.mainloop()
app.printCanvasObjects()
