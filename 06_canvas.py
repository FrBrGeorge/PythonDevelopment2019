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
    def mousedown(self, event):
        print(event)

    def mousemove(self, event):
        print(event)

    def mouseup(self, event):
        print(event)

    def __init__(self, master=None):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

class MyApp(App):
    def create(self):
        self.Canvas = Paint(self)
        self.Canvas.grid(row=0, column=0, sticky=N+E+S+W)

app = MyApp(Title="Canvas Example")
app.mainloop()
