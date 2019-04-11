#!/usr/bin/env python3
'''
Пример объектной организации кода
'''
import abc
from collections import namedtuple
PanelCoords = namedtuple("PanelCoords", ["row", "column", "rowspan", "columnspan"])

from tkinter import *
from tkinter import colorchooser

from MikhailVMK_CanvasPanel import CanvasPanel
from MikhailVMK_CanvasToolPanel import CanvasToolPanel
from MikhailVMK_Binding import ForwardFunction


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
        # WorkSpace object is an aggragation of MiscPanel objects, CanvasPanel objects, Action objects
        # for now WorkSpace object contains a single ToolPanel object and two CanvasPanel objects
        self._canvasToolPanelCoords = PanelCoords(row=0, column=1, rowspan = 3, columnspan = 1) 
        self._canvasToolPanel = CanvasToolPanel(self)
        self._canvasToolPanel.grid(row=self._canvasToolPanelCoords.row,
                            column=self._canvasToolPanelCoords.column,
                            rowspan=self._canvasToolPanelCoords.rowspan,
                            columnspan=self._canvasToolPanelCoords.columnspan,
                            sticky=N+E+S+W)        
        self._canvasPanelCoords = PanelCoords(row=0, column=0, rowspan = 3, columnspan = 1)
        # self._canvasPanel = CanvasPanel(self, self._canvasToolPanel)
        self._canvasPanel = Canvas(self)
        self._canvasPanel.grid(row=self._canvasPanelCoords.row,
                            column=self._canvasPanelCoords.column,
                            rowspan=self._canvasPanelCoords.rowspan,
                            columnspan=self._canvasPanelCoords.columnspan,
                            sticky=N+E+S+W)
        # self._canvasPanel['borderwidth'] = 2
        # self._canvasPanel['relief'] = 'ridge'
        # self._canvasPanel1Coords = PanelCoords(row=4, column=0, rowspan = 3, columnspan = 1)
        # self._canvasPanel1 = CanvasPanel(self, self._canvasToolPanel)
        # self._canvasPanel1.grid(row=self._canvasPanel1Coords.row,
        #                     column=self._canvasPanel1Coords.column,
        #                     rowspan=self._canvasPanel1Coords.rowspan,
        #                     columnspan=self._canvasPanel1Coords.columnspan,
        #                     sticky=N+E+S+W)
        # self._canvasPanel1['borderwidth'] = 2
        # self._canvasPanel1['relief'] = 'ridge'
        self._createBindings()
    def _adjust(self):
        self.rowconfigure(0, weight=12)
        self.columnconfigure(0, weight=12)
        self.columnconfigure(1, weight=0)
    def _createBindings(self):
        self._canvasPanel.bind('<Button-1>',
                                ForwardFunction(self._canvasPanel,
                                                handler = self._canvasToolPanel,
                                                method ='initiateDraw'))
        self._canvasPanel.bind('<B1-Motion>',
                                ForwardFunction(self._canvasPanel,
                                                handler = self._canvasToolPanel,
                                                method ='progressDraw'))
        self._canvasPanel.bind('<ButtonRelease-1>',
                                ForwardFunction(self._canvasPanel,
                                                handler = self._canvasToolPanel,
                                                method ='terminateDraw'))   


    def printCanvasObjects(self):
        for item in self._canvasPanel.find_all():
            # print(self._canvasPanel.itemconfigure(item))
            print(*self._canvasPanel.coords(item))


app = WorkSpace(Title="Canvas Example")
app.mainloop()
# app.printCanvasObjects()