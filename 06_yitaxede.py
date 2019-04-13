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
        #for i in range(self.size()[0]):
        #    self.columnconfigure(i, weight=12)
        #for i in range(self.size()[1]):
        #    self.rowconfigure(i, weight=12)
        
class Paint(Canvas):
    '''Canvas with simple drawing'''
    def mousedown(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = self.canvasx(event.x), self.canvasy(event.y)
        self.cursor = None

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        x, y = self.canvasx(event.x), self.canvasy(event.y)
        self.cursor = self.create_line((self.x0, self.y0, x, y), fill=self.foreground.get())

    def mouseup(self, event):
        '''Dragging is done'''
        self.cursor = None
        
    def rightmousedown(self, event):
        '''Store rightmousedown coords'''
        self.rx0, self.ry0 = self.canvasx(event.x), self.canvasy(event.y)
        self.moving = self.find_closest(self.canvasx(event.x), self.canvasy(event.y))

    def rightmousemove(self, event):
        '''Do sometheing when drag a mouse with the right button pressed'''
        if self.moving:
            x, y = self.canvasx(event.x), self.canvasy(event.y)
            self.move(self.moving, x - self.rx0, y - self.ry0)
            self.rx0, self.ry0 = x, y

    def rightmouseup(self, event):
        '''Dragging is done'''
        self.moving = None

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)
        self.bind("<Button-3>", self.rightmousedown)
        self.bind("<B3-Motion>", self.rightmousemove)
        self.bind("<ButtonRelease-3>", self.rightmouseup)

class MyApp(App):
    def askcolor(self):
        clr = colorchooser.askcolor()[1]
        if clr:
            self.Canvas.foreground.set(clr)
            self.ShowColor['bg'] = clr

    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)
        self.ctrlFrame = Frame(self)
        self.ctrlFrame.grid(row=0, column=1)
        self.AskColor = Button(self.ctrlFrame, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=0, sticky=E+W)
        self.ShowColor = Label(self.ctrlFrame, textvariable=self.Canvas.foreground, height=2, bg=self.Canvas.foreground.get())
        self.ShowColor.grid(row=1, column=0, sticky=N+W+E)
        self.Clear = Button(self.ctrlFrame, text="Clear", command=lambda:self.Canvas.delete(ALL))
        self.Clear.grid(row=2, column=0, sticky=E+W)
        self.SaveAs = Button(self.ctrlFrame, text="Save as...", command=self.save_as)
        self.SaveAs.grid(row=4, column=0, sticky=E+W)
        self.Open = Button(self.ctrlFrame, text="Open...", command=self.read_from)
        self.Open.grid(row=5, column=0, sticky=E+W)
        
        
    def adjust(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
    def save_as(self):
        name = filedialog.asksaveasfilename(initialfile="canvas.cnv", defaultextension=".cnv", filetypes=[("Canvas Documents","*.cnv")])
        if name:
            file = open(name, 'w')
            for id in self.Canvas.find_all():
                file.write(f'{self.Canvas.coords(id)}, \"{self.Canvas.itemcget(id, "fill")}\"\n')
                
    def read_from(self):
        name = filedialog.askopenfilename(filetypes=[("Canvas Documents","*.cnv")])
        if name:
            self.Canvas.delete(ALL)
            file = open(name, 'r')
            for line in file:
                if len(line) <= 2:
                    break
                coords, clr = eval(line)
                self.Canvas.create_line(*coords, fill=clr)
            
        
class DoubleApp(Frame):
    def __init__(self, master=None, Title="Double Application"):
        Frame.__init__(self, master)
        self.master.title(Title)
        self.grid(row=0, column=0, sticky=N+W+E+S)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.app1 = MyApp(self)
        self.app2 = MyApp(self)
         
        self.mButton1 = Button(self.app1.ctrlFrame, text="To the other", command=self.first_to_second)
        self.mButton1.grid(row=3, column=0, sticky=E+W)
        self.mButton2 = Button(self.app2.ctrlFrame, text="To the other", command=self.second_to_first)
        self.mButton2.grid(row=3, column=0, sticky=E+W)
        
        self.ctrlFrame = Frame(self)
        self.ctrlFrame.grid(sticky=N+S+W+E)
        self.qButton = Button(self.ctrlFrame, text="Quit", command=self.quit)
        self.qButton.grid(row=0, column=3, sticky=E+W)
        
    def first_to_second(self):
        for id in self.app1.Canvas.find_all():
            self.app2.Canvas.create_line(*self.app1.Canvas.coords(id), fill=self.app1.Canvas.itemcget(id, "fill"))
            self.app1.Canvas.delete(id)
        
    def second_to_first(self):
        for id in self.app2.Canvas.find_all():
            self.app1.Canvas.create_line(*self.app2.Canvas.coords(id), fill=self.app2.Canvas.itemcget(id, "fill"))
            self.app2.Canvas.delete(id)

        

app = DoubleApp(Title="Double Canvas Example")
app.mainloop()

