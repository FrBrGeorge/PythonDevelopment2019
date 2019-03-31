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
        self.anotherOne.cursor = None

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        if self.anotherOne.cursor:
            self.anotherOne.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())
        self.anotherOne.cursor = self.anotherOne.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
        '''Dragging is done'''
        self.anotherOne.cursor = None
        self.cursor = None
        #print(self.find_all())
    
    def thirddown(self, event):
        self.x00, self.y00 = event.x, event.y
        self.item = self.find_closest(event.x, event.y)[0]
        self.itemS = self.anotherOne.find_closest(event.x, event.y)[0]

    def thirdmove(self, event):
        self.move(self.item, event.x - self.x00, event.y - self.y00)
        self.anotherOne.move(self.itemS, event.x - self.x00, event.y - self.y00)
        self.x00 = event.x
        self.y00 = event.y

    def thirdup(self, event):
        return


    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)
        self.bind("<Button-3>", self.thirddown)
        self.bind("<B3-Motion>", self.thirdmove)
        self.bind("<ButtonRelease-3>", self.thirdup)


        self.anotherOne = None

class MyApp(App):
    def askcolor(self):
        color = colorchooser.askcolor()[1]
        self.Canvas.foreground.set(color)
        self.Canvas2.foreground.set(color)
        self.ShowColor.config(fg = color)

    def clear(self):
        self.Canvas.delete("all")
        self.Canvas2.delete("all")

    def write(self):
        file = filedialog.asksaveasfilename()
        with open(file, "w") as out_file:
            for item in self.Canvas.find_all():
                print(*self.Canvas.coords(item), self.Canvas.itemcget(item, "fill"), file = out_file)

    def read(self):
        file = filedialog.askopenfilename()
        with open(file, "r") as in_file:
            objects = in_file.read().splitlines()
            for obj in objects:
                info = obj.split()
                self.Canvas.create_line((info[0], info[1], info[2], info[3]), fill = info[4])
                self.Canvas2.create_line((info[0], info[1], info[2], info[3]), fill = info[4])

    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)

        self.Canvas2 = Paint(self, foreground="midnightblue")
        self.Canvas2.grid(row = 3, column = 0, rowspan=3, sticky=N+E+S+W)

        self.Canvas.anotherOne = self.Canvas2
        self.Canvas2.anotherOne = self.Canvas

        self.Frame = Frame(self)
        self.Frame.grid(row = 0, column = 1, sticky = N+W)

        self.AskColor = Button(self.Frame, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=1, sticky=N+W)
        
        self.ShowColor = Label(self.Frame, textvariable=self.Canvas.foreground, fg = self.Canvas.foreground.get())
        self.ShowColor.grid(row=1, column=1, sticky=N+W)
        
        self.Quit = Button(self.Frame, text="Quit", command=self.quit)
        self.Quit.grid(row=2, column=1, sticky=N+W)

        self.Clear = Button(self.Frame, text = "Clear", command = self.clear)
        self.Clear.grid(row = 3, column = 1, sticky = N+W)

        self.Write = Button(self.Frame, text = "Write", command = self.write)
        self.Write.grid(row = 4, column = 1, sticky = N+W)

        self.Read = Button(self.Frame, text = "Read", command = self.read)
        self.Read.grid(row = 5, column = 1, sticky = N+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))

