#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser, filedialog

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
    def askcolor(self):
        color = colorchooser.askcolor()
        self.CanvasLeft.foreground.set(color[1])
        self.CanvasRight.foreground.set(color[1])
        self.Control.ShowColor.configure(bg=color[1])
        if 1 - (0.299 * color[0][0] + 0.587 * color[0][1] + 0.114 * color[0][2]) / 255 < 0.5:
            self.Control.ShowColor.configure(fg="black")
        else:
            self.Control.ShowColor.configure(fg="white")

    def copy(self, CanvasFrom, CanvasTo):
        for line in CanvasFrom.find_all():
            CanvasTo.create_line(CanvasFrom.coords(line),fill=CanvasFrom.itemcget(line, "fill"))

    def clear(self):
        self.CanvasLeft.delete("all")
        self.CanvasRight.delete("all")
    
    def save(self, Canvas):
        fileName = filedialog.asksaveasfilename(filetypes = (("Text file", "*.txt"),))
        if not fileName:
            return
        f = open(fileName, "w")
        for line in Canvas.find_all():
            print(*Canvas.coords(line), Canvas.itemcget(line, "fill"), file=f)
        f.close()

    def load(self, Canvas):
        fileName = filedialog.askopenfilename(filetypes=(("Text file", "*.txt"),))
        if not fileName:
            return
        f = open(fileName, "r")
        for line in f.readlines():
            splittedLine = line.split(" ")
            x1 = splittedLine[0]
            y1 = splittedLine[1]
            x2 = splittedLine[2]
            y2 = splittedLine[3]
            color = splittedLine[4]
            if color[-1] == '\n':
                color = color[:-1]
            Canvas.create_line((x1, y1, x2, y2), fill=color)
        f.close()

    def create(self):
        self.CanvasLeft = Paint(self, foreground="midnightblue")
        self.CanvasLeft.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)

        self.CanvasRight = Paint(self, foreground="midnightblue")
        self.CanvasRight.grid(row=0, column=2, rowspan=3, sticky=N+E+S+W)

        self.Control = Frame()
        self.Control.grid(row=0, column=1, sticky=N+E+S+W)

        self.Control.AskColor = Button(self.Control, text="Color", command=self.askcolor)
        self.Control.AskColor.grid(row=0, column=0, sticky=W+E)

        self.Control.ShowColor = Label(self.Control, textvariable=self.CanvasLeft.foreground, bg="midnightblue", fg="white")
        self.Control.ShowColor.grid(row=1, column=0, sticky=W+E)

        self.Control.Clear = Button(self.Control, text="Clear", command=lambda:self.clear())
        self.Control.Clear.grid(row=2, column=0, sticky=W+E)

        self.Control.CopyLeftToRight = Button(self.Control, text="Copy ->", command=lambda:self.copy(self.CanvasLeft, self.CanvasRight))
        self.Control.CopyLeftToRight.grid(row=3, column=0, sticky=W+E)

        self.Control.CopyRightToLeft = Button(self.Control, text="<- Copy", command=lambda:self.copy(self.CanvasRight, self.CanvasLeft))
        self.Control.CopyRightToLeft.grid(row=4, column=0, sticky=W+E)

        self.Control.SaveLeft = Button(self.Control, text="Save left picture", command=lambda:self.save(self.CanvasLeft))
        self.Control.SaveLeft.grid(row=5, column=0, sticky=W+E)

        self.Control.SaveRight = Button(self.Control, text="Save right picture", command=lambda:self.save(self.CanvasRight))
        self.Control.SaveRight.grid(row=6, column=0, sticky=W+E)

        self.Control.LoadLeft = Button(self.Control, text="Load left picture", command=lambda:self.load(self.CanvasLeft))
        self.Control.LoadLeft.grid(row=7, column=0, sticky=W+E)

        self.Control.LoadRight = Button(self.Control, text="Load right picture", command=lambda:self.load(self.CanvasRight))
        self.Control.LoadRight.grid(row=8, column=0, sticky=W+E)

        self.Control.Quit = Button(self.Control, text="Quit", command=self.quit)
        self.Control.Quit.grid(row=9, column=0, sticky=W+E)

app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.CanvasLeft.find_all():
    print("Left Canvas:\t", *app.CanvasLeft.coords(item), app.CanvasLeft.itemcget(item, "fill"))
for item in app.CanvasRight.find_all():
    print("Right Canvas:\t", *app.CanvasRight.coords(item), app.CanvasRight.itemcget(item, "fill"))

