import abc
from tkinter import *

from MikhailVMK_ColorPalet import ColorPalet
from MikhailVMK_Binding import ForwardFunction

class CanvasTool(Label, metaclass=abc.ABCMeta):
    def initiateDraw(self, canvasPanel,  colorPalet, event):
        pass
    def progressDraw(self, canvasPanel,  colorPalet, event):
        pass
    def terminateDraw(self, canvasPanel,  colorPalet, event):
        pass
    def __init__(self, root):
        Label.__init__(self, root)
        self['relief'] = 'raised'        
    def select(self):
        self['relief'] = 'sunken'
    def deselect(self):
        self['relief'] = 'raised'        

class Line(CanvasTool):
    def __init__(self, root):
        CanvasTool.__init__(self, root)
        self.configure(text='Line')
    def initiateDraw(self, canvasPanel, event):
        '''Store mouse coords'''
        canvasPanel.x0, canvasPanel.y0 = event.x, event.y
        canvasPanel.cursor = None 
    def progressDraw(self, canvasPanel, colorPalet, event):
        '''Do sometheing when drag a mouse'''
        if canvasPanel.cursor:
            canvasPanel.delete(canvasPanel.cursor)
        canvasPanel.cursor = self.createObject(canvasPanel,
                                            (canvasPanel.x0, canvasPanel.y0, event.x, event.y),
                                            colorPalet.getColor())
    def terminateDraw(self, canvasPanel, event):
        '''Dragging is done'''
        canvasPanel.cursor = None
    def createObject(self, canvasPanel, coords, color):
        ret = canvasPanel.create_line(coords, fill = color, tag = self["text"])
        return ret  

class CanvasToolPanel(Frame):
    def __init__(self, root, color='black'):
        Frame.__init__(self, root)
        self['borderwidth'] = 2
        self['relief'] = 'ridge'

        self._quit = Button(self, text="Quit", command=root.quit)
        self._quit.grid(row=0, column=0, sticky=N+W)
        
        self._colorPalet = ColorPalet(self)
        self._colorPalet.grid(row=1, column=0, sticky=N+W)
        
        self._tools = []
        self._tools.append(Line(self))
        self._tools.append(Line(self))        
        self._selected = None
        
        self._createBindings()
        self._layoutTools()

    def _createBindings(self):
        for tool in self._tools:
            tool.bind('<Button-1>', ForwardFunction(tool, handler = self, method = '_select'))
     
    def _layoutTools(self):
        for tool in self._tools:
            tool.grid(row=self.grid_size()[1], column=0, sticky=N+W)
            tool['borderwidth'] = 2

    def initiateDraw(self, canvasPanel, event):
        if self._selected is not None:
            self._selected.initiateDraw(canvasPanel, event)

    def progressDraw(self, canvasPanel, event):
        if self._selected is not None:
            self._selected.progressDraw(canvasPanel, self._colorPalet, event)
    def terminateDraw(self, canvasPanel, event):
        if self._selected is not None:
            self._selected.terminateDraw(canvasPanel, event)
    
    def _deselect(self, event):
        if self._selected is not None:
            self._selected.deselect()
            self._selected = None
    def _select(self, tool, event):
        self._deselect(event)
        self._selected = tool
        tool.select()