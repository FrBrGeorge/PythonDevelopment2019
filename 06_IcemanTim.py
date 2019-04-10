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
        self.center_window()
        self.grid(sticky=N+E+S+W)
        self.create()
        self.adjust()

    def center_window(self):
        width = 1200
        height = 720
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        osx = (screen_w - width)/2
        osy = (screen_h - height)/2
        self.master.geometry('%dx%d+%d+%d' % (width, height, osx, osy))

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
    def mousedown_left(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove_left(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup_left(self, event):
        '''Dragging is done'''
        self.cursor = None

    def mousedown_right(self, event):
        '''Store mousedown coords'''
        self.x1, self.y1 = event.x, event.y
        self.cursor = self.find_closest(event.x, event.y)
        self.x01, self.y01, self.x02, self.y02 = self.coords(self.cursor)
        self.col = self.itemcget(self.cursor, 'fill')

    def mousemove_right(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x01 + event.x - self.x1, self.y01 + event.y - self.y1
            ,self.x02 + event.x-self.x1,self.y02 + event.y-self.y1), fill=self.col)

    def mouseup_right(self, event):
        '''Dragging is done'''
        self.cursor = None

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, bg="white", relief=SUNKEN, *ap, **an)

        self.bind("<Button-1>", self.mousedown_left)
        self.bind("<B1-Motion>", self.mousemove_left)
        self.bind("<ButtonRelease-1>", self.mouseup_left)

        self.bind("<Button-3>", self.mousedown_right)
        self.bind("<B3-Motion>", self.mousemove_right)
        self.bind("<ButtonRelease-3>", self.mouseup_right)

class Actions(Frame):
    
    def askcolor(self):
        colour = colorchooser.askcolor()[1]
        if colour != None:
            self.Canvas1.foreground.set(colour) 
            self.Canvas2.foreground.set(self.Canvas1.foreground.get())  
            self.ShowColor['bg'] = self.Canvas1.foreground.get()

    def adjust(self):
        '''Adjust grid sise/properties'''
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)

    def copy(self):
        l = set()
        for i in self.Canvas1.find_all():
            l.add((*self.Canvas1.coords(i),self.Canvas1.itemcget(i, "fill")))
        for i in self.Canvas2.find_all():
            l.add((*self.Canvas2.coords(i),self.Canvas2.itemcget(i, "fill")))
        self.clear()
        for i in l:
            self.Canvas1.create_line(i[:4],fill=i[4])
            self.Canvas2.create_line(i[:4],fill=i[4])

    def clear(self):
        for i in self.Canvas1.find_all():
            self.Canvas1.delete(i)
        for i in self.Canvas2.find_all():
            self.Canvas2.delete(i)

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

    def __init__(self, canvas1=None, canvas2=None, master=None, Title="Application"):

        Frame.__init__(self)
        
        self.Canvas1=canvas1
        self.Canvas2=canvas2

        self.bg = 'black'
        
        self.AskColor = Button(self, text="Select colour", bg="lightgreen", command=self.askcolor)
        self.AskColor.grid(row=0, column=1, ipadx=40, ipady=40, padx=15, pady=5, sticky=N)

        self.ShowColor = Label(self, textvariable=self.Canvas1.foreground, bg=self.Canvas2.foreground.get())
        self.ShowColor.grid(row=3, column=1, ipadx=60, ipady=40, padx=15, pady =5,sticky=N)

        self.Copy = Button(self, text='Copy', bg="lightgreen", command=self.copy)
        self.Copy.grid(row=5, column=1, ipadx=60, ipady=40, padx=15, pady =5, sticky=N)

        self.Clear = Button(self, text='Clear', bg="lightgreen", command=self.clear)
        self.Clear.grid(row=7, column=1, ipadx=60, ipady=40, padx=15, pady =5, sticky=N)

        self.Save = Button(self, text='Save', bg="lightgreen", command=self.save)
        self.Save.grid(row=9, column=1, ipadx=60, ipady=40, padx=15, pady =5, sticky=N)

        self.Load = Button(self, text='Load',bg="lightgreen", command=self.load)
        self.Load.grid(row=11, column=1, ipadx=60, ipady=40, padx=15, pady =5, sticky=N)

        self.Quit = Button(self, text="Quit", bg="lightgreen", command=self.quit)
        self.Quit.grid(row=13, column=1, ipadx=60, ipady=40, padx=15, pady =5, sticky=N)
       
        self.adjust()

class MyApp(App):

    def create(self):
        self.Canvas1 = Paint(self, foreground="lightyellow")
        self.Canvas1.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)

        self.Canvas2 = Paint(self, foreground="lightyellow")
        self.Canvas2.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)

        act_buttons = Actions(canvas1=self.Canvas1, canvas2=self.Canvas2)
        act_buttons.grid(row=0, column=1, sticky=N)

app = MyApp(Title="HW_6_Bikbulatov")
app.mainloop()
