import abc
from tkinter import *
from tkinter import colorchooser
used_options = [
    
]

class Tool(Label, metaclass=abc.ABCMeta):
    def canvasMouseDown(self, canvasPanel,  color, event):
        pass
    def canvasMouseMove(self, canvasPanel,  color, event):
        pass
    def canvasMouseUp(self, canvasPanel,  color, event):
        pass
    def __init__(self, root):
        Label.__init__(self, root)
        self._toolPanel = root      
        self.bind("<Button-1>", self._mousedown) 
    def _mousedown(self, event):
        self._toolPanel.toolMouseDown(self)

class Line(Tool):
    def __init__(self, root):
        Tool.__init__(self, root)
        self.configure(text='Line')
    def canvasMouseDown(self, canvasPanel, color, event):
        '''Store mousedown coords'''
        canvasPanel.x0, canvasPanel.y0 = event.x, event.y
        canvasPanel.cursor = None 
    def canvasMouseMove(self, canvasPanel, color, event):
        '''Do sometheing when drag a mouse'''
        if canvasPanel.cursor:
            canvasPanel.delete(canvasPanel.cursor)
        canvasPanel.cursor = self.createObject(canvasPanel,(canvasPanel.x0,canvasPanel.y0,event.x,event.y), color)
    def canvasMouseUp(self, canvasPanel, color, event):
        '''Dragging is done'''
        canvasPanel.cursor = None
    def createObject(self, canvasPanel, coords, color):
        return canvasPanel.create_line(coords, fill = color, tag = self["text"])  

# class Rectangle(Tool):
#     def __init__(self, root):
#         Tool.__init__(self, root)
#         self.configure(text='Rectangle')
#     def canvasMouseDown(self, canvasPanel, color, event):
#         canvasPanel.x0, canvasPanel.y0 = event.x, event.y
#         canvasPanel.cursor = None 
#     def canvasMouseMove(self, canvasPanel, color, event):
#         if canvasPanel.cursor:
#             canvasPanel.delete(canvasPanel.cursor)
#         canvasPanel.cursor = canvasPanel.create_rectangle((canvasPanel.x0, canvasPanel.y0, event.x, event.y),
#                                                     fill=color,
#                                                     width=0,
#                                                     tag = "Rectangle")
#     def canvasMouseUp(self, canvasPanel, color, event):
#         canvasPanel.cursor = None

class Find(Tool):
    def __init__(self, master, itembuffer):
        Tool.__init__(self, master)
        self._itembuffer = itembuffer
        self.configure(text='Find')

    def canvasMouseDown(self, canvasPanel, color, event):
        self._itembuffer.clear() 
        item = canvasPanel.find_closest(event.x, event.y)
        if len(item) == 0:
            return
        # print(item, canvasPanel.itemcget(item, 'fill'))
        itemOptions = canvasPanel.itemconfigure(item)
        itemTag = itemOptions['tags'][4]
        itemColor = itemOptions['fill'][4]
        itemCoords = canvasPanel.coords(item)
        print(itemTag, itemColor, itemCoords)
        self._itembuffer.append((itemTag, itemCoords, itemColor))

class FindAll(Tool):
    def __init__(self, master, itembuffer):
        Tool.__init__(self, master)
        self._itembuffer = itembuffer
        self.configure(text='FindAll')

    def canvasMouseDown(self, canvasPanel, color, event):
        self._itembuffer.clear() 
        items = canvasPanel.find_all()
        if len(items) == 0:
            return
        for item in items:
            itemOptions = canvasPanel.itemconfigure(item)
            itemTag = itemOptions['tags'][4]
            itemColor = itemOptions['fill'][4]
            itemCoords = canvasPanel.coords(item)
            self._itembuffer.append((itemTag, itemCoords, itemColor))

class Insert(Tool):
    def __init__(self, master, itembuffer, tools):
        Tool.__init__(self, master)
        self._itembuffer = itembuffer
        self._tools = tools
        self.configure(text='Insert')

    def canvasMouseDown(self, canvasPanel, color, event):
        for entry in self._itembuffer:
            itemTag = entry[0]
            itemCoords = entry[1]
            itemColor = entry[2]
            for tool in self._tools:
                if tool['text'] == itemTag:
                    tool.createObject(canvasPanel, itemCoords, itemColor)
                    break
