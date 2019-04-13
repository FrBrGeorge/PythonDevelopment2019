from tkinter import *

class CanvasPanel(Canvas):
    # CanvasPanel class is a wrapper of Canvas class of tkinter
    def __init__(self, master=None, *ap, **an):
        Canvas.__init__(self, master, *ap, **an)
        
    def _get_item(self, event):
        self.x0, self.y0 = event.x, event.y 
        self.item = self.find_closest(event.x, event.y)

    def _drag_item(self, event):
        self.move(self.item, event.x - self.x0, event.y - self.y0)
        self.x0, self.y0 = event.x, event.y 

    def _put_item(self, event):
        self.item = None            