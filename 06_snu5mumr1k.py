#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пример объектной организации кода
"""

from tkinter import *
from tkinter import colorchooser


class Paint(Canvas):
    """Canvas with simple drawing"""
    def __init__(self, master=None, *args, foreground="black", **kwargs):
        self.foreground = StringVar()
        self.foreground.set(foreground)

        super().__init__(master=master, *args, **kwargs)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

    def mousedown(self, event):
        """Store mousedown coords"""
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove(self, event):
        """Do sometheing when drag a mouse"""
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
        """Dragging is done"""
        self.cursor = None


class Application(Frame):
    def __init__(self, master=None, Title="Application"):
        super().__init__(master=master)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.create_widgets()
        self.adjust()

    def create_widgets(self):
        self.Canvas = Paint(self, foreground="midnightblue")
        self.Canvas.grid(row=0, column=0, rowspan=3, sticky=N+E+S+W)
        self.AskColor = Button(self, text="Color", command=self.askcolor)
        self.AskColor.grid(row=0, column=1, sticky=N+W)
        self.ShowColor = Label(self, textvariable=self.Canvas.foreground)
        self.ShowColor.grid(row=1, column=1, sticky=N+W+E)
        self.Quit = Button(self, text="Quit", command=self.quit)
        self.Quit.grid(row=2, column=1, sticky=N+W)

    def adjust(self):
        """Adjust grid size/properties"""
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)

    def askcolor(self):
        self.Canvas.foreground.set(colorchooser.askcolor()[1])


def main():
    application = Application(Title="Canvas Example")
    application.mainloop()


if __name__ == "__main__":
    main()
