#!/usr/bin/env python3
'''
Смешивание фреймворков: события threading и события tkinter не связаны
'''

import tkinter as tk
import time
from threading import Thread, Event

class MyThread(Thread):
    def __init__(self, event, root):
        Thread.__init__(self)
        self.stopped = event
        self.root = root

    def run(self):
        while not self.stopped.wait(1):
            self.root.update_clock()

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.grid()
        self.button = tk.Button(text="Quit", command = self.delayed_quit)
        self.button.grid()
        self.update_clock()
        self.stopped = Event()
        self.thread = MyThread(self.stopped, self)
        self.thread.start()
        self.root.mainloop()

    def delayed_quit(self):
        self.stopped.set()
        self.root.after(3000, self.root.quit)
        self.label.configure(text="Wait 3 secs")

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)

app=App()
