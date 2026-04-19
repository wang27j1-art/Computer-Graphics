# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 13:46:18 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Checkerboard", 200, 200)

def draw_square(color, x, y, size, window):
     x1 = x
     y1 = y
     x2 = x + size
     y2 = y + size
     square = Rectangle(Point(x1, y1), Point(x2, y2))
     square.setFill(color)
     square.draw(win)
   
def make_checkerboard(num_rows, color_1, color_2):
    size = int(200 / num_rows)
    color = color_1
    top_color = color
    for x in range(0, 200, size):
        if color == top_color:
            if color == color_1:
                color = color_2
            else:
                color = color_1
        top_color = color
        for y in range(0, 200, size):
            draw_square(color, x, y, size, win)
            if color == color_1:
                color = color_2
            else:
                color = color_1

my_rows = int(input("How many rows? "))
my_color_1 = input("Pick a color: ")
my_color_2 = input("Pick another color: ")

make_checkerboard(my_rows, my_color_1, my_color_2)

win.getMouse()
win.close()