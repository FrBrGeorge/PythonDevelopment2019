#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

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
        '''Adjust grid size/properties'''
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)
        
class Paint(Canvas):
    '''Canvas with simple drawing'''
    def mousedown1(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove1(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())
     
    def mouseup1(self, event):
        '''Dragging is done'''
        self.cursor = None

    def mousedown3(self, event):
        self.mov = self.find_closest(event.x, event.y, halo = 15)
        if self.mov:
            self.cds = self.coords(self.mov)
            self.x3, self.y3 = event.x, event.y

    def mousemove3(self, event):
        if self.mov:
            self.coords(self.mov, (self.cds[0] - (self.x3 - event.x)), (self.cds[1] - (self.y3 - event.y)), (self.cds[2] - (self.x3 - event.x)), (self.cds[3] - (self.y3 - event.y)))
            
    def mouseup3(self, event):
        self.mov = None
        

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown1)
        self.bind("<B1-Motion>", self.mousemove1)
        self.bind("<ButtonRelease-1>", self.mouseup1)
        self.bind("<Button-3>", self.mousedown3)
        self.bind("<B3-Motion>", self.mousemove3)
        self.bind("<ButtonRelease-3>", self.mouseup3)
        

class MyApp(App):
    def askcolor1(self):
        ret = colorchooser.askcolor()[1]
        if (ret != None):
            self.Canvas1.foreground.set(ret)
            self.Frame.ShowColor1.configure(bg = self.Canvas1.foreground.get())
    
    def askcolor2(self):
        ret = colorchooser.askcolor()[1]
        if (ret != None):
            self.Canvas2.foreground.set(ret)
            self.Frame.ShowColor2.configure(bg = self.Canvas2.foreground.get())

    def Copy1to2(self):
        for item in self.Canvas1.find_all():
            self.Canvas2.create_line(self.Canvas1.coords(item),fill = app.Canvas1.itemcget(item, "fill"))
    def Copy2to1(self):
        for item in self.Canvas2.find_all():
            self.Canvas1.create_line(self.Canvas2.coords(item),fill = app.Canvas2.itemcget(item, "fill"))

    def Clean1(self):
        self.Canvas1.delete(ALL)
    def Clean2(self):
        self.Canvas2.delete(ALL)

    def Save(self):
        filename = asksaveasfilename(filetypes = [("TXT files", "*.TXT")], defaultextension = ".TXT", initialfile = "cizlota.TXT", initialdir = os.getcwd())
        if (filename != ''):
            f = open(filename, 'w')
            for item in self.Canvas1.find_all():
                for coord in self.Canvas1.coords(item):
                    f.write(f'{coord} ')
                f.write(f'{app.Canvas1.itemcget(item, "fill")}\n')
            f.close()

    def Load(self):
        filename = askopenfilename(filetypes = [("TXT files", "*.TXT")], initialdir = os.getcwd())
        if (filename != ''):
            self.Canvas1.delete(ALL)
            f = open(filename, 'r')
            for line in f:
                c = line.split()
                self.Canvas1.create_line([float(c[0]), float(c[1]), float(c[2]), float(c[3])], fill = c[4])
            f.close()

    def create(self):
        self.columnconfigure(0, weight = 10)
        self.columnconfigure(1, minsize = 166)
        self.columnconfigure(1, weight = 0)
        self.columnconfigure(2, weight = 10)
        self.rowconfigure(0, weight = 1)
        #self.rowconfigure(1, weight = 1)
        self.Canvas1 = Paint(self, foreground="Green")
        self.Canvas1.grid(row=0, column=0, sticky=N+E+S+W)
        self.Canvas2 = Paint(self, foreground="Red")
        self.Canvas2.grid(row=0, column=2, sticky=N+E+S+W)
        self.Frame = Frame(self, relief = SUNKEN, bd = 3)
        self.Frame.grid(row=0, column=1, sticky=N+E+S+W)
        self.Frame.columnconfigure(0, weight = 1)
        self.Frame.ShowColor1 = Button(self.Frame, textvariable=self.Canvas1.foreground, command=self.askcolor1, width = 10, bg = self.Canvas1.foreground.get())
        self.Frame.ShowColor1.grid(row=0, column=0, sticky=N+W)
        self.Frame.ShowColor2 = Button(self.Frame, textvariable=self.Canvas2.foreground, command=self.askcolor2, width = 10, bg = self.Canvas2.foreground.get())
        self.Frame.ShowColor2.grid(row=0, column=1, sticky=N+E)
        self.Frame.Copy2t1 = Button(self.Frame, text = "<-", command=self.Copy2to1, width = 10)
        self.Frame.Copy2t1.grid(row=1, column=0, sticky=N+W)
        self.Frame.Copy1t2 = Button(self.Frame, text = "->", command=self.Copy1to2, width = 10)
        self.Frame.Copy1t2.grid(row=1, column=1, sticky=N+E)
        self.Frame.Clean_1 = Button(self.Frame, text = "Clean", command=self.Clean1, width = 10)
        self.Frame.Clean_1.grid(row=2, column=0, sticky=N+W)
        self.Frame.Clean_2 = Button(self.Frame, text = "Clean", command=self.Clean2, width = 10)
        self.Frame.Clean_2.grid(row=2, column=1, sticky=N+E)
        self.Frame.Save1 = Button(self.Frame, text = "Save", command=self.Save, width = 10)
        self.Frame.Save1.grid(row=3, column=0, sticky=N+W)
        self.Frame.Load1 = Button(self.Frame, text = "Load", command=self.Load, width = 10)
        self.Frame.Load1.grid(row=4, column=0, sticky=N+W)
        self.Frame.Quit = Button(self.Frame, text="Quit", command=self.quit, width = 21)
        self.Frame.Quit.grid(row=6, column=0, columnspan = 2, sticky=S)
        

app = MyApp(Title="Canvas Example")
app.mainloop()
    

