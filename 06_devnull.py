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
        self.grid(sticky=N + E + S + W)
        self.create()
        self.config()

    def create(self):
        '''Create all the widgets'''
        self.bQuit = Button(self, text='Quit', command=self.quit)
        self.bQuit.grid(row=0, column=1)

    def config(self):
        #self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        #self.rowconfigure(1, weight=1)

'''
    def adjust(self):
        
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)
'''


class Paint(Canvas):

    def mousedown(self, event):
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove(self, event):
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
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
        self.Canvas.foreground.set(colorchooser.askcolor()[1])
        self.ShowColor['bg'] = self.Canvas.foreground.get()

    def load(self):
        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(("text file", "*.txt"),)
        )
        if not filename:
            return
        with open(filename, "r") as f:
            for s in f.readlines():
                s = s.split()
                coords = tuple(float(i) for i in s[:4])
                color = s[4]
                self.Canvas.create_line(coords, fill=color)

    def clear(self):
        self.Canvas.delete(ALL)
        self.Canvas2.delete(ALL)

    def copy(self):
        l = set()
        for i in self.Canvas.find_all():
            l.add((*self.Canvas.coords(i), self.Canvas.itemcget(i, "fill")))
        for i in self.Canvas2.find_all():
            l.add((*self.Canvas2.coords(i), self.Canvas2.itemcget(i, "fill")))
        self.clear()
        for i in l:
            self.Canvas.create_line(i[:4], fill=i[4])
            self.Canvas2.create_line(i[:4], fill=i[4])

    def save(self):
        filename = filedialog.asksaveasfilename(
            initialdir="/",
            title="Select",
            filetypes=(("file", "*.txt"),)
        )
        if not filename:
            return
        with open(filename, "w") as f:
            canvas = self.Canvas
            for i in canvas.find_all():
                for s in canvas.coords(i):
                    f.write(str(s) + " ")
                f.write(canvas.itemcget(i, "fill") + "\n")

    def create(self):
        self.Canvas = Paint(self, foreground="black")
        self.Canvas.foreground.set("#000000")
        self.Canvas.grid(row=0, column=0, rowspan=3, sticky=N + E + S + W)
        self.Canvas2 = Paint(self, foreground="black")
        self.Canvas2.foreground.set("#000000")
        self.Canvas2.grid(row=0, column=2, rowspan=3, sticky=N + E + S + W)
        self.AskColor = Button(self, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=1, sticky=W + N + S + E)
        self.ShowColor = Label(self, textvariable=self.Canvas.foreground)
        self.ShowColor.grid(row=1, column=1, sticky=W + N + S + E)
        self.ShowColor['bg'] = self.Canvas.foreground.get()
        self.Copy = Button(self, text="CopyToRight", command=self.copy)
        self.Copy.grid(row=2, column=1, sticky=W + N + S + E)
        self.Load = Button(self, text="Load", command=self.load)
        self.Load.grid(row=3, column=1, sticky=W + N + S + E)
        self.Save = Button(self, text="Save", command=self.save)
        self.Save.grid(row=4, column=1, sticky=W + N + S + E)
        self.Clear = Button(self, text="Clear", command=self.clear)
        self.Clear.grid(row=5, column=1, sticky=W + N + S + E)
        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=6, column=1, sticky=W + N + S + E)


app = MyApp(Title="Canvas Example")
app.mainloop()
# for item in app.Canvas.find_all():
#   print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))
