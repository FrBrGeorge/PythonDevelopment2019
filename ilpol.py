#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
class App(Frame):
    '''Base framed application class'''
    current_foreground_color = "midnightblue"
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
    def mouseselect(self, event):
        if self.selected != None:
            self.itemconfig(self.selected, dash=())
            self.selected = None
        else:
            line = self.find_closest(event.x, event.y)
            self.itemconfig(line, dash=(4,4))
            self.selected = line
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
        print("color = ",self.current_foreground_color)
        self.current_foreground_color = colorchooser.askcolor()[1]
        self.ControlFrame.ShowColor.configure(bg=self.current_foreground_color)
        self.Canvas.foreground.set(self.current_foreground_color)
        self.New_Canvas.foreground.set(self.current_foreground_color)
       
    
    def copy12(self):

        lines = self.Canvas.find_all()

        for i in lines:
            self.New_Canvas.create_line(
                self.Canvas.coords(i),
                fill=self.Canvas.itemcget(i, "fill")
            )

    def copy21(self):

        lines = self.New_Canvas.find_all()

        for i in lines:
            self.Canvas.create_line(
                self.New_Canvas.coords(i),
                fill=self.New_Canvas.itemcget(i, "fill")
            )
    def delete(self,canvas):
          for i in canvas.find_all():
              canvas.delete(i)

    def save(self):
        filename = filedialog.asksaveasfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (("text file", "*.txt"),)
        )
        
        with open(filename, "w") as file:
            for i in self.Canvas.find_all():
                for coord in self.Canvas.coords(i):
                    file.write(str(coord) + " ")
                file.write(self.Canvas.itemcget(i, "fill") + "\n")
        filename = filename + "New_Canvas"
        with open(filename, "w") as file:
            for i in self.New_Canvas.find_all():
                for coord in self.New_Canvas.coords(i):
                    file.write(str(coord) + " ")
                file.write(self.New_Canvas.itemcget(i, "fill") + "\n")

    def load(self):
        filename = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (("text file", "*.txt"),)
        )
        
        with open(filename, "r") as file:
            for line in file.readlines():
                coords = ()
                for i in line.split():
                    coords = coords + (i,)
                bg = coords[4]
                coords = coords[:-1]

                self.Canvas.create_line(coords, fill=bg)
        filename = filename + "New_Canvas"
        with open(filename, "r") as file:
            for line in file.readlines():
                coords = ()
                for i in line.split():
                    coords = coords + (i,)
                bg = coords[4]
                coords = coords[:-1]
                self.New_Canvas.create_line(coords, fill=bg)

    def create(self):
        self.Canvas = Paint(self, foreground=self.current_foreground_color)
        self.Canvas.grid(row=0, column=0,rowspan = 9, sticky=N+E+S+W)
        self.Canvas.configure(bg="#ffdaa0")

        self.New_Canvas = Paint(self, foreground=self.current_foreground_color)
        self.New_Canvas.grid(row=0, column=1,rowspan =9 , sticky=N+E+S+W)
        self.New_Canvas.configure(bg="#dbf4d7")

        self.ControlFrame = Frame(self)
        self.ControlFrame.grid(row=0, column=2,  sticky=N+E+S+W)

        self.ControlFrame.AskColor = Button(self, text="Color", command=self.askcolor)
        self.ControlFrame.AskColor.grid(row=0, column=2, sticky=N+E+S+W)
        self.ControlFrame.ShowColor = Label(self, textvariable=self.Canvas.foreground)
        self.ControlFrame.ShowColor.grid(row=1, column=2, sticky=N+E+S+W)
        self.ControlFrame.ShowColor.configure(bg=self.current_foreground_color)

        self.ControlFrame.Copy1 = Button(self, text="1 to 2", command= self.copy12)
        self.ControlFrame.Copy1.grid(row=2, column=2, sticky=N+E+S+W)

        self.ControlFrame.Copy1 = Button(self, text="2 to 1", command= self.copy21)
        self.ControlFrame.Copy1.grid(row=3, column=2, sticky=N+E+S+W)

        self.ControlFrame.Clear1 = Button(self, text="Delete1",
                                            command = lambda : self.delete(self.Canvas))
        self.ControlFrame.Clear1.grid(row=4, column=2, sticky=N+E+S+W)

        self.ControlFrame.Clear2 = Button(self, text="Delete2",
                                            command = lambda : self.delete(self.New_Canvas))
        self.ControlFrame.Clear2.grid(row=5, column=2, sticky=N+E+S+W)

        self.ControlFrame.Save = Button(self, text="Save", command=self.save)
        self.ControlFrame.Save.grid(row=6, column=2, sticky=N+E+S+W)

        self.ControlFrame.Load = Button(self, text="Load", command=self.load)
        self.ControlFrame.Load.grid(row=7, column=2, sticky=N+E+S+W)

        self.ControlFrame.Quit = Button(self, text="Quit", command=self.quit)
        self.ControlFrame.Quit.grid(row=8, column=2, sticky=N+E+S+W)



app = MyApp(Title="Canvas")
app.mainloop()
for item in app.Canvas.find_all():
    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))

