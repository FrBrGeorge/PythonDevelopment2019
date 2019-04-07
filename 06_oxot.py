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

    def mouse3down(self, event):
        '''Store mousedown coords'''
        self.x1, self.y1 = event.x, event.y
        self.cursor = self.find_closest(event.x, event.y)
        self.x01, self.y01, self.x02, self.y02 = self.coords(self.cursor)
        self.col = self.itemcget(self.cursor, 'fill')

    def mouse3move(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        
        self.cursor = self.create_line((self.x01 + event.x - self.x1, self.y01 + event.y - self.y1
            ,self.x02 + event.x-self.x1,self.y02 + event.y-self.y1), fill=self.col)

    def mouse3up(self, event):
        '''Dragging is done'''
        self.cursor = None

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)
        self.bind("<Button-3>", self.mouse3down)
        self.bind("<B3-Motion>", self.mouse3move)
        self.bind("<ButtonRelease-3>", self.mouse3up)


class ButFrame(Frame):
    def askcolor(self):
        col = colorchooser.askcolor()[1]
        if col:
            self.Canvas.foreground.set(col) 
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

        self.clear()

        for i in l:
            self.Canvas.create_line(i[:4],fill=i[4])
            self.Canvas1.create_line(i[:4],fill=i[4])

    def clear(self):
        for i in self.Canvas.find_all():
            self.Canvas.delete(i)
        for i in self.Canvas1.find_all():
            self.Canvas1.delete(i)


    def save(self):
        def strr(l):
            s = ''
            for i in l:
                s += str(i) + ' '
            return s

        f = filedialog.asksaveasfilename()
        if f:
            file = open(f,'w')
            for i in self.Canvas.find_all():
                file.write(strr(self.Canvas.coords(i)) + " " + str(self.Canvas.itemcget(i, "fill")) + ' 0' + '\n')
            for i in self.Canvas1.find_all():
                file.write(strr(self.Canvas1.coords(i)) + " " + str(self.Canvas1.itemcget(i, "fill")) + ' 1' + '\n')
            file.close()

    def load(self):
        f = filedialog.askopenfilename()
        if f:
            self.clear()
            file = open(f,'r')

            for i in file:
                i = i.split()
                if i[-1] == '0':
                    self.Canvas.create_line(i[:4], fill=i[4])
                if i[-1] == '1':
                    self.Canvas1.create_line(i[:4], fill=i[4])

            file.close()


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

        self.Save = Button(self, text='Save', command=self.save)
        self.Save.grid(row=4, column=1, sticky=N)

        self.Load = Button(self, text='Load', command=self.load)
        self.Load.grid(row=5, column=1, sticky=N)

        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=6, column=1, sticky=N)
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

