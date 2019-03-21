#!/usr/bin/env python3
'''
Convert rgb.txt to python code
'''

def convert(path="rgb.txt"):
    '''Read rgb.txt file into doctionary'''
    with open(path) as f:
        return { "".join(name):(r,g,b) for r, g, b, *name in (l.split() for l in f) }

if __name__ == "__main__":
    print("Colors =",str(convert()).replace("'), '","'),\n'"))
