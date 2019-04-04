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
            self.rowconfigure(i, weight=1)
        
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

    def rightdown(self, event):
        self.closest = self.find_closest(event.x, event.y)
        if self.closest:
            self.direction = self.coords(self.closest)[2] - self.coords(self.closest)[0], self.coords(self.closest)[3] - self.coords(self.closest)[1]
            color = self.itemcget(self.closest, "fill")
            self.delete(self.closest)
            self.closest = self.create_line((event.x, event.y, self.direction[0] + event.x, self.direction[1] + event.y), fill=color)

    def rightmove(self, event):
        if self.closest:
            color = self.itemcget(self.closest, "fill")
            self.delete(self.closest)
            self.closest = self.create_line((event.x, event.y, self.direction[0] + event.x, self.direction[1] + event.y), fill=color)

    def rightup(self, event):
        self.closest = None

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

        self.bind("<Button-3>", self.rightdown)
        self.bind("<B3-Motion>", self.rightmove)
        self.bind("<ButtonRelease-3>", self.rightup)

class ToolSet(Frame):
    def __init__(self, canvases=None):
        Frame.__init__(self)
        self.canvases = canvases
        self.AskColor = Button(self, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=0, sticky=N+W)
        self.ShowColor = Label(self, textvariable=self.canvases[0].foreground, background=self.canvases[0].foreground.get())
        self.ShowColor.grid(row=1, column=0, sticky=N+W+E)
        self.Sync = Button(self, text="Syncronize canvases", command=self.syncronize_canvases)
        self.Sync.grid(row=2, column=0, sticky=N+W)
        self.Cleaner = Button(self, text="Clear canvases", command=self.clear_canvases)
        self.Cleaner.grid(row=3, column=0, sticky=N+W)
        self.Save = Button(self, text="Save", command=self.save_canvases)
        self.Save.grid(row=4, column=0, sticky=N+W)
        self.Load = Button(self, text="Load", command=self.load_canvases)
        self.Load.grid(row=5, column=0, sticky=N+W)
        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=6, column=0, sticky=N+W)

    def askcolor(self):
        color = colorchooser.askcolor()[1]
        for canvas in self.canvases:
            canvas.foreground.set(color)
        self.ShowColor["background"] = color

    def syncronize_canvases(self):
        lines = set()
        for canvas in self.canvases:
            for item in canvas.find_all():
                lines.add((*canvas.coords(item), canvas.itemcget(item, "fill")))

        self.clear_canvases()

        for canvas in self.canvases:
            for line in lines:
                canvas.create_line(line[:4], fill=line[-1])

    def clear_canvases(self):
        for canvas in self.canvases:
            canvas.delete("all")

    def save_canvases(self):
        filename = filedialog.asksaveasfilename()
        if filename is None:
            return

        with open(filename, "w") as fout:
            print(len(self.canvases), file=fout)
            for canvas in self.canvases:
                print(len(canvas.find_all()), file=fout)
                for item in canvas.find_all():
                    print(*canvas.coords(item), canvas.itemcget(item, "fill"), file=fout)

    def load_canvases(self):
        filename = filedialog.askopenfilename()
        if filename is None:
            return

        self.clear_canvases()

        with open(filename, "r") as fin:
            canvases_in_file = int(next(fin))
            for canvas in self.canvases:
                lines_size = int(next(fin))
                for i in range(lines_size):
                    line = next(fin).split()
                    canvas.create_line([float(x) for x in line[:4]], fill=line[-1])


class MyApp(App):
    def create(self):
        self.Canvases = [Paint(self, foreground="midnightblue") for i in range(2)]
        for i, canvas in enumerate(self.Canvases):
            canvas.grid(row=0, column=i, rowspan=3, sticky=N+E+S+W)
        self.Canvases[1]["background"] = "black"
        self.tools = ToolSet(self.Canvases)
        self.tools.grid(row=0, column=len(self.Canvases), sticky=N+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
for item in app.Canvases[0].find_all():
    print(*app.Canvases[0].coords(item), app.Canvases[0].itemcget(item, "fill"))

