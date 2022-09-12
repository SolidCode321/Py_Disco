import random as rand
from graphics import *
from tkinter import *
import time

global circ_shape
global win
global frame
circ_array = []
nocirc = 5
ref = 5


class circl():
    def __init__(self):
        self.rad = 20
        self.pos = Point(rand.randint(0,300), rand.randint(0,300))
        self.rgb_value = color_rgb(rand.randint(0,255), rand.randint(0,255), rand.randint(0,255))


for i in range(nocirc):
    circ_array.append(circl())

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def change_color(win):
    for a in range(nocirc):
        print(hex_to_rgb(circ_array[a].rgb_value))
        cur_val = hex_to_rgb(circ_array[a].rgb_value)
        pre_val = hex_to_rgb(circ_array[a-1].rgb_value)
        for b in range(3):
            cur_val[b] += pre_val[b]
        print(hex_to_rgb(circ_array[a].rgb_value))
        circ_shape = Circle(circ_array[a].pos, circ_array[a].rad)
        circ_shape.setFill(circ_array[a].rgb_value)
        circ_shape.draw(win)
        win.flush()

def initscreen():
    win = GraphWin('disco', 500, 500)
    frame = Frame(win)

    for a in range(nocirc):
        circ_shape = Circle(circ_array[a].pos, circ_array[a].rad)
        circ_shape.setFill(circ_array[a].rgb_value)
        circ_shape.draw(win)

    for j in range(ref):
        clear_frame(frame)
        change_color(win)
        

    win.getMouse()
    win.close()


initscreen()


