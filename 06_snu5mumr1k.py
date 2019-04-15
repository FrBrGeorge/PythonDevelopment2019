#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пример объектной организации кода
"""

from pathlib import Path
import json
import logging

from tkinter import (
    Button,
    Canvas,
    Frame,
    Label,
    StringVar,
    Tk,

    colorchooser,
    filedialog,
)
import tkinter

logger = logging.getLogger(__name__)


def get_lines_descriptions(canvas):
    result = []
    for item in canvas.find_all():
        result.append(
            {
                "coordinates": canvas.coords(item),
                "config": {
                    "fill": canvas.itemcget(item, "fill"),
                },
            }
        )
    return result


def restore_lines_from_descriptions(canvas, lines):
    canvas.delete(tkinter.ALL)

    for line in lines:
        canvas.create_line(line["coordinates"], **line["config"])



class Paint(Canvas):
    """Canvas with simple drawing"""
    def __init__(self, *args, master=None, foreground="black", **kwargs):
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
        ask_color = Button(self, text="Color", command=self.ask_color)
        ask_color.grid(row=0, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        # The longest color name as man page says http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
        self.show_color = Label(
            self,
            textvariable=self.paint_widget.foreground,
            width=len('light goldenrod yellow') + 3,
        )
        self.set_color(self.paint_widget.foreground.get())
        self.show_color.grid(row=1, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        clear = Button(self, text="Clear", command=self.clear)
        clear.grid(row=2, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        save_painting = Button(self, text="Save painting as ...", command=self.save(self.paint_widget))
        save_painting.grid(row=3, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        save_painting = Button(self, text="Load", command=self.load(self.paint_widget))
        save_painting.grid(row=4, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.grid(row=5, column=0, sticky=tkinter.N + tkinter.W + tkinter.E)

    def ask_color(self):
        color = colorchooser.askcolor()[1]
        self.paint_widget.foreground.set(color)
        self.set_color(color)

    def set_color(self, color):
        self.show_color.configure(bg=color)
        self.show_color.configure(fg=self.invert_color(color))

    def invert_color(self, color):
        if isinstance(color, str):
            color = self.winfo_rgb(color)

        inverted_color = [65535 - i for i in color]
        return f"#{inverted_color[0]:x}{inverted_color[1]:x}{inverted_color[2]:x}"

    def clear(self):
        self.paint_widget.delete(tkinter.ALL)

    def save(self, canvas):
        def do_save():
            description = get_lines_descriptions(canvas)
            filename = filedialog.asksaveasfilename(
                filetypes=[
                    ("JSON files", "*.json"),
                ],
                initialdir=".",
            )
            if not filename:
                logger.info("Empty filename")
                return

            destination = Path(filename)
            with destination.open("w") as f:
                json.dump(description, f)

        return do_save

    def load(self, canvas):
        def do_load():
            filename = filedialog.askopenfilename(
                filetypes=[
                    ("ALL files", "*.*"),
                    ("JSON files", "*.json"),
                ],
                initialdir=".",
                defaultextension=".json",
            )
            if not filename:
                logger.info("Empty filename")
                return

            destination = Path(filename)
            with destination.open() as f:
                lines = json.load(f)

            restore_lines_from_descriptions(canvas, lines)

        return do_load


class CopyMenu(Frame):
    def __init__(self, paint_widget, buffer_widget, master=None):
        self.paint_widget = paint_widget
        self.buffer_widget = buffer_widget

        super().__init__(master=master)
        self.create_widgets()

    def create_widgets(self):
        copy_from_buffer = Button(
            self,
            text="<-",
            command=self.copy(self.buffer_widget, self.paint_widget),
        )
        copy_from_buffer.grid(row=0, column=0)

        copy_to_buffer = Button(
            self,
            text="->",
            command=self.copy(self.paint_widget, self.buffer_widget),
        )
        copy_to_buffer.grid(row=1, column=0)

    def copy(self, source, destination):
        def do_copy():
            lines = get_lines_descriptions(source)
            restore_lines_from_descriptions(destination, lines)

        return do_copy


class Application(Frame):
    class MenuCell:
        row = 0
        column = 0

    class PaintCell:
        row = 0
        column = 1

    class CopyMenuCell:
        row = 0
        column = 2

    class BufferPaintCell:
        row = 0
        column = 3

    def __init__(self, master=None, Title="Application"):
        super().__init__(master=master)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        self.create_widgets()
        self.adjust()

    def create_widgets(self):
        paint_widget = Paint(
            foreground="midnightblue",
            master=self,
        )
        paint_widget.grid(
            column=self.PaintCell.column,
            row=self.PaintCell.row,
            sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W,
        )

        buffer_widget = Canvas(
            master=self,
        )
        buffer_widget.grid(
            column=self.BufferPaintCell.column,
            row=self.BufferPaintCell.row,
            sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W,
        )

        copy_menu = CopyMenu(
            buffer_widget=buffer_widget,
            master=self,
            paint_widget=paint_widget,
        )
        copy_menu.grid(row=self.CopyMenuCell.row, column=self.CopyMenuCell.column, sticky=tkinter.N + tkinter.E + tkinter.W)

        menu = Menu(paint_widget=paint_widget, master=self)
        menu.grid(row=self.MenuCell.row, column=self.MenuCell.column, sticky=tkinter.N + tkinter.W)

    def adjust(self):
        """Adjust grid size/properties"""
        for column in range(self.size()[0]):
            if column in [self.PaintCell.column, self.BufferPaintCell.column]:
                self.columnconfigure(column, weight=12)

        for row in range(self.size()[1]):
            self.rowconfigure(row, weight=12)


def main():
    application = Application(Title="Canvas Example")
    application.mainloop()


if __name__ == "__main__":
    logger.setLevel("DEBUG")

    main()
