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
        #print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)


class ButFrame(Frame):
    def askcolor(self):
        self.Canvas.foreground.set(colorchooser.askcolor()[1]) 
        self.Canvas1.foreground.set(self.Canvas.foreground.get())  
        self.ShowColor['bg'] = self.Canvas.foreground.get()

    def adjust(self):
        '''Adjust grid sise/properties'''
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)

    def copy(self):
        l = set()
        for i in self.Canvas.find_all():
            l.add((*self.Canvas.coords(i),self.Canvas.itemcget(i, "fill")))
        for i in self.Canvas1.find_all():
            l.add((*self.Canvas1.coords(i),self.Canvas1.itemcget(i, "fill")))

        for i in l:
            self.Canvas.create_line(i[:4],fill=i[4])
            self.Canvas1.create_line(i[:4],fill=i[4])

    def clear(self):
        for i in self.Canvas.find_all():
            self.Canvas.delete(i)
        for i in self.Canvas1.find_all():
            self.Canvas1.delete(i)

    def __init__(self, canvas=None, canvas1=None, master=None, Title="Application"):
        Frame.__init__(self)
        self.Canvas=canvas
        self.Canvas1=canvas1
        self.bg = 'black'
        self.AskColor = Button(self, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=1, sticky=N)

        self.ShowColor = Label(self, textvariable=self.Canvas.foreground, bg=self.Canvas.foreground.get())
        self.ShowColor.grid(row=1, column=1, sticky=N)
            
        self.Copy = Button(self, text='Copy', command=self.copy)
        self.Copy.grid(row=2, column=1, sticky=N)

        self.Clear = Button(self, text='Clear', command=self.clear)
        self.Clear.grid(row=3, column=1, sticky=N)

        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=4, column=1, sticky=N)
        self.adjust()
     
class MyApp(App):

    def create(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)
        self.Canvas1 = Paint(self, foreground="midnightblue")
        self.Canvas1.grid(row=0, column=1, sticky=N+E+S+W)
        butFr = ButFrame(canvas=self.Canvas, canvas1=self.Canvas1)
        butFr.grid(row=0,column=1, sticky=N)



app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))

