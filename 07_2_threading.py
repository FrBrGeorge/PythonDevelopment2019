#!/usr/bin/env python3
'''
Использование таймера из threading
'''

from threading import Thread, Event

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.5):
            print("my thread")

stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
input("А вы пока нажмите Enter\n")
stopFlag.set()
print("Тогда всё")
