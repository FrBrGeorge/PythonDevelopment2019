from tkinter import *

class CanvasPanel(Canvas):
    # CanvasPanel class is a wrapper of Canvas class of tkinter
    def _Button_1(self, event):
        self._canvasToolPanel.canvasButton_1(self, event)
    def _B1_Motion(self, event):   
        self._canvasToolPanel.canvasB1_Motion(self, event)
    def _ButtonRelease_1(self, event):   
        self._canvasToolPanel.canvasButtonRelease_1(self, event)
    def __init__(self, master=None, canvasTools=None, *ap, **an):
        Canvas.__init__(self, master, *ap, **an)
        self._canvasToolPanel = canvasTools
        self.bind("<Button-1>", self._Button_1)
        self.bind("<B1-Motion>", self._B1_Motion)
        self.bind("<ButtonRelease-1>", self._ButtonRelease_1)
        # self.bind("<Button-3>", )
        # self.bind("<B3-Motion>", )
        # self.bind("<ButtonRelease-3>", )