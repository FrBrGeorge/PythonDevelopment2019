#!/usr/bin/env python3

from tkinter import *
from tkinter import colorchooser, filedialog


class App(Frame):
    """Base framed application class"""

    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N + E + S + W)
        self.create()
        self.adjust()

    def create(self):
        """Create all the widgets"""
        self.bQuit = Button(self, text="Quit", command=self.quit)
        self.bQuit.grid()

    def adjust(self):
        """Adjust grid sise/properties"""
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)


class Paint(Canvas):
    """Canvas with simple drawing"""

    def mousedown(self, event):
        """Store mousedown coords"""
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove(self, event):
        """Do sometheing when drag a mouse"""
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line(
            (self.x0, self.y0, event.x, event.y), fill=self.foreground.get()
        )

    def mouseup(self, event):
        """Dragging is done"""
        self.cursor = None
        # print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

    def draw_lines(self, lines_list):
        for line in lines_list:
            self.create_line(line[:4], fill=line[4])

    def save(self, path):
        with open(path, "w") as file:
            for line in self.lines:
                to_write = [str(elem) for elem in line]
                file.write(" ".join(to_write) + "\n")

    def load(self, path):
        lines = []
        with open(path, "r") as file:
            for line_string in file:
                line = [float(elem) for elem in line_string.split()[:4]]
                line.append(" ".join(line_string.split()[4:]))
                lines.append(line)
        self.delete(ALL)
        self.draw_lines(lines)

    @property
    def lines(self):
        return [
            self.coords(item) + [self.itemcget(item, "fill")]
            for item in self.find_all()
        ]


class MyApp(App):
    def askcolor(self):
        color = colorchooser.askcolor()[1]
        self.Canvas1.foreground.set(color)
        self.Canvas2.foreground.set(color)
        self.ShowColor["bg"] = color

    def create(self):
        self._create_canvases()
        self._create_buttons()

    def _create_canvases(self):
        self.Canvas1 = Paint(self, foreground="midnightblue")
        self.Canvas1.grid(row=0, column=0, rowspan=3, sticky=N + S + W)
        self.Canvas2 = Paint(self, foreground="midnightblue")
        self.Canvas2.grid(row=3, column=0, rowspan=3, sticky=N + S + W)

    def _create_buttons(self):
        self.frame = Frame(self)
        self.frame.grid(row=0, column=1, sticky=N + W)
        self.AskColor = Button(self.frame, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=0, sticky=N + W)
        self.ShowColor = Label(
            self.frame, textvariable=self.Canvas1.foreground, bg="midnightblue"
        )
        self.ShowColor.grid(row=1, column=0, sticky=N + W + E)
        self.Quit = Button(self.frame, text="Quit", command=self.quit)
        self.Quit.grid(row=2, column=0, sticky=N + W)
        self.Copy12 = Button(
            self.frame,
            text="Copy from upper canvas to lower canvas",
            command=self.copy_lines12,
        )
        self.Copy12.grid(row=3, column=0, sticky=N + W)
        self.Copy21 = Button(
            self.frame,
            text="Copy from lower canvas to upper canvas",
            command=self.copy_lines21,
        )
        self.Copy21.grid(row=4, column=0, sticky=N + W)
        self.Delete = Button(
            self.frame, text="Clear upper canvas", command=self.clear_canvas1
        )
        self.Delete.grid(row=5, column=0, sticky=N + W)
        self.Delete = Button(
            self.frame, text="Clear lower canvas", command=self.clear_canvas2
        )
        self.Delete.grid(row=6, column=0, sticky=N + W)
        self.Save = Button(
            self.frame, text="Save upper canvas", command=self.save_canvas
        )
        self.Save.grid(row=7, column=0, sticky=N + W)
        self.Load = Button(
            self.frame, text="Load upper canvas from file", command=self.load_canvas
        )
        self.Load.grid(row=8, column=0, sticky=N + W)

    def copy_lines12(self):
        lines1 = self.Canvas1.lines
        self.Canvas2.draw_lines(lines1)

    def copy_lines21(self):
        lines2 = self.Canvas2.lines
        self.Canvas1.draw_lines(lines2)

    def clear_canvas1(self):
        self.Canvas1.delete(ALL)

    def clear_canvas2(self):
        self.Canvas2.delete(ALL)

    def save_canvas(self):
        path = filedialog.asksaveasfilename(
            initialdir="./",
            title="Select file",
            filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        )
        self.Canvas1.save(path)

    def load_canvas(self):
        path = filedialog.askopenfilename(
            initialdir="./",
            title="Select file",
            filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        )
        self.Canvas1.load(path)


app = MyApp(Title="Canvas Example")
app.mainloop()
print(*app.Canvas1.lines, sep="\n")
