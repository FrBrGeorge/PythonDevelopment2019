#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Домашнее задание по 05_WidgetsAndCollaborative
"""

from argparse import ArgumentParser
from pathlib import Path
import logging

from tkinter import Tk, Frame, PhotoImage, StringVar, Listbox, Label
import tkinter

logger = logging.getLogger(__name__)


class Application(Frame):
    def __init__(self, images_path, images_pattern, refresh_rate=1000, master=None):
        self.images_path = images_path
        self.images_pattern = images_pattern
        self.refresh_rate = refresh_rate

        super().__init__(master)
        self.master = master
        self.grid(column=0, row=0, sticky=tkinter.E + tkinter.W + tkinter.S + tkinter.N)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    def refresh_images(self):
        self.images_mapping = self.get_images()
        self.files_list.set(value=sorted(self.images_mapping.keys()))
        self.after(self.refresh_rate, self.get_images)

    def set_active_image(self, event):
        identifier = event.widget.selection_get()
        image = self.images_mapping.get(identifier)
        if image is not None:
            self.active_image.configure(image=image)
        else:
            logger.error("Image was stolen!")

    def create_widgets(self):
        self.files_list = StringVar()
        self.refresh_images()

        self.active_image = Label(self)
        self.active_image.grid(row=0, column=1, sticky=tkinter.E + tkinter.W + tkinter.S + tkinter.N)

        files_listbox = Listbox(self, listvariable=self.files_list)
        files_listbox.grid(row=0, column=0, sticky=tkinter.E + tkinter.W + tkinter.N)
        files_listbox.bind("<<ListboxSelect>>", self.set_active_image)
        files_listbox.selection_set(0)

    def get_images(self):
        images = self.images_path.glob(self.images_pattern)
        result = {}
        for image_file in images:
            identifier = image_file.with_suffix("").name
            identifier_file = image_file.with_suffix(".txt")
            if not identifier_file.exists():
                logging.warning("There is no description for %s", identifier)
            else:
                with identifier_file.open() as f:
                    identifier = f.read().strip()

            result[identifier] = PhotoImage(file=str(image_file))

        return result


def main(args):
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    application = Application(
        images_path=args.images_path,
        images_pattern=args.images_pattern,
        master=root,
        refresh_rate=args.refresh_rate,
    )
    application.mainloop()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--images-path", default=Path(), type=Path)
    parser.add_argument("--images-pattern", default="*.png")
    parser.add_argument("--refresh-rate", default=1000, type=int, help="refresh info rate in seconds")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    logger.setLevel("DEBUG" if args.verbose else "INFO")

    main(args)
