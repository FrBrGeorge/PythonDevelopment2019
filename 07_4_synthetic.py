#!/usr/bin/env python3
'''
Пророждение события Tkinter
'''
import time
from tkinter import *
from threading import Thread, Event;


# TODO super()
class Clock(Thread):
    def __init__(self, root, grain=1, event="<<Tick>>"):
        super().__init__()
        self.root = root    # Окно, которому посылать событие
        self.grain = grain  # Размер одного тика в секундах (м. б дробный)
        self.event = event  # TKinter-событие, которое надо посылать
        self.done = Event() # threading-событие, которое останавливет тред

    def run(self):
        while not self.done.wait(self.grain):
            self.root.event_generate(self.event)

class App(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.grid()
        self.Clock = Clock(self)
        self.Time = StringVar()
        self.update_clock()
        self.Screen = Label(textvariable=self.Time)
        self.Screen.grid(row=0, column=0)
        self.Start = Button(text="Start", command=self.start)
        self.Start.grid(row=0, column=1)
        self.Quit = Button(text="Quit", command=self.quit)
        self.Quit.grid(row=0, column=2)
        self.bind(self.Clock.event, self.tick)
        # тред надо остановить, даже если окно просто закрыли
        self.bind("<Destroy>", self.quit)

    def tick(self, event):
        self.update_clock()

    def start(self):
        self.Clock.start()

    def quit(self, *events):
        self.Clock.done.set()
        self.master.quit()

    def update_clock(self):
        self.Time.set(time.strftime("%H:%M:%S"))

Tick = App()
Tick.mainloop()
