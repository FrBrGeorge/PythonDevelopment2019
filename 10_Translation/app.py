#!/usr/bin/env python3
# runargs: -i
from tkinter import *
import sys
import os.path
import gettext


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
        update_labels(feet.get(), meters.get())
    except ValueError:
        pass


def update_labels(f=0, m=0):
    m, f = int(float(m)), int(float(f))
    mlabel['text'] = ngettext("meter", "meters", m)
    flabel['text'] = ngettext("foot", "feet", f)


datapath = os.path.dirname(sys.argv[0])
gettext.install('app', datapath, names=("ngettext",))

root = Tk()
root.title(_("Feet to meters"))

mainframe = Frame(root, padx=3, pady=12)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

Logo = PhotoImage(file=os.path.join(datapath, _("LogoEN.png")))
Label(mainframe, image=Logo).grid(column=1, row=1, sticky=(N, W))

feet_entry = Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

Label(mainframe, textvariable=meters, relief=GROOVE)\
    .grid(column=2, row=2, sticky=(W, E))
Button(mainframe, text=_("Calculate"), command=calculate)\
    .grid(column=3, row=3, sticky=W)

flabel = Label(mainframe)
flabel.grid(column=3, row=1, sticky=W)
Label(mainframe, text=_("is equivalent to")).grid(column=1, row=2, sticky=E)
mlabel = Label(mainframe)
mlabel.grid(column=3, row=2, sticky=W)
update_labels()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
