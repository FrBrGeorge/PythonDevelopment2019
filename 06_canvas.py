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
        
class Paint(Canvas):
    def buttondown(*args):
        print(*args)

    def __init__(self, master=None):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.buttondown)

class MyApp(App):
    def create(self):
        self.Canvas = Paint(self)
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
