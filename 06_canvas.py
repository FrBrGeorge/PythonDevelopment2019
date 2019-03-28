#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *

class App(Frame):
    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.create()

    def create(self):
        self.bQuit = Button(self, text='Quit', command=self.quit)
        self.bQuit.grid()
        

app = App(Title="Example")
app.mainloop()
