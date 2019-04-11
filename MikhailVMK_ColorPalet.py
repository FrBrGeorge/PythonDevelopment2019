from tkinter import *
from tkinter import colorchooser

from RgbNamedColors import Colors
def encodedColorValid(encodedColor):
    if not isinstance(encodedColor, str):
        return False
    if encodedColor in Colors.keys():
        return True
    if len(encodedColor) != 7:
        return False
    if encodedColor[0] != "#":
        return False
    for char in encodedColor[1:]:
        if not char.isdigit() and not char in "abcdefABCDEF":
            return False
    return True

def decodedColorValid(decodedColor):
    if not isinstance(decodedColor, tuple):
        return False
    if len(decodedColor) != 3:
        return False
    for color in decodedColor:
        if not isinstance(color, int):
            return False
        if color < 0 or color > 255:
            return False
    return True             

def getContrastColor(decodedColor):
    assert decodedColorValid(decodedColor)
    return ((decodedColor[0] + 128) % 256, (decodedColor[1] + 128) % 256, (decodedColor[2] + 128) % 256)

def encodeColor(decodedColor):
    assert decodedColorValid(decodedColor)
    colorString = "#"
    for i in range(0, len(decodedColor)):
        color = format(decodedColor[i], 'x')
        if len(color) == 1:
            colorString += '0'
        colorString += color    
    return colorString

def decodeColor(encodedColor):
    assert encodedColorValid(encodedColor)
    if encodedColor in Colors.keys():
        r = int(Colors[encodedColor][0])
        g = int(Colors[encodedColor][1])
        b = int(Colors[encodedColor][2])  
    else:      
        r = int(encodedColor[1:3], 16)
        g = int(encodedColor[3:5], 16)
        b = int(encodedColor[5:7], 16)
    return r, g, b


class ColorPalet(Frame):
    def __init__(self, root, color = "black"):
        Frame.__init__(self, root)
        self._toolColor = StringVar()
        self._toolColor.set(color)
        self._askColor = Button(self, text="Color", command=self._askcolor)
        self._askColor.grid(row=0, column=0, sticky=N+W)
        self._showColor = Entry(self,
                            textvariable=self._toolColor,
                            background =self._toolColor.get(),
                            foreground = encodeColor(getContrastColor(decodeColor(color))),
                            validatecommand = (self.register(decodedColorValid), '%P'),
                            validate='key')
        self._showColor.grid(row=1, column=0, sticky=N+W+E)
        
    def _askcolor(self):
        color = colorchooser.askcolor(color = self._toolColor.get())[1]
        self._toolColor.set(color)
        self._showColor.config(background = color)
        self._showColor.config(foreground = encodeColor(getContrastColor(decodeColor(color))))
    
    def getColor(self):
        return self._toolColor.get()       
