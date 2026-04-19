# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 10:36:01 2026

@author: zahuo
"""
from graphics import *
import random

win = GraphWin("Squares", 600, 600)
win.setBackground("light blue")

# The square function
def make_a_square(win, x_loc, y_loc, size, color):
    point1 = Point(x_loc, y_loc)
    point2 = Point(x_loc + size, y_loc + size)
    my_square = Rectangle(point1, point2)
    my_square.setFill(color)
    my_square.draw(win)

go = True
while go == True:
    random_x_loc = random.randrange(0, 500)
    random_y_loc = random.randrange(0, 500)
    s = int(input("Enter a size: "))
    if s <= 0:
        go = False
        print("Invalid size. Click the screen to close the window and TRY AGAIN!!! :(")
    else:
        user_color = input("Enter a color: ")
        make_a_square(win, random_x_loc, random_y_loc, s, user_color)

win.getMouse()
win.close()