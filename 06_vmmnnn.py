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
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get(), tag="line")
       # self.elem.append(self.cursor)

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


class Paint2(Canvas):
    '''Canvas with simple drawing'''

    def mousedown(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_oval((self.x0, self.y0, event.x, event.y), fill=self.foreground.get(), tag="oval")
        #self.elem2.append(self.cursor)

    def mouseup(self, event):
        '''Dragging is done'''
        self.cursor = None
        # print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)


class MyApp(App):
    def askcolor(self):
        c = colorchooser.askcolor()[1]
        if (c):             # Cancel gives None
            self.Canvas.foreground.set(c)
            self.Frame.AskColor.configure(bg=c)

    def askcolor2(self):
        c = colorchooser.askcolor()[1]
        if (c):             # Cancel gives None
            self.Canvas2.foreground.set(c)
            self.Frame.AskColor2.configure(bg=c)

    def CopyUp(self):
        for item in self.Canvas2.find_withtag("oval"):
            self.Canvas.create_oval(self.Canvas2.coords(item),fill = app.Canvas2.itemcget(item, "fill"), tag="oval")

    def CopyDown(self):
        for item in self.Canvas.find_withtag("line"):
            self.Canvas2.create_line(self.Canvas.coords(item),fill = app.Canvas.itemcget(item, "fill"), tag="line")

    def CleanUp(self):
        self.Canvas.delete(ALL)

    def CleanDown(self):
        self.Canvas2.delete(ALL)

    def create(self):

        self.Canvas = Paint(self, foreground="blue")
        self.Canvas.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)

        self.Frame = Frame(self)
        self.Frame.grid(row=0, column=1, sticky=N+E+S+W)
        self.Frame.columnconfigure(0, weight=1)

        self.Frame.AskColor = Button(self.Frame, textvariable=self.Canvas.foreground, command=self.askcolor)
        self.Frame.AskColor.grid(row=0, column=0, sticky=N+W)

        self.Frame.CopyUp = Button(self.Frame, text="Copy up", command=self.CopyUp)
        self.Frame.CopyUp.grid(row=10, column=0, sticky=N+W)

        self.Frame.CleanUp = Button(self.Frame, text="Clean up", command=self.CleanUp)
        self.Frame.CleanUp.grid(row=15, column=0, sticky=N + W)



        self.Canvas2 = Paint2(self, foreground="blue")
        self.Canvas2.grid(row=25, column=0, rowspan=3, sticky=N+E+S+W)

        self.Frame.AskColor2 = Button(self.Frame, textvariable=self.Canvas2.foreground, command=self.askcolor2)
        self.Frame.AskColor2.grid(row=20, column=0, sticky=N+W)

        self.Frame.CopyDown = Button(self.Frame, text="Copy down", command=self.CopyDown)
        self.Frame.CopyDown.grid(row=25, column=0, sticky=N+W)

        self.Frame.CleanDown = Button(self.Frame, text="Clean down", command=self.CleanDown)
        self.Frame.CleanDown.grid(row=30, column=0, sticky=N + W)

        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=27, column=1, sticky=N+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))

