#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пример объектной организации кода
"""

from tkinter import (
    Button,
    Canvas,
    Frame,
    Label,
    StringVar,
    Tk,

    colorchooser,
)
import tkinter


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
        if self.cursor is not None:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
        """Dragging is done"""
        self.cursor = None


class Menu(Frame):
    def __init__(self, paint_widget, master=None):
        self.paint_widget = paint_widget

        super().__init__(master=master)

        self.create_widgets()

    def create_widgets(self):
        self.ask_color = Button(self, text="Color", command=self.askcolor)
        self.ask_color.grid(row=0, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        # The longest color name as man page says http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
        self.show_color = Label(self, textvariable=self.paint_widget.foreground, width=len('light goldenrod yellow') + 3)
        self.show_color.grid(row=1, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        self.quit = Button(self, text="Quit", command=self.quit)
        self.quit.grid(row=2, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

    def askcolor(self):
        self.paint_widget.foreground.set(colorchooser.askcolor()[1])


class Application(Frame):
    class MenuCell:
        row = 0
        column = 0

    class PaintCell:
        row = 0
        column = 1

    def __init__(self, master=None, Title="Application"):
        super().__init__(master=master)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W)
        self.create_widgets()
        self.adjust()

    def create_widgets(self):
        paint_widget = Paint(self, foreground="midnightblue")
        paint_widget.grid(row=self.PaintCell.row, column=self.PaintCell.column, sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W)

        menu = Menu(paint_widget=paint_widget, master=self)
        menu.grid(row=self.MenuCell.row, column=self.MenuCell.column, sticky=tkinter.N + tkinter.W)

    def adjust(self):
        """Adjust grid size/properties"""
        for column in range(self.size()[0]):
            if column in [self.PaintCell.column]:
                self.columnconfigure(column, weight=12)

        for row in range(self.size()[1]):
            if row in [self.MenuCell.row, self.PaintCell.row]:
                self.rowconfigure(row, weight=12)


def main():
    application = Application(Title="Canvas Example")
    application.mainloop()


if __name__ == "__main__":
    main()
