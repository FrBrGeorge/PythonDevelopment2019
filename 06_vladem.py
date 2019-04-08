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

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

class MyApp(App):
    def askcolor(self):
        self.Canvas.foreground.set(colorchooser.askcolor()[1])
        # change background / foreground color 
        self.ShowColor.configure(fg = self.Canvas.foreground.get())
        self.Canvas.configure(bg = self.Canvas.foreground.get())

    def clear(self):
        self.Canvas.delete("all")

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
                
    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue", bg="midnightblue")
        self.Canvas.grid(row=0, column=0, rowspan=2, sticky=N+E+S+W)
        self.Canvas.create_line(0, 0, 100, 300, fill='white')
        # second canvas
        self.CanvasCopy = Canvas(bg="pink")
        self.CanvasCopy.grid(row=2, column=0, rowspan=2, sticky=N+E+S+W)
        for line in self.Canvas.find_all():
            self.CanvasCopy.create_line(self.Canvas.coords(line),fill=self.Canvas.itemcget(line, "fill"))
        # frame containing controls
        frame = Frame(self)
        frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky=N+E+S+W)

        self.AskColor = Button(frame, text="Pick color", command=self.askcolor)
        self.AskColor.grid(row=0, column=0)
        
        self.ShowColor = Label(frame, textvariable=self.Canvas.foreground, fg="midnightblue")
        self.ShowColor.grid(row=1, column=0)
        
        self.Quit = Button(frame, text="Quit", command=self.quit)
        self.Quit.grid(row=2, column=0)

        self.Write = Button(frame, text = "Write", command = self.write)
        self.Write.grid(row = 4, column = 0)

app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))

