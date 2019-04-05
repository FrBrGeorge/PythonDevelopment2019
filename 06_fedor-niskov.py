#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

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
        #print(self.find_all())

    def mouseselect(self, event):
        if self.selected != None:
            self.itemconfig(self.selected, dash=())
            self.selected = None
        else:
            line = self.find_closest(event.x, event.y)
            self.itemconfig(line, dash=(4,4))
            self.selected = line

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        self.selected = None
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)
        self.bind("<Button-3>", self.mouseselect)

class MyApp(App):
    def askcolor(self):
        color = colorchooser.askcolor()
        self.Canvas.foreground.set(color[1])
        self.Canvas2.foreground.set(color[1])
        self.ControlPanel.ShowColor.configure(bg=color[1])

    def copy(self, CanvasDst, CanvasSrc):
        s = CanvasSrc.selected
        if s == None:
            lines = CanvasSrc.find_all()
        else:
            lines = [s]
            CanvasSrc.itemconfig(s, dash=())
            CanvasSrc.selected = None
        for i in lines:
            CanvasDst.create_line(
                CanvasSrc.coords(i),
                fill=CanvasSrc.itemcget(i, "fill")
            )

    def clear(self, canvas):
        for i in canvas.find_all():
            canvas.delete(i)

    def save(self):
        filename = filedialog.asksaveasfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (("text file", "*.txt"),)
        )
        if not filename:
            return
        with open(filename, "w") as f:
            cs = self.Canvas
            for i in cs.find_all():
                for c in cs.coords(i):
                    f.write(str(c) + " ")
                f.write(cs.itemcget(i, "fill") + "\n")

    def load(self):
        filename = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (("text file", "*.txt"),)
        )
        if not filename:
            return
        with open(filename, "r") as f:
            for l in f.readlines():
                l = l.split()
                coords = tuple(float(c) for c in l[:4])
                color = l[4]
                self.Canvas.create_line(coords, fill=color)

    def create(self):

        init_color = "midnightblue"

        self.Canvas = Paint(self, foreground=init_color)
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)

        self.ControlPanel = Frame(self)
        self.ControlPanel.grid(row=0, column=1, sticky=N+E+S+W)

        self.ControlPanel.AskColor = Button(self.ControlPanel, text="Color", command=self.askcolor)
        self.ControlPanel.AskColor.grid(row=0, column=0, sticky=W+E)

        self.ControlPanel.ShowColor = Label(self.ControlPanel, textvariable=self.Canvas.foreground)
        self.ControlPanel.ShowColor.grid(row=1, column=0, sticky=W+E)
        self.ControlPanel.ShowColor.configure(bg=init_color)

        self.ControlPanel.Quit = Button(self.ControlPanel, text="Quit", command=self.quit)
        self.ControlPanel.Quit.grid(row=2, column=0, sticky=W+E)

        self.ControlPanel.CopyL = Button(self.ControlPanel, text="<",
            command = lambda : self.copy(self.Canvas, self.Canvas2))
        self.ControlPanel.CopyL.grid(row=3, column=0, sticky=W+E)

        self.ControlPanel.CopyR = Button(self.ControlPanel, text=">",
            command = lambda : self.copy(self.Canvas2, self.Canvas))
        self.ControlPanel.CopyR.grid(row=4, column=0, sticky=W+E)

        self.ControlPanel.Clear = Button(self.ControlPanel, text="Clear Left",
            command = lambda : self.clear(self.Canvas))
        self.ControlPanel.Clear.grid(row=5, column=0, sticky=W+E)

        self.ControlPanel.Clear2 = Button(self.ControlPanel, text="Clear Right",
            command = lambda : self.clear(self.Canvas2))
        self.ControlPanel.Clear2.grid(row=6, column=0, sticky=W+E)

        self.ControlPanel.Quit = Button(self.ControlPanel, text="Save...", command=self.save)
        self.ControlPanel.Quit.grid(row=7, column=0, sticky=W+E)

        self.ControlPanel.Quit = Button(self.ControlPanel, text="Load...", command=self.load)
        self.ControlPanel.Quit.grid(row=8, column=0, sticky=W+E)

        self.Canvas2 = Paint(self, foreground=init_color)
        self.Canvas2.grid(row=0, column=2, sticky=N+E+S+W)

    def adjust(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        for i in range(self.ControlPanel.size()[1]):
            self.ControlPanel.rowconfigure(i, weight=0)
        self.ControlPanel.columnconfigure(0, weight=1)


app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item))
    print(app.Canvas.itemcget(item, "fill"))

